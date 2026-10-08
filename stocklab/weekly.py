"""The week-ahead question: buy at the next open and hold for a week (5 sessions). Will the stock be
higher at that week's last close, and will it beat the market (SPY) over the same week?

Two candidates answer it, and the better one is used:

    usual odds  how often the watched stocks rose (or beat SPY) in the weeks of the past year
    model       a strongly regularised logistic regression on trend, momentum, volatility and macro
                inputs, pulled halfway toward the usual odds so it can't stray far on thin evidence

Both are scored walk-forward: each month of history is predicted only from weeks that had already
ended before that month began. The candidate with the lower Brier score (mean squared error of the
probability) over that test is the *champion* whose odds are shown. Over a week most of a stock's
move is noise, and when this was written the usual odds were the champion: the model is kept
running so the page switches by itself if it ever does better.

Next to the odds each stock gets context that is description, not forecast: its typical weekly range,
whether it looks stretched or beaten down, and how often it rose after similar setups before.
Live calls go to state/weekly.csv and are scored once their week is over. A run that happens after the
week's first session has opened still shows the odds but doesn't log them: they would no longer be a
call made before the week began.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .sources.prices import next_session_started

HORIZON = 5  # sessions
FEATURES = ["ret_5", "ret_20", "ret_60", "ret_120", "dist_sma50", "dist_sma200", "vol_20", "rsi_14", "mkt_ret_5", "vix", "curve_10y3m"]
QUESTIONS = {"up": ("target_wk_up", "week_return"), "beat": ("target_wk_beat", "excess_return")}
RECENT = pd.Timedelta(days=365)  # the usual odds look back this far
MIN_TRAIN_ROWS = 500
RSI_STATES = [(0, 40, "beaten down"), (40, 60, "normal"), (60, 101, "stretched")]
COLUMNS = ["ticker", "feature_date", "p_up", "p_beat", "source", "target_date", "week_return", "excess_return",
           "outcome_up", "outcome_beat", "made_at"]


def week_frame(frame, prices, market):
    """The daily feature frame plus long momentum and the week-ahead targets. Row t's week runs from
    the open of session t+1 to the close of session t+5; target_date is that last session."""
    close, opens = prices["close"].reindex(frame.index), prices["open"].reindex(frame.index)
    full_close = prices["close"]
    f = frame.copy()
    f["ret_60"] = np.log(full_close / full_close.shift(60)).reindex(frame.index)
    f["ret_120"] = np.log(full_close / full_close.shift(120)).reindex(frame.index)
    f["dist_sma200"] = (full_close / full_close.rolling(200).mean() - 1).reindex(frame.index)
    week = close.shift(-HORIZON) / opens.shift(-1) - 1
    m_close, m_open = market["close"].reindex(frame.index), market["open"].reindex(frame.index)
    f["week_return"] = week
    f["excess_return"] = week - (m_close.shift(-HORIZON) / m_open.shift(-1) - 1)
    f["target_wk_up"] = (week > 0).astype(float).where(week.notna())
    f["target_wk_beat"] = (f["excess_return"] > 0).astype(float).where(f["excess_return"].notna())
    f["target_date"] = pd.Series(frame.index, index=frame.index).shift(-HORIZON)
    for col in FEATURES:
        if col not in f:
            f[col] = np.nan
    return f


def pooled(weeks):
    return pd.concat([w.assign(ticker=t) for t, w in weeks.items()]).sort_index()


def usual_odds(data, target, known_before):
    """Share of yes among the weeks that ended in the year before `known_before`."""
    done = data[(data["target_date"] < known_before) & (data["target_date"] >= known_before - RECENT)][target].dropna()
    return float(done.mean()) if len(done) else 0.5


def fit_model(data, target, known_before):
    train = data[data[target].notna() & (data["target_date"] < known_before)]
    if len(train) < MIN_TRAIN_ROWS or train[target].nunique() < 2:
        return None
    cols = [c for c in FEATURES if train[c].notna().any()]
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(C=0.01, max_iter=500))
    return model.fit(train[cols].to_numpy(float), train[target].astype(int)), cols


def model_odds(fitted, rows, usual):
    model, cols = fitted
    return 0.5 * model.predict_proba(rows[cols].to_numpy(float))[:, 1] + 0.5 * usual


def walk_forward(data, target, ret):
    """Monthly out-of-sample test of both candidates over every finished week after the first year."""
    known = data[data[target].notna()]
    if known.empty:
        return pd.DataFrame(columns=["ticker", "y", "ret", "usual", "model"])
    first = (known.index.min() + RECENT).to_period("M")
    parts = []
    for month in pd.period_range(first, known.index.max().to_period("M"), freq="M"):
        cut = month.start_time
        test = known[(known.index >= cut) & (known.index <= month.end_time)]
        fitted = fit_model(data, target, cut)
        if test.empty or fitted is None:
            continue
        usual = usual_odds(data, target, cut)
        parts.append(pd.DataFrame({"ticker": test["ticker"], "y": test[target], "ret": test[ret], "usual": usual,
                                   "model": model_odds(fitted, test, usual)}, index=test.index))
    return pd.concat(parts) if parts else pd.DataFrame(columns=["ticker", "y", "ret", "usual", "model"])


def score(test):
    out = {"weeks": int(len(test)), "from": test.index.min().date().isoformat() if len(test) else None}
    for c in ("usual", "model"):
        p, y = test[c].to_numpy(float), test["y"].to_numpy(float)
        out[c] = {"accuracy": float(((p >= 0.5) == (y == 1)).mean()) if len(y) else None,
                  "brier": float(((p - y) ** 2).mean()) if len(y) else None}
    better = out["model"]["brier"] is not None and out["model"]["brier"] < out["usual"]["brier"]
    out["champion"] = "model" if better else "usual"
    return out


def rsi_state(rsi):
    for lo, hi, name in RSI_STATES:
        if lo <= rsi < hi:
            return name
    return "normal"


def context(week):
    """Description of one stock's weeks: typical range, current setup, how similar setups went."""
    done = week.dropna(subset=["week_return"])
    recent = done[done.index >= done.index.max() - pd.Timedelta(days=730)] if len(done) else done
    last = week.iloc[-1]
    state = rsi_state(float(last["rsi_14"])) if pd.notna(last["rsi_14"]) else None
    above = bool(last["dist_sma200"] > 0) if pd.notna(last["dist_sma200"]) else None
    similar = done
    if state is not None:
        lo, hi = next((lo, hi) for lo, hi, n in RSI_STATES if n == state)
        similar = similar[(similar["rsi_14"] >= lo) & (similar["rsi_14"] < hi)]
    if above is not None:
        similar = similar[(similar["dist_sma200"] > 0) == above]
    q = recent["week_return"].quantile([0.1, 0.5, 0.9]).tolist() if len(recent) >= 20 else [None] * 3
    return {"rsi": float(last["rsi_14"]) if pd.notna(last["rsi_14"]) else None, "state": state, "above_200d": above,
            "range_low": q[0], "median": q[1], "range_high": q[2],
            "up_share_2y": float((recent["week_return"] > 0).mean()) if len(recent) else None,
            "similar_weeks": int(len(similar)), "similar_up": float((similar["week_return"] > 0).mean()) if len(similar) else None,
            "similar_avg": float(similar["week_return"].mean()) if len(similar) else None}


