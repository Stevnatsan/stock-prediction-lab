import json

import pytest

from stocklab import insight
from stocklab.pipeline import run_daily
from stocklab.sources.prices import with_retries
from stocklab.state import State

from conftest import FakeSources, evening_after, synthetic_prices


def test_price_stats_describe_a_known_series():
    prices = synthetic_prices(400, seed=4)
    prices["close"] = [100.0 + i for i in range(400)]  # a steady climb
    stats = insight.price_stats(prices, synthetic_prices(400, seed=5))
    assert stats["returns"]["1 week"] == pytest.approx(499 / 494 - 1)
    assert stats["off_high"] == 0
    assert stats["rsi_14"] == 100
    assert "Uptrend" in insight._trend(stats)
    assert set(stats["vs_market"]) == {"3 months", "1 year"}


def test_daily_run_writes_a_readable_insight(tmp_path, config):
    full = {t: synthetic_prices(400, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    run_daily(config, FakeSources(full), tmp_path / "state", tmp_path / "reports", None, evening_after(full["AAA"].index[-1]))
    brief = json.loads((tmp_path / "reports" / "insight.json").read_text())
    assert set(brief["stocks"]) == {"AAA", "BBB"}
    assert brief["stocks"]["AAA"]["models"]["up"]["p"] is not None
    text = (tmp_path / "reports" / "insight.md").read_text()
    assert "## AAA" in text and ("coin flip" in text or "edge" in text)


def test_insight_without_state_or_market():
    brief = insight.build({"AAA": synthetic_prices(300)}, None, None, evening_after("2021-03-01"))
    assert brief["market"] is None and brief["stocks"]["AAA"]["summary"]
    assert insight.to_markdown(brief).startswith("# Market insight")


def test_retries_until_the_source_answers():
    calls, waits = [], []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("rate limited")
        return "prices"

    assert with_retries(flaky, waits=(1, 2, 3), sleep=waits.append) == "prices"
    assert waits == [1, 2]
    with pytest.raises(ConnectionError):
        with_retries(lambda: (_ for _ in ()).throw(ConnectionError("down")), waits=(1,), sleep=lambda s: None)
