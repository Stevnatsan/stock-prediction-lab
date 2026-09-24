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
    """Offline stand-in for LiveSources. Optional extras: `context` {ticker: {"earnings"/"analysts": frame}},
    `macro` (a FRED-like frame), `options`/`social` {ticker: value}, and a `finbert` scoring function."""

    def __init__(self, prices, headlines=None, context=None, macro=None, options=None, social=None, finbert=None, broker=None):
        self.data = prices
        self.headline_items = headlines or {}
        self.context = context or {}
        self.macro_data = macro
        self.options_data = options or {}
        self.social_data = social or {}
        self.finbert_fn = finbert
        self.broker = broker
        self.health = defaultdict(lambda: {"ok": 0, "failed": 0, "items": 0, "last_error": ""})

    def prices(self, ticker, years):
        self.health["prices"]["ok"] += 1
        return self.data[ticker].copy()

    def headlines(self, ticker, now):
        return list(self.headline_items.get(ticker, []))

    def filing_dates(self, ticker):
        return None

    def earnings(self, ticker):
        return self.context.get(ticker, {}).get("earnings")

    def analysts(self, ticker):
        return self.context.get(ticker, {}).get("analysts")

    def macro(self, years):
        return self.macro_data

    def options(self, ticker, now, spot):
        return self.options_data.get(ticker)

    def social(self, ticker, now):
        return self.social_data.get(ticker)

    def finbert(self, texts):
        return self.finbert_fn(texts) if self.finbert_fn else None


@pytest.fixture
def config():
    return Config(tickers=["AAA", "BBB"], market="SPY", history_years=4, decision_threshold=0.55, cost_bps=5,
                  learning_rate=0.01, l2=1e-4, sources={}, paper_orders={"enabled": True, "budget_per_stock": 10000})


def evening_after(date, hours=22, minutes=30):
    """A UTC timestamp after the US close on `date`."""
    return (pd.Timestamp(date) + timedelta(hours=hours, minutes=minutes)).tz_localize("UTC").to_pydatetime()
