from collections import defaultdict
from datetime import timedelta

import numpy as np
import pandas as pd
import pytest

from stocklab.config import Config


def synthetic_prices(n=900, seed=0, persistence=0.0, start="2020-01-01"):
    """Fake daily bars. `persistence` > 0 plants a real pattern: each session's open->close move
    partly repeats the previous one, which a working model must discover."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(start, periods=n)
    shocks = rng.normal(0, 0.012, n)
    session = np.zeros(n)
    for t in range(n):
        session[t] = persistence * (session[t - 1] if t else 0.0) + shocks[t]
    gaps = rng.normal(0, 0.004, n)
    opens, closes, prev = np.empty(n), np.empty(n), 100.0
    for t in range(n):
        opens[t] = prev * np.exp(gaps[t])
        closes[t] = opens[t] * np.exp(session[t])
        prev = closes[t]
    return pd.DataFrame({
        "open": opens, "high": np.maximum(opens, closes) * 1.004, "low": np.minimum(opens, closes) * 0.996,
        "close": closes, "volume": rng.lognormal(15, 0.3, n),
    }, index=pd.DatetimeIndex(dates, name="date"))


class FakeSources:
    def __init__(self, prices, headlines=None):
        self.data = prices
        self.headline_items = headlines or {}
        self.health = defaultdict(lambda: {"ok": 0, "failed": 0, "items": 0, "last_error": ""})

    def prices(self, ticker, years):
        self.health["prices"]["ok"] += 1
        return self.data[ticker].copy()

    def headlines(self, ticker, now):
        return list(self.headline_items.get(ticker, []))

    def filing_dates(self, ticker):
        return None


@pytest.fixture
def config():
    return Config(tickers=["AAA", "BBB"], market="SPY", history_years=4, decision_threshold=0.55, cost_bps=5,
                  learning_rate=0.01, l2=1e-4, sources={})


def evening_after(date, hours=22, minutes=30):
    """A UTC timestamp after the US close on `date`."""
    return (pd.Timestamp(date) + timedelta(hours=hours, minutes=minutes)).tz_localize("UTC").to_pydatetime()
