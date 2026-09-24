"""Company events from Yahoo Finance (via yfinance), with years of history so the models can learn from
the past: earnings dates with EPS surprises, and analyst rating changes with price-target revisions."""
import numpy as np
import pandas as pd

from .prices import NEW_YORK


def _new_york(index):
    index = pd.DatetimeIndex(index)
    return index.tz_convert(NEW_YORK).tz_localize(None) if index.tz is not None else index


def earnings_events(ticker, limit=40):
    """Past and scheduled earnings reports (about 10 years back, the next few ahead)."""
    import yfinance as yf

    return normalise_earnings(yf.Ticker(ticker).get_earnings_dates(limit=limit))


def normalise_earnings(raw):
    if raw is None or raw.empty:
        raise ValueError("no earnings dates returned")
    released = _new_york(raw.index)
    # a report with no time of day is assumed to come after the close: never earlier than it really was
    released = pd.DatetimeIndex([t + pd.Timedelta(hours=16) if t == t.normalize() else t for t in released])
    surprise = (pd.to_numeric(raw["Surprise(%)"], errors="coerce").to_numpy(float) if "Surprise(%)" in raw
                else np.full(len(raw), np.nan))
    events = pd.DataFrame({"released": released, "surprise": surprise})
    return events.drop_duplicates("released").sort_values("released").reset_index(drop=True)


def analyst_actions(ticker):
    """Every analyst rating change / price-target change Yahoo has on record."""
    import yfinance as yf

    return normalise_analysts(yf.Ticker(ticker).upgrades_downgrades)


def normalise_analysts(raw):
    if raw is None or raw.empty:
        raise ValueError("no analyst actions returned")
    action = raw["Action"].astype(str).str.lower() if "Action" in raw else pd.Series("", index=raw.index)
    rating = np.select([action.eq("up"), action.eq("down")], [1.0, -1.0], 0.0)
    target = np.full(len(raw), np.nan)
    if {"currentPriceTarget", "priorPriceTarget"} <= set(raw.columns):
        new = pd.to_numeric(raw["currentPriceTarget"], errors="coerce").to_numpy(float)
        old = pd.to_numeric(raw["priorPriceTarget"], errors="coerce").to_numpy(float)
        ok = (new > 0) & (old > 0)
        target[ok] = np.log(new[ok] / old[ok])
    actions = pd.DataFrame({"time": _new_york(raw.index), "rating": rating, "target": target})
    return actions.sort_values("time").reset_index(drop=True)
