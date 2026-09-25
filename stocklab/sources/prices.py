"""Daily prices from Yahoo Finance (via yfinance). No API key needed."""
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

import pandas as pd

NEW_YORK = ZoneInfo("America/New_York")
SESSION_SETTLED = time(16, 15)  # a little after the 16:00 close, so the daily bar is final
MIN_SESSION_BARS = 70           # a full session has 78 five-minute bars


def _daily(raw):
    index = raw.index.tz_convert(NEW_YORK).tz_localize(None).normalize() if raw.index.tz is not None else raw.index.normalize()
    prices = raw.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].copy()
    prices.index = pd.DatetimeIndex(index, name="date")
    return prices[~prices.index.duplicated(keep="last")].dropna(subset=["open", "close"])


def bar_from_intraday(raw, day):
    """Today's daily bar built from its five-minute bars, or None unless the whole session is there."""
    if raw is None or raw.empty:
        return None
    bars = raw.rename(columns=str.lower)
    index = bars.index.tz_convert(NEW_YORK) if bars.index.tz is not None else bars.index.tz_localize(NEW_YORK)
    bars = bars.set_axis(index)
    session = bars[(index.date == day) & (index.time >= time(9, 30)) & (index.time < time(16, 0))].dropna(subset=["open", "close"])
    if len(session) < MIN_SESSION_BARS or session.index[-1].time() < time(15, 50):
        return None
    return pd.DataFrame({"open": [session["open"].iloc[0]], "high": [session["high"].max()], "low": [session["low"].min()],
                         "close": [session["close"].iloc[-1]], "volume": [session["volume"].sum()]},
                        index=pd.DatetimeIndex([pd.Timestamp(day)], name="date"))


def fetch_prices(ticker, years, now=None):
    import yfinance as yf

    now_ny = (now or datetime.now(NEW_YORK)).astimezone(NEW_YORK)
    t = yf.Ticker(ticker)
    start = (now_ny - timedelta(days=int(365.25 * years) + 120)).date()
    raw = t.history(start=start.isoformat(), interval="1d", auto_adjust=True, raise_errors=True)
    if raw is None or raw.empty:
        raise ValueError(f"no price data returned for {ticker}")
    prices = _daily(raw)
    today = now_ny.date()
    # Yahoo can take hours after the close to publish a stock's finished daily bar (index bars appear
    # sooner). Rather than skip the night, rebuild the bar from the session's five-minute bars.
    if now_ny.weekday() < 5 and now_ny.time() >= SESSION_SETTLED and prices.index[-1].date() < today:
        bar = bar_from_intraday(t.history(period="1d", interval="5m", prepost=False, auto_adjust=True), today)
        if bar is not None:
            prices = pd.concat([prices, bar])
    return prices


def drop_unfinished_session(prices, now):
    """If the run happens before today's close has settled, today's bar is still moving: drop it."""
    now_ny = now.astimezone(NEW_YORK)
    today = pd.Timestamp(now_ny.date())
    if len(prices) and prices.index[-1] == today and now_ny.time() < SESSION_SETTLED:
        return prices.iloc[:-1]
    return prices
