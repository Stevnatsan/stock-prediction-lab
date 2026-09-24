"""Features known at the close of day t, and the two questions the models answer about the NEXT session:

    up    will the stock close above its open?
    beat  will its open -> close return beat the market's (SPY) over the same session?

Predicting the next session (open -> close) rather than close -> close matches how the bot runs:
it decides after the close, so the earliest it could act is the next morning's open.

Features come in two kinds. *Historical* ones (prices, earnings dates, analyst revisions, macro data,
SEC filings) can be rebuilt for any past day, so the models learn them from years of history.
*Live-only* ones (headlines, options-implied volatility, social media) can't be looked up for the past,
so they are unknown (NaN) on historical rows and only start to matter once the bot has collected them.
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
CONTEXT_FEATURES = [
    "earn_next",           # 1 if the company reports earnings before the next session closes
    "earn_days_since",     # calendar days since the last earnings report
    "earn_surprise",       # last report's EPS surprise, % vs analysts' estimate
    "analyst_rating_30d",  # analyst upgrades minus downgrades, last 30 days
    "analyst_target_30d",  # average price-target revision (log of new / old target), last 30 days
    "vix",                 # CBOE volatility index (FRED), previous day
    "vix_chg_5",           # VIX change over a week
    "rate_chg_5",          # 10-year Treasury yield change over a week, percentage points
    "curve_10y3m",         # yield curve: 10-year Treasury minus 3-month bill
    "filings_5d",          # 8-K filings with the SEC in the last 5 days
]
VADER_FEATURES = [
    "sent_mean",    # average headline sentiment (VADER), last 24 h
    "sent_count",   # number of headlines, last 24 h
    "sent_3d",      # sentiment over 3 days, recent headlines weighted more
    "has_news",     # 1 if any headline in the last 24 h
]
FINBERT_FEATURES = ["finbert_mean", "sent_count", "finbert_3d", "has_news"]  # the same, scored by FinBERT
MARKET_LIVE_FEATURES = [
    "iv_atm",        # at-the-money implied volatility from the options market
    "iv_premium",    # implied vs realised volatility (log ratio): is a bigger move than usual priced in?
    "put_call",      # log(put volume / call volume)
    "social_count",  # StockTwits + Reddit posts, last 24 h (log scale)
    "social_mood",   # StockTwits bull/bear labels and Reddit title sentiment, -1 to 1
]
LIVE_FEATURES = list(dict.fromkeys(VADER_FEATURES + FINBERT_FEATURES + MARKET_LIVE_FEATURES))
HISTORICAL = PRICE_FEATURES + CONTEXT_FEATURES

# Online logistic regressions, one per stock and model. "price" is the control: nothing but prices.
# "full" and "finbert" differ only in how headlines are scored, so their live accuracy compares the two.
VARIANTS = {
    "price": PRICE_FEATURES,
    "full": HISTORICAL + VADER_FEATURES + MARKET_LIVE_FEATURES,
    "finbert": HISTORICAL + FINBERT_FEATURES + MARKET_LIVE_FEATURES,
    "beat_full": HISTORICAL + VADER_FEATURES + MARKET_LIVE_FEATURES,
}
# Gradient boosting, pooled across stocks, trained only on features that exist for the past.
BOOSTED = {"gbm": HISTORICAL, "beat_gbm": HISTORICAL}
# Averages of a logistic and a boosting model.
ENSEMBLES = {"ensemble": ("full", "gbm"), "beat_ensemble": ("beat_full", "beat_gbm")}
ALL_MODELS = list(VARIANTS) + list(BOOSTED) + list(ENSEMBLES)

# Per question: (outcome column, realised return column, today's version of the outcome for the
# "same as today" baseline). For "beat", returns are the stock's minus the market's.
TASKS = {"up": ("target_up", "target_ret", "session_ret"), "beat": ("target_beat", "target_excess", "session_excess")}
LEAD_MODEL = {"up": "full", "beat": "beat_full"}  # the logistic model other models' calls are filed alongside


def task_of(variant):
    return "beat" if variant.startswith("beat_") else "up"


def signature(variant):
    """What a model's predictions depend on. When this changes, the model is rebuilt from history."""
    if variant in VARIANTS:
        return ["logistic", task_of(variant), *VARIANTS[variant]]
    if variant in BOOSTED:
        return ["boosting", task_of(variant), *BOOSTED[variant]]
    a, b = ENSEMBLES[variant]
    return ["mean", signature(a), signature(b)]


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
    f["session_excess"] = f["session_ret"] - np.log(market["close"] / market["open"]).reindex(prices.index)
    return f.replace([np.inf, -np.inf], np.nan)


