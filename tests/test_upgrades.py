"""FinBERT alongside VADER, rebuilding models when their inputs change, calibration, and the report."""
import json

import numpy as np
import pandas as pd

from stocklab.features import ALL_MODELS, signature
from stocklab.pipeline import run_daily
from stocklab.report import calibration
from stocklab.sources.news import headline_id
from stocklab.state import State

from conftest import FakeSources, evening_after, synthetic_prices

README = "# Lab\n\n<!-- scoreboard:start -->\nold\n<!-- scoreboard:end -->\n"


def _prices(n=420):
    return {t: synthetic_prices(n, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}


def _fake_finbert(texts):
    return [0.9 if "beats" in t else -0.8 if "lawsuit" in t else 0.0 for t in texts]


def test_headlines_are_scored_by_vader_and_finbert(tmp_path, config):
    full = _prices()
    now = evening_after(full["AAA"].index[-1])
    title = "AAA beats estimates"
    news = {"AAA": [{"id": headline_id(title), "title": title, "published": (now - pd.Timedelta(hours=2)).isoformat(),
                     "source": "test", "link": ""}]}
    sources = FakeSources(full, news, finbert=_fake_finbert, options={"AAA": {"iv_atm": 0.35, "put_call": -0.2}},
                          social={"AAA": [{"published": now.isoformat(), "mood": 1.0}]})
    run_daily(config, sources, tmp_path / "s", tmp_path / "r", None, now)
    stored = [json.loads(line) for line in (tmp_path / "s" / "news" / "AAA.jsonl").read_text().splitlines()]
    assert stored[0]["score"] > 0 and stored[0]["finbert"] == 0.9
    state = State.load(tmp_path / "s", config)
    call = next(p for p in state.pending if p["ticker"] == "AAA" and p["variant"] == "finbert")
    assert call["finbert_24h"] == 0.9 and call["sentiment_24h"] > 0
    live = state.live.set_index("ticker")
    assert live.at["AAA", "finbert_mean"] == 0.9 and live.at["AAA", "iv_atm"] == 0.35 and live.at["AAA", "social_mood"] == 1.0
    assert np.isnan(live.at["BBB", "finbert_mean"]) and np.isnan(live.at["BBB", "social_count"])


def test_changed_models_are_rebuilt_and_live_calls_kept(tmp_path, config):
    full = _prices()
    days = full["AAA"].index
    run_daily(config, FakeSources({t: df.iloc[:-2] for t, df in full.items()}), tmp_path / "s", tmp_path / "r", None,
              evening_after(days[-3]))
    run_daily(config, FakeSources({t: df.iloc[:-1] for t, df in full.items()}), tmp_path / "s", tmp_path / "r", None,
              evening_after(days[-2]))  # scores the first night's calls: now there are live rows
    before = State.load(tmp_path / "s", config).predictions

    # pretend the gradient boosting model used to have different inputs
    sig_path = tmp_path / "s" / "models" / "signatures.json"
    sigs = json.loads(sig_path.read_text())
    sigs["gbm"] = ["boosting", "up", "ret_1"]
    sig_path.write_text(json.dumps(sigs))

    state = State.load(tmp_path / "s", config)
    assert state.drop_stale_models() == ["gbm", "ensemble"]  # the ensemble depends on it
    run_daily(config, FakeSources({t: df.iloc[:-1] for t, df in full.items()}), tmp_path / "s", tmp_path / "r", None,
              evening_after(days[-2]) + pd.Timedelta(minutes=30))
    after = State.load(tmp_path / "s", config).predictions
    assert not after.duplicated(["ticker", "variant", "feature_date"]).any()
    for variant in ALL_MODELS:
        assert (after["variant"] == variant).sum() == (before["variant"] == variant).sum(), variant
    live_before = before[before["source"] == "live"].sort_values(["ticker", "variant"]).reset_index(drop=True)
    live_after = after[after["source"] == "live"].sort_values(["ticker", "variant"]).reset_index(drop=True)
    pd.testing.assert_frame_equal(live_before, live_after)
    assert json.loads(sig_path.read_text())["gbm"] == signature("gbm")
    assert State.load(tmp_path / "s", config).drop_stale_models() == []


def test_state_from_before_signatures_rebuilds_only_what_changed(tmp_path, config):
    full = _prices()
    run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, evening_after(full["AAA"].index[-1]))
    (tmp_path / "s" / "models" / "signatures.json").unlink()
    old_full = json.loads((tmp_path / "s" / "models" / "full" / "AAA.json").read_text())
    old_full["features"] = old_full["features"][:16]  # the old, shorter feature list
    old_full["weights"] = {f: 0.0 for f in old_full["features"]}
    for key in ("count", "mean", "m2"):
        old_full[key] = old_full[key][:16]
    (tmp_path / "s" / "models" / "full" / "AAA.json").write_text(json.dumps(old_full))
    stale = State.load(tmp_path / "s", config).drop_stale_models()
    assert "full" in stale and "price" not in stale and "finbert" not in stale
    assert set(stale) >= {"gbm", "beat_gbm", "ensemble", "beat_ensemble"}  # no record of their inputs: rebuilt


def test_calibration_tells_honest_from_overconfident():
    rng = np.random.default_rng(0)
    p = rng.uniform(0.4, 0.62, 20000)
    honest = pd.DataFrame({"p_up": p, "outcome_up": (rng.random(20000) < p).astype(float)})
    table, error = calibration(honest)
    assert error < 0.01 and (table["actual"] - table["predicted"]).abs().max() < 0.03
    coin = pd.DataFrame({"p_up": p, "outcome_up": (rng.random(20000) < 0.5).astype(float)})
    assert calibration(coin)[1] > 0.03  # claims 60% when it's really 50%


def test_report_covers_both_questions_calibration_and_orders(tmp_path, config):
    full = _prices()
    readme = tmp_path / "README.md"
    readme.write_text(README)
    (tmp_path / "s").mkdir()
    (tmp_path / "s" / "orders.csv").write_text(
        "session,ticker,qty,buy_price,sell_price,trade_return,buy_status,sell_status\n"
        f"{full['AAA'].index[-1].date()},AAA,10,100,101,0.01,filled,filled\n")
    run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", readme, evening_after(full["AAA"].index[-1]))
    board = readme.read_text()
    for text in ("Next-session calls", "P(beats SPY)", "Beats the market?", "Are the probabilities honest?", "(champion)"):
        assert text in board, text
    report = (tmp_path / "r" / "latest.md").read_text()
    for text in ("## Calibration", "VADER vs FinBERT", "Beats the market (market-neutral)", "1 round trips, profit/loss $+10.00"):
        assert text in report, text
    for chart in ("rolling_accuracy.png", "paper_trading.png", "calibration.png"):
        assert (tmp_path / "r" / chart).stat().st_size > 10_000