def update_live(path, weeks, calls, now):
    """Score finished weeks in state/weekly.csv and add tonight's calls (once per day per stock)."""
    path = Path(path)
    log = pd.read_csv(path) if path.exists() and path.stat().st_size else pd.DataFrame(columns=COLUMNS)
    log["target_date"] = log["target_date"].astype(object)  # all blank until a week ends, which reads as float
    for i, row in log[log["outcome_up"].isna()].iterrows():
        f = weeks.get(row["ticker"])
        day = pd.Timestamp(row["feature_date"])
        if f is None or day not in f.index or pd.isna(f.at[day, "target_wk_up"]):
            continue
        log.loc[i, ["target_date", "week_return", "excess_return", "outcome_up", "outcome_beat"]] = [
            f.at[day, "target_date"].date().isoformat(), round(float(f.at[day, "week_return"]), 6),
            round(float(f.at[day, "excess_return"]), 6), f.at[day, "target_wk_up"], f.at[day, "target_wk_beat"]]
    have = set(zip(log["ticker"], log["feature_date"].astype(str)))
    new = [{"ticker": t, "feature_date": c["feature_date"], "p_up": round(c["p_up"], 5), "p_beat": round(c["p_beat"], 5),
            "source": c["source"], "made_at": now.isoformat(timespec="seconds")} for t, c in calls.items() if (t, c["feature_date"]) not in have]
    if new:
        log = pd.concat([log, pd.DataFrame(new, columns=COLUMNS)], ignore_index=True) if len(log) else pd.DataFrame(new, columns=COLUMNS)
    path.parent.mkdir(parents=True, exist_ok=True)
    log.sort_values(["feature_date", "ticker"]).to_csv(path, index=False, float_format="%.6g")
    return log


