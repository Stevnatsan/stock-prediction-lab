"""Gradient boosting, the ensemble, the champion and the watchlist."""
import numpy as np
import pandas as pd
import pytest

from stocklab import boosting, watchlist
from stocklab.features import ALL_MODELS, ENSEMBLES, build_frame
from stocklab.pipeline import run_daily
from stocklab.report import CHAMPION_WINDOW, champion
from stocklab.state import State

from conftest import FakeSources, evening_after, synthetic_prices


def _frames(persistence, tickers=6, days=1200):
    market = synthetic_prices(days, seed=99)
    return {f"T{i}": build_frame(synthetic_prices(days, seed=i, persistence=persistence), market) for i in range(tickers)}


def _accuracy(frames):
    probs = boosting.walk_forward(frames, {t: None for t in frames})
    hits = [((p >= 0.5) == bool(frames[t].at[d, "target_up"])) for t, s in probs.items() for d, p in s.items()]
    return np.mean(hits), len(hits)


def test_boosting_trains_only_on_finished_sessions():
    frames = _frames(0.0, tickers=2, days=300)
    cutoff = frames["T0"].index[200]
    X, y = boosting.training_data(frames, cutoff)
    known = sum(int(((f["target_date"] < cutoff) & f["target_up"].notna()).sum()) for f in frames.values())
    assert len(y) == known and len(y) > 0
    assert all((f.loc[f["target_date"] < cutoff].index < cutoff).all() for f in frames.values())


def test_boosting_on_pure_noise_is_a_coin_flip():
    acc, n = _accuracy(_frames(0.0))
    assert n > 4000 and 0.47 < acc < 0.53, acc


def test_boosting_finds_a_real_pattern():
    acc, _ = _accuracy(_frames(0.6))
    assert acc > 0.62, acc


def test_champion_is_the_most_accurate_recent_model():
    days = pd.bdate_range("2024-01-01", periods=CHAMPION_WINDOW + 50)
    rows = []
    for i, d in enumerate(days):
        recent = i >= 50
        rows += [{"variant": "full", "feature_date": d, "correct": int(not recent)},   # great long ago, bad lately
                 {"variant": "gbm", "feature_date": d, "correct": int(recent)},
                 {"variant": "price", "feature_date": d, "correct": i % 2}]
    best, scores = champion(pd.DataFrame(rows))
    assert best == "gbm" and scores["gbm"] == 1.0


def test_new_models_and_reruns_never_duplicate_history(tmp_path, config):
    full = {t: synthetic_prices(420, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    day = full["AAA"].index[-1]
    for minutes in (0, 30):
        run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, evening_after(day) + pd.Timedelta(minutes=minutes))
    p = State.load(tmp_path / "s", config).predictions
    assert not p.duplicated(["ticker", "variant", "feature_date"]).any()
    assert set(p["variant"]) == set(ALL_MODELS)
    for ensemble, (a, b) in ENSEMBLES.items():
        ens = p[p["variant"] == ensemble].set_index(["ticker", "feature_date"])["p_up"]
        parts = p[p["variant"].isin([a, b])].pivot_table(index=["ticker", "feature_date"], columns="variant", values="p_up")
        assert len(ens) > 100
        np.testing.assert_allclose(ens, ((parts[a] + parts[b]) / 2).loc[ens.index], atol=1e-5)


def test_removed_stocks_lose_their_open_calls(tmp_path, config):
    full = {t: synthetic_prices(420, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    now = evening_after(full["AAA"].index[-1])
    run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, now)
    config.tickers = ["AAA"]
    run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, now)
    assert {x["ticker"] for x in State.load(tmp_path / "s", config).pending} == {"AAA"}


@pytest.fixture
def config_file(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("# comment kept\ntickers: [AAPL, MSFT]\nmarket: SPY\n")
    return path


def test_watchlist_add_and_remove(config_file):
    tickers, notes = watchlist.update("ko, brk.b, AAPL", "msft", config_path=config_file, known={"KO", "BRK-B", "AAPL"})
    assert tickers == ["AAPL", "KO", "BRK-B"] and notes == []
    text = config_file.read_text()
    assert "# comment kept" in text and "tickers: [AAPL, KO, BRK-B]" in text


def test_watchlist_rejects_bad_input(config_file):
    with pytest.raises(ValueError, match="valid"):
        watchlist.update("AAPL; rm -rf /", config_path=config_file, known=set())
    with pytest.raises(ValueError, match="empty"):
        watchlist.update(remove="AAPL MSFT", config_path=config_file, known=set())
    with pytest.raises(ValueError, match="limit"):
        watchlist.update(" ".join(f"S{i}" for i in range(watchlist.MAX_STOCKS)), config_path=config_file, known=set())
    assert "tickers: [AAPL, MSFT]" in config_file.read_text()


def test_unknown_symbols_are_allowed_with_a_note(config_file):
    tickers, notes = watchlist.update("SPY", config_path=config_file, known={"AAPL"})
    assert "SPY" in tickers and "not in the S&P 500" in notes[0]