def targets(prices, market):
    """For row t: the next session's open -> close return, whether it was up, and whether it beat the
    market's own open -> close return that session. NaN on the last row (tomorrow is unknown)."""
    session = prices["close"].shift(-1) / prices["open"].shift(-1) - 1
    market_session = (market["close"] / market["open"] - 1).reindex(prices.index).shift(-1)
    t = pd.DataFrame(index=prices.index)
    t["target_ret"] = session
    t["target_up"] = (session > 0).astype(float).where(session.notna())
    t["target_excess"] = session - market_session
    t["target_beat"] = (t["target_excess"] > 0).astype(float).where(t["target_excess"].notna())
    t["target_date"] = pd.Series(prices.index, index=prices.index).shift(-1)
    return t


def filings_feature(index, filing_dates, days=5):
    """How many 8-Ks were filed in the `days` calendar days up to and including each date."""
    if filing_dates is None:
        return pd.Series(np.nan, index=index)
    stamps = pd.to_datetime(pd.Series(sorted(filing_dates)))
    counts = [int(((stamps > d - timedelta(days=days)) & (stamps <= d)).sum()) for d in index]
    return pd.Series(counts, index=index, dtype=float)


CLOSE = pd.Timedelta(hours=16)
KNOWN_BY = pd.Timedelta(hours=17)  # the daily run starts after 17:00 New York time
CALENDAR_REACH = pd.Timedelta(days=100)


def earnings_features(index, events):
    """`events`: DataFrame with 'released' (New York time, naive) and 'surprise' (%). A report is
    *upcoming* for row t if it lands between t's close and the next session's close (companies announce
    their dates weeks ahead), and its surprise is only used once it has been released."""
    f = pd.DataFrame(np.nan, index=index, columns=["earn_next", "earn_days_since", "earn_surprise"])
    if events is None or not len(events):
        return f
    events = events.sort_values("released")
    released = pd.DatetimeIndex(events["released"])
    surprise = events["surprise"].ffill().to_numpy(float)  # the latest known surprise at each report
    closes = index + CLOSE
    next_closes = closes[1:].append(pd.DatetimeIndex([closes[-1] + pd.offsets.BDay(1)]))
    for day, close, next_close in zip(index, closes, next_closes):
        if close < released[0] - CALENDAR_REACH or close > released[-1] + CALENDAR_REACH:
            continue  # outside the period the calendar covers: unknown, not "no earnings"
        f.at[day, "earn_next"] = float(((released >= close) & (released < next_close)).any())
        last = released.searchsorted(close, side="left") - 1  # most recent report strictly before the close
        if last >= 0:
            f.at[day, "earn_days_since"] = min((close - released[last]).days, 120)
            f.at[day, "earn_surprise"] = float(np.clip(surprise[last], -50, 50))
    return f


def analyst_features(index, actions, days=30):
    """`actions`: DataFrame with 'time' (New York, naive), 'rating' (+1 upgrade, -1 downgrade, 0 other)
    and 'target' (log of new / old price target, NaN if none). Counts only what was public by the run."""
    f = pd.DataFrame(np.nan, index=index, columns=["analyst_rating_30d", "analyst_target_30d"])
    if actions is None or not len(actions):
        return f
    actions = actions.sort_values("time")
    times = pd.DatetimeIndex(actions["time"])
    rating, target = actions["rating"].to_numpy(float), actions["target"].to_numpy(float)
    for day in index:
        cutoff = day + KNOWN_BY
        if cutoff < times[0]:
            continue  # before the history we have: unknown
        lo, hi = times.searchsorted(cutoff - pd.Timedelta(days=days), side="right"), times.searchsorted(cutoff, side="right")
        f.at[day, "analyst_rating_30d"] = float(rating[lo:hi].sum())
        revisions = target[lo:hi][np.isfinite(target[lo:hi])]
        f.at[day, "analyst_target_30d"] = float(revisions.mean()) if len(revisions) else 0.0
    return f


