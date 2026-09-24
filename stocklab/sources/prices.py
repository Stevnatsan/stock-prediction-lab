"""Daily prices from Yahoo Finance (via yfinance). No API key needed."""
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

import pandas as pd

NEW_YORK = ZoneInfo("America/New_York")
SESSION_SETTLED = time(16, 15)  # a little after the 16:00 close, so the daily bar is final


def fetch_prices(ticker, years):
    import yfinance as yf

    start = (datetime.now(NEW_YORK) - timedelta(days=int(365.25 * years) + 120)).date()
    raw = yf.Ticker(ticker).history(start=start.isoformat(), interval="1d", auto_adjust=True, raise_errors=True)
    if raw is None or raw.empty:
        raise ValueError(f"no price data returned for {ticker}")
    index = raw.index.tz_convert(NEW_YORK).tz_localize(None).normalize() if raw.index.tz is not None else raw.index.normalize()
    prices = raw.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].copy()
    prices.index = pd.DatetimeIndex(index, name="date")
    return prices[~prices.index.duplicated(keep="last")].dropna(subset=["open", "close"])


def drop_unfinished_session(prices, now):
    """If the run happens before today's close has settled, today's bar is still moving: drop it."""
    now_ny = now.astimezone(NEW_YORK)
    today = pd.Timestamp(now_ny.date())
    if len(prices) and prices.index[-1] == today and now_ny.time() < SESSION_SETTLED:
        return prices.iloc[:-1]
    return prices
