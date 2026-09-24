from datetime import datetime, timedelta, timezone

import pandas as pd

from stocklab.features import news_features, score_headlines
from stocklab.pipeline import run_daily
from stocklab.sentiment import score
from stocklab.sources.news import headline_id
from stocklab.sources.prices import drop_unfinished_session
from stocklab.state import State

from conftest import FakeSources, evening_after, synthetic_prices

README = "# Lab\n\n<!-- scoreboard:start -->\nold\n<!-- scoreboard:end -->\n\nrest\n"


def _headline(title, published):
    return {"id": headline_id(title), "title": title, "published": published.isoformat(), "source": "test", "link": ""}


def test_two_daily_runs_score_learn_and_predict(tmp_path, config):
    full = {t: synthetic_prices(400, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    day1 = full["AAA"].index[-2]
    readme = tmp_path / "README.md"
    readme.write_text(README)
    now1 = evening_after(day1)
    news = {"AAA": [_headline("AAA beats estimates, shares surge", now1 - timedelta(hours=3))]}

    sources = FakeSources({t: df.iloc[:-1] for t, df in full.items()}, news)
    summary = run_daily(config, sources, tmp_path / "state", tmp_path / "reports", readme, now1)
    assert summary["AAA"]["history_replayed"] > 250
    assert summary["AAA"]["headlines_24h"] == 1
    state = State.load(tmp_path / "state", config)
    assert len(state.pending) == 4  # 2 stocks x 2 model variants
    assert {p["feature_date"] for p in state.pending} == {day1.date().isoformat()}
    aaa_full = next(p for p in state.pending if p["ticker"] == "AAA" and p["variant"] == "full")
    assert aaa_full["sentiment_24h"] > 0

    # running again the same evening must not duplicate anything
    run_daily(config, FakeSources({t: df.iloc[:-1] for t, df in full.items()}, news), tmp_path / "state",
              tmp_path / "reports", readme, now1 + timedelta(minutes=20))
    assert len(State.load(tmp_path / "state", config).pending) == 4

    day2 = full["AAA"].index[-1]
    summary = run_daily(config, FakeSources(full), tmp_path / "state", tmp_path / "reports", readme, evening_after(day2))
    assert summary["AAA"]["scored"] == 2 and summary["BBB"]["scored"] == 2
    state = State.load(tmp_path / "state", config)
    live = state.predictions[state.predictions["source"] == "live"]
    assert len(live) == 4
    assert set(live["feature_date"].dt.date) == {day1.date()}
    assert {p["feature_date"] for p in state.pending} == {day2.date().isoformat()}

    board = readme.read_text()
    assert "old" not in board and "Next-session calls" in board and board.endswith("rest\n")
    assert (tmp_path / "reports" / "latest.md").exists()
    assert (tmp_path / "reports" / "rolling_accuracy.png").exists()
    assert (tmp_path / "reports" / "paper_trading.png").exists()


def test_missed_days_are_caught_up(tmp_path, config):
    full = {t: synthetic_prices(400, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    first = full["AAA"].index[-6]
    run_daily(config, FakeSources({t: df.loc[:first] for t, df in full.items()}), tmp_path / "s", tmp_path / "r",
              None, evening_after(first))
    summary = run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, evening_after(full["AAA"].index[-1]))
    assert summary["AAA"]["scored"] == 2      # the pending prediction from the first run
    assert summary["AAA"]["caught_up"] == 4   # the four sessions the bot missed
    predictions = State.load(tmp_path / "s", config).predictions
    assert not predictions.duplicated(["ticker", "variant", "feature_date"]).any()


def test_no_prediction_once_the_next_session_has_opened(tmp_path, config):
    full = {t: synthetic_prices(300, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    last = full["AAA"].index[-1]
    next_morning = (last + pd.offsets.BDay(1) + timedelta(hours=15)).tz_localize("UTC").to_pydatetime()  # ~11:00 New York
    summary = run_daily(config, FakeSources(full), tmp_path / "s", tmp_path / "r", None, next_morning)
    assert summary["AAA"]["history_replayed"] > 100
    assert summary["AAA"]["prediction"].startswith("skipped")
    assert State.load(tmp_path / "s", config).pending == []


def test_sentiment_reads_finance_headlines():
    assert score("Apple beats earnings expectations, shares surge") > 0.3
    assert score("Regulators open probe; analysts downgrade stock after lawsuit") < -0.3


def test_news_features_use_the_right_windows():
    now = datetime(2026, 3, 2, 22, 0, tzinfo=timezone.utc)
    items = score_headlines([
        _headline("Company beats estimates", now - timedelta(hours=2)),
        _headline("Company faces lawsuit", now - timedelta(hours=30)),
        _headline("Old news about a record quarter", now - timedelta(days=5)),
    ])
    f = news_features(items, now)
    assert f["sent_count"] == 1 and f["has_news"] == 1.0
    assert f["sent_mean"] > 0
    assert f["sent_3d"] < f["sent_mean"]  # the older negative headline pulls the 3-day mood down
    assert news_features([], now)["has_news"] == 0.0


def test_todays_bar_is_ignored_until_the_close_settles():
    prices = synthetic_prices(10, start="2026-03-02")
    today = prices.index[-1]
    during = (today + timedelta(hours=18)).tz_localize("UTC").to_pydatetime()   # 14:00 in New York
    after = (today + timedelta(hours=21, minutes=30)).tz_localize("UTC").to_pydatetime()
    assert drop_unfinished_session(prices, during).index[-1] < today
    assert drop_unfinished_session(prices, after).index[-1] == today


def test_headline_store_dedupes_and_prunes(tmp_path, config):
    state = State(tmp_path, config)
    now = datetime(2026, 3, 2, 22, 0, tzinfo=timezone.utc)
    fresh = _headline("Shares rally", now - timedelta(hours=1))
    stale = _headline("Ancient story", now - timedelta(days=10))
    stored = state.store_headlines("AAA", score_headlines([fresh, fresh, stale]), now)
    assert [h["title"] for h in stored] == ["Shares rally"]
    later = now + timedelta(days=40)
    assert state.store_headlines("AAA", [], later) == []
    assert pd.isna(news_features([], later)["sent_mean"])