def macro_features(index, macro):
    """`macro`: daily series (vix, rate_10y, curve = 10-year minus 3-month) indexed by observation date. FRED publishes a
    day's value the next morning, so row t uses the latest observation from *before* t."""
    cols = ["vix", "vix_chg_5", "rate_chg_5", "curve_10y3m"]
    if macro is None or not len(macro):
        return pd.DataFrame(np.nan, index=index, columns=cols)
    m = macro.sort_index().ffill()
    m = m.assign(vix_chg_5=np.log(m["vix"] / m["vix"].shift(5)), rate_chg_5=m["rate_10y"].diff(5), curve_10y3m=m["curve"])[cols]
    pos = m.index.searchsorted(index, side="left") - 1
    values = m.to_numpy(float)[np.clip(pos, 0, None)]
    values[pos < 0] = np.nan
    return pd.DataFrame(values, index=index, columns=cols)


def build_frame(prices, market, context=None):
    """Features + targets for every day. `context` may hold 'filings', 'earnings', 'analysts', 'macro';
    any that are missing stay unknown (NaN) rather than being treated as zero. Live-only features are
    NaN on every historical row, otherwise the model would learn that "no news" is normal and treat
    the first live headline as a five-standard-deviation event."""
    context = context or {}
    frame = price_features(prices, market).join(targets(prices, market))
    frame["close"] = prices["close"]  # not a feature: sizes paper orders
    frame["filings_5d"] = filings_feature(frame.index, context.get("filings"))
    frame = frame.join(earnings_features(frame.index, context.get("earnings")))
    frame = frame.join(analyst_features(frame.index, context.get("analysts")))
    frame = frame.join(macro_features(frame.index, context.get("macro")))
    for col in LIVE_FEATURES:
        frame[col] = np.nan
    return frame.dropna(subset=PRICE_FEATURES)


def _age_hours(item, now):
    return (now - pd.Timestamp(item["published"]).to_pydatetime()).total_seconds() / 3600


def news_features(headlines, now, score_key="score", prefix="sent"):
    """Sentiment features from stored headlines (each with an ISO 'published' time and a score)."""
    last_day, last_3d, count = [], [], 0
    for h in headlines:
        age = _age_hours(h, now)
        count += 0 <= age <= 24
        s = h.get(score_key)
        if s is None:
            continue
        if 0 <= age <= 24:
            last_day.append(s)
        if 0 <= age <= 72:
            last_3d.append((s, 0.5 ** (age / 24)))
    weights = sum(w for _, w in last_3d)
    return {
        f"{prefix}_mean": float(np.mean(last_day)) if last_day else np.nan,
        f"{prefix}_3d": float(sum(s * w for s, w in last_3d) / weights) if weights else np.nan,
        "sent_count": float(count),
        "has_news": 1.0 if count else 0.0,
    }


def social_features(posts, now):
    """`posts`: dicts with 'published' and 'mood' (-1..1, or None if it carries no opinion).
    None means no social source was available: unknown, not "nobody is talking about it"."""
    if posts is None:
        return {"social_count": np.nan, "social_mood": np.nan}
    recent = [p for p in posts if 0 <= _age_hours(p, now) <= 24]
    moods = [p["mood"] for p in recent if p.get("mood") is not None]
    return {"social_count": float(np.log1p(len(recent))), "social_mood": float(np.mean(moods)) if moods else np.nan}


def live_features(row, headlines, options, posts, now):
    """Everything collected tonight that doesn't exist for past days."""
    f = news_features(headlines, now)
    f.update(news_features(headlines, now, score_key="finbert", prefix="finbert"))
    options = options or {}
    iv = options.get("iv_atm", np.nan)
    realised = row["vol_20"] * np.sqrt(252)
    f["iv_atm"] = iv
    f["iv_premium"] = float(np.log(iv / realised)) if np.isfinite(iv) and iv > 0 and realised > 0 else np.nan
    f["put_call"] = options.get("put_call", np.nan)
    f.update(social_features(posts, now))
    return f


def score_headlines(items):
    return [{**item, "score": round(sentiment.score(item["title"]), 4)} for item in items]
