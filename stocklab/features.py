"""Features known at the close of day t, and the target: did the NEXT session close above its open?

Predicting the next session (open -> close) rather than close -> close matches how the bot runs:
it decides after the close, so the earliest it could act is the next morning's open.
"""
from datetime import timedelta

import numpy as np
import pandas as pd

from . import sentiment

PRICE_FEATURES = [
    "ret_1",        # yesterday -> today close, log return
    "ret_5",        # one week
    "ret_20",       # one month
    "vol_20",       # 20-day volatility of daily returns
    "rsi_14",       # relative strength index (Wilder, 14 days)
    "dist_sma50",   # distance of close from its 50-day average
    "volume_z",     # today's volume vs the last 20 days
    "gap",          # overnight gap: today's open vs yesterday's close
    "session_ret",  # today's open -> close move
    "mkt_ret_1",    # market (SPY) daily return
    "mkt_ret_5",    # market weekly return
]
NEWS_FEATURES = [
    "sent_mean",    # average headline sentiment, last 24 h
    "sent_count",   # number of headlines, last 24 h
    "sent_3d",      # sentiment over 3 days, recent headlines weighted more
    "has_news",     # 1 if any headline in the last 24 h
    "filings_5d",   # 8-K filings with the SEC in the last 5 days
]
VARIANTS = {"price": PRICE_FEATURES, "full": PRICE_FEATURES + NEWS_FEATURES}


def _rsi(close, window=14):
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
    return 100 - 100 / (1 + gain / loss)  # no down days -> gain/loss = inf -> RSI 100


def price_features(prices, market):
    c, o = prices["close"], prices["open"]
    log_ret = np.log(c).diff()
    f = pd.DataFrame(index=prices.index)
    f["ret_1"] = log_ret
    f["ret_5"] = np.log(c / c.shift(5))
    f["ret_20"] = np.log(c / c.shift(20))
    f["vol_20"] = log_ret.rolling(20).std()
    f["rsi_14"] = _rsi(c)
    f["dist_sma50"] = c / c.rolling(50).mean() - 1
    volume = np.log1p(prices["volume"].astype(float))
    f["volume_z"] = (volume - volume.rolling(20).mean()) / volume.rolling(20).std()
    f["gap"] = np.log(o / c.shift(1))
    f["session_ret"] = np.log(c / o)
    market_close = market["close"].reindex(prices.index).ffill()
    f["mkt_ret_1"] = np.log(market_close).diff()
    f["mkt_ret_5"] = np.log(market_close / market_close.shift(5))
    return f.replace([np.inf, -np.inf], np.nan)


def targets(prices):
    """For row t: the next session's open -> close return and whether it was up. NaN on the last row."""
    next_open, next_close = prices["open"].shift(-1), prices["close"].shift(-1)
    session = next_close / next_open - 1
    t = pd.DataFrame(index=prices.index)
    t["target_ret"] = session
    t["target_up"] = (session > 0).astype(float).where(session.notna())
    t["target_date"] = pd.Series(prices.index, index=prices.index).shift(-1)
    return t


def filings_feature(index, filing_dates, days=5):
    """How many 8-Ks were filed in the `days` calendar days up to and including each date."""
    if filing_dates is None:
        return pd.Series(np.nan, index=index)
    stamps = pd.to_datetime(pd.Series(sorted(filing_dates)))
    counts = [int(((stamps > d - timedelta(days=days)) & (stamps <= d)).sum()) for d in index]
    return pd.Series(counts, index=index, dtype=float)


def build_frame(prices, market, filing_dates=None):
    """Price features + filings + targets. Past headlines can't be fetched, so every news feature is
    *unknown* (NaN) on historical rows, not zero. Otherwise the model would learn that "no news" is
    normal and treat the first live headline as a five-standard-deviation event."""
    frame = price_features(prices, market).join(targets(prices))
    frame["filings_5d"] = filings_feature(frame.index, filing_dates)
    for col in ("sent_mean", "sent_count", "sent_3d", "has_news"):
        frame[col] = np.nan
    return frame.dropna(subset=PRICE_FEATURES)


def news_features(headlines, now):
    """Sentiment features from stored headlines (each with an ISO 'published' time and a 'score')."""
    last_day, last_3d = [], []
    for h in headlines:
        age_hours = (now - pd.Timestamp(h["published"]).to_pydatetime()).total_seconds() / 3600
        if 0 <= age_hours <= 24:
            last_day.append(h["score"])
        if 0 <= age_hours <= 72:
            last_3d.append((h["score"], 0.5 ** (age_hours / 24)))
    weights = sum(w for _, w in last_3d)
    return {
        "sent_mean": float(np.mean(last_day)) if last_day else np.nan,
        "sent_count": float(len(last_day)),
        "sent_3d": float(sum(s * w for s, w in last_3d) / weights) if weights else np.nan,
        "has_news": 1.0 if last_day else 0.0,
    }


def score_headlines(items):
    return [{**item, "score": round(sentiment.score(item["title"]), 4)} for item in items]