def live_record(log):
    done = log.dropna(subset=["outcome_up"])
    right = (done["p_up"] >= 0.5) == (done["outcome_up"] == 1)
    out = {"all": {"calls": int(len(done)), "right": int(right.sum())}}
    for t, g in done.groupby("ticker"):
        hits = (g["p_up"] >= 0.5) == (g["outcome_up"] == 1)
        out[t] = {"calls": int(len(g)), "right": int(hits.sum()),
                  "last": [{"date": str(d), "right": bool(h)} for d, h in zip(g["feature_date"].tail(10), hits.tail(10))]}
    return out


def run(frames, prices, market, state_dir, now, save=True):
    """Week-ahead odds for every stock in `frames`, the test behind them, and per-stock context.
    `save` logs tonight's calls to state/weekly.csv and scores finished weeks; without it the log is only read."""
    weeks = {t: week_frame(frames[t], prices[t], market) for t in frames}
    data = pooled(weeks)
    known_now = max(w.index[-1] for w in weeks.values()) + pd.Timedelta(days=1)
    record, calls = {}, {t: {"feature_date": w.index[-1].date().isoformat()} for t, w in weeks.items()}
    for question, (target, ret) in QUESTIONS.items():
        record[question] = score(walk_forward(data, target, ret))
        usual = usual_odds(data, target, known_now)
        fitted = fit_model(data, target, known_now)
        use_model = record[question]["champion"] == "model" and fitted is not None
        for t, w in weeks.items():
            p_model = float(model_odds(fitted, w.iloc[[-1]], usual)[0]) if fitted is not None else None
            calls[t][f"p_{question}"] = p_model if use_model else usual
            calls[t][f"model_{question}"] = p_model
            if question == "up":
                calls[t]["source"] = "model" if use_model else "usual odds"
    for t, c in calls.items():
        start = pd.Timestamp(c["feature_date"])
        c["week_from"] = (start + pd.offsets.BDay(1)).date().isoformat()
        c["week_to"] = (start + pd.offsets.BDay(HORIZON)).date().isoformat()
        c["context"] = context(weeks[t])
    path = Path(state_dir) / "weekly.csv"
    late = next_session_started(max(w.index[-1] for w in weeks.values()), now)
    if save:
        log = update_live(path, weeks, {} if late else calls, now)
    else:
        log = pd.read_csv(path) if path.exists() and path.stat().st_size else pd.DataFrame(columns=COLUMNS)
    return {"horizon": HORIZON, "calls": calls, "record": record, "live": live_record(log), "late": late}
