"""Gradient boosting: a stronger, non-linear model that learns from every watched stock at once.

Where the online logistic model draws straight lines, boosting combines many small decision trees,
so it can pick up patterns like "a big drop only matters when volatility is low" or "earnings
tomorrow and the VIX is high". It is retrained from scratch (once a month over history, every day
live) on pooled data from all stocks, and only ever on sessions whose outcome was already known,
so its accuracy is out-of-sample too. Trees handle unknown (NaN) inputs natively.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier

from .features import BOOSTED

FEATURES = BOOSTED["gbm"]
MIN_TRAIN_ROWS = 500


def make_model():
    return HistGradientBoostingClassifier(max_iter=150, learning_rate=0.05, max_depth=3, min_samples_leaf=80,
                                          l2_regularization=1.0, random_state=0)


def training_data(frames, known_before, features=FEATURES, target="target_up"):
    """Every stock's rows whose outcome (the next session) finished strictly before `known_before`."""
    parts = [f.loc[f[target].notna() & (f["target_date"] < known_before), features + [target]] for f in frames.values()]
    data = pd.concat(parts) if parts else pd.DataFrame(columns=features + [target])
    return data[features].to_numpy(float), data[target].to_numpy(int)


class Fitted:
    """A trained model plus the features it uses: any feature with no known value at all in the
    training data (e.g. a source that was down) is left out rather than failing the whole fit."""

    def __init__(self, model, columns):
        self.model, self.columns = model, columns

    def predict_proba(self, X):
        return self.model.predict_proba(X[:, self.columns])


def fit(frames, known_before, features=FEATURES, target="target_up"):
    X, y = training_data(frames, known_before, features, target)
    if len(y) < MIN_TRAIN_ROWS or len(set(y)) < 2:
        return None
    columns = np.flatnonzero(~np.isnan(X).all(axis=0))
    if not len(columns):
        return None
    return Fitted(make_model().fit(X[:, columns], y), columns)


def walk_forward(frames, start_after, features=FEATURES, target="target_up"):
    """Out-of-sample probabilities for every known-outcome row after start_after[ticker] (None = all).
    Retrains at the start of each month on everything known before it. Returns {ticker: Series}."""
    wanted = {}
    for ticker, after in start_after.items():
        f = frames[ticker]
        dates = f.index[f[target].notna()]
        wanted[ticker] = dates if after is None else dates[dates > after]
    months = sorted({d.to_period("M") for dates in wanted.values() for d in dates})
    out = {t: [] for t in wanted}
    for month in months:
        cutoff = month.start_time
        model = fit(frames, cutoff, features, target)
        if model is None:
            continue
        for ticker, dates in wanted.items():
            in_month = dates[(dates >= cutoff) & (dates <= month.end_time)]
            if len(in_month):
                p = model.predict_proba(frames[ticker].loc[in_month, features].to_numpy(float))[:, 1]
                out[ticker].append(pd.Series(p, index=in_month))
    return {t: pd.concat(parts) if parts else pd.Series(dtype=float) for t, parts in out.items()}


def predict_latest(frames, tickers, features=FEATURES, target="target_up"):
    """Tonight's probability for each ticker's latest row, from a model trained on every outcome known so far."""
    latest = max(frames[t].index[-1] for t in tickers)
    model = fit(frames, latest + pd.Timedelta(days=1), features, target)
    if model is None:
        return {}
    rows = np.vstack([frames[t].loc[frames[t].index[-1], features].to_numpy(float) for t in tickers])
    return dict(zip(tickers, model.predict_proba(rows)[:, 1]))
