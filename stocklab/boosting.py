"""Gradient boosting: a stronger, non-linear model that learns from every watched stock at once.

Where the online logistic model draws straight lines, boosting combines many small decision trees,
so it can pick up patterns like "a big drop only matters when volatility is low". It is retrained
from scratch (once a month over history, every day live) on pooled data from all stocks, and only
ever on sessions whose outcome was already known, so its accuracy is out-of-sample too.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier

from .features import PRICE_FEATURES

FEATURES = PRICE_FEATURES
MIN_TRAIN_ROWS = 500


def make_model():
    return HistGradientBoostingClassifier(max_iter=150, learning_rate=0.05, max_depth=3, min_samples_leaf=80,
                                          l2_regularization=1.0, random_state=0)


def training_data(frames, known_before):
    """Every stock's rows whose outcome (the next session) finished strictly before `known_before`."""
    parts = [f.loc[f["target_up"].notna() & (f["target_date"] < known_before), FEATURES + ["target_up"]] for f in frames.values()]
    data = pd.concat(parts) if parts else pd.DataFrame(columns=FEATURES + ["target_up"])
    return data[FEATURES].to_numpy(float), data["target_up"].to_numpy(int)


def fit(frames, known_before):
    X, y = training_data(frames, known_before)
    if len(y) < MIN_TRAIN_ROWS or len(set(y)) < 2:
        return None
    return make_model().fit(X, y)


def walk_forward(frames, start_after):
    """Out-of-sample probabilities for every known-outcome row after start_after[ticker] (None = all).
    Retrains at the start of each month on everything known before it. Returns {ticker: Series}."""
    wanted = {}
    for ticker, after in start_after.items():
        f = frames[ticker]
        dates = f.index[f["target_up"].notna()]
        wanted[ticker] = dates if after is None else dates[dates > after]
    months = sorted({d.to_period("M") for dates in wanted.values() for d in dates})
    out = {t: [] for t in wanted}
    for month in months:
        cutoff = month.start_time
        model = fit(frames, cutoff)
        if model is None:
            continue
        for ticker, dates in wanted.items():
            in_month = dates[(dates >= cutoff) & (dates <= month.end_time)]
            if len(in_month):
                p = model.predict_proba(frames[ticker].loc[in_month, FEATURES].to_numpy(float))[:, 1]
                out[ticker].append(pd.Series(p, index=in_month))
    return {t: pd.concat(parts) if parts else pd.Series(dtype=float) for t, parts in out.items()}


def predict_latest(frames, tickers):
    """Tonight's P(up) for each ticker's latest row, from a model trained on every outcome known so far."""
    latest = max(frames[t].index[-1] for t in tickers)
    model = fit(frames, latest + pd.Timedelta(days=1))
    if model is None:
        return {}
    rows = np.vstack([frames[t].loc[frames[t].index[-1], FEATURES].to_numpy(float) for t in tickers])
    return dict(zip(tickers, model.predict_proba(rows)[:, 1]))
