"""The week-ahead question: buy at the next open and hold for a week (5 sessions). Will the stock be
higher at that week's last close, and will it beat the market (SPY) over the same week?

One gradient-boosting model per question, pooled across all stocks, retrained from scratch every run.
On top of the daily features it gets longer-term momentum (3 and 6 months, distance from the 200-day
average), which matters more over a week than over a single session. Its track record is measured
walk-forward: each month of history is predicted by a model trained only on weeks that had already
finished before that month began, so no call ever saw its own answer.

Live calls go to state/weekly.csv and are scored once their week is over.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from . import boosting
from .features import HISTORICAL

HORIZON = 5  # sessions
LONG_FEATURES = ["ret_60", "ret_120", "dist_sma200"]
FEATURES = HISTORICAL + LONG_FEATURES
QUESTIONS = {"up": "target_wk_up", "beat": "target_wk_beat"}
CONFIDENT = 0.05  # a call at least 5 points from 50%
COLUMNS = ["ticker", "feature_date", "p_up", "p_beat", "target_date", "week_return", "excess_return", "outcome_up", "outcome_beat", "made_at"]


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
    market_week = m_close.shift(-HORIZON) / m_open.shift(-1) - 1
    f["week_return"] = week
    f["excess_return"] = week - market_week
    f["target_wk_up"] = (week > 0).astype(float).where(week.notna())
    f["target_wk_beat"] = (f["excess_return"] > 0).astype(float).where(f["excess_return"].notna())
    f["target_date"] = pd.Series(frame.index, index=frame.index).shift(-HORIZON)
    return f


def _accuracy(p, y):
    return float(((p >= 0.5) == (y == 1)).mean()) if len(y) else None


def track_record(frames, probabilities, question):
    """How the walk-forward calls did, per stock and overall, against always guessing yes."""
    target = QUESTIONS[question]
    ret_col = "week_return" if question == "up" else "excess_return"
    rows = []
    for ticker, p in probabilities.items():
        f = frames[ticker].loc[p.index]
        rows.append(pd.DataFrame({"ticker": ticker, "p": p.to_numpy(), "y": f[target].to_numpy(), "ret": f[ret_col].to_numpy()}, index=p.index))
    data = pd.concat(rows) if rows else pd.DataFrame(columns=["ticker", "p", "y", "ret"])

    def summary(d):
        sure = d[(d["p"] - 0.5).abs() >= CONFIDENT]
        leaned_up = d[d["p"] >= 0.5 + CONFIDENT]
        return {"calls": int(len(d)), "accuracy": _accuracy(d["p"], d["y"]), "always_yes": float(d["y"].mean()) if len(d) else None,
                "confident_calls": int(len(sure)), "confident_accuracy": _accuracy(sure["p"], sure["y"]),
                "avg_week": float(d["ret"].mean()) if len(d) else None,
                "avg_week_when_leaning_up": float(leaned_up["ret"].mean()) if len(leaned_up) else None,
                "from": d.index.min().date().isoformat() if len(d) else None}

    return {"all": summary(data), **{t: summary(g) for t, g in data.groupby("ticker")}}


def update_live(path, frames, calls, now):
    """Score finished weeks in state/weekly.csv and add tonight's calls (once per day per stock)."""
    path = Path(path)
    log = pd.read_csv(path) if path.exists() and path.stat().st_size else pd.DataFrame(columns=COLUMNS)
    log["target_date"] = log["target_date"].astype(object)  # all blank until a week ends, which reads as float
    for i, row in log[log["outcome_up"].isna()].iterrows():
        f = frames.get(row["ticker"])
        day = pd.Timestamp(row["feature_date"])
        if f is None or day not in f.index or pd.isna(f.at[day, "target_wk_up"]):
            continue
        log.loc[i, ["target_date", "week_return", "excess_return", "outcome_up", "outcome_beat"]] = [
            f.at[day, "target_date"].date().isoformat(), round(float(f.at[day, "week_return"]), 6),
            round(float(f.at[day, "excess_return"]), 6), f.at[day, "target_wk_up"], f.at[day, "target_wk_beat"]]
    have = set(zip(log["ticker"], log["feature_date"].astype(str)))
    new = [{"ticker": t, "feature_date": c["feature_date"], "p_up": round(c["p_up"], 5), "p_beat": round(c["p_beat"], 5),
            "made_at": now.isoformat(timespec="seconds")} for t, c in calls.items() if (t, c["feature_date"]) not in have]
    if new:
        log = pd.concat([log, pd.DataFrame(new, columns=COLUMNS)], ignore_index=True) if len(log) else pd.DataFrame(new, columns=COLUMNS)
    path.parent.mkdir(parents=True, exist_ok=True)
    log.sort_values(["feature_date", "ticker"]).to_csv(path, index=False, float_format="%.6g")
    return log


def live_record(log):
    done = log.dropna(subset=["outcome_up"])
    out = {"all": {"calls": int(len(done)), "right": int(((done["p_up"] >= 0.5) == (done["outcome_up"] == 1)).sum())}}
    for t, g in done.groupby("ticker"):
        out[t] = {"calls": int(len(g)), "right": int(((g["p_up"] >= 0.5) == (g["outcome_up"] == 1)).sum()),
                  "last": [{"date": str(r.feature_date), "right": bool((r.p_up >= 0.5) == (r.outcome_up == 1))} for r in g.tail(10).itertuples()]}
    return out


def run(frames, prices, market, state_dir, now, save=True):
    """Week-ahead calls for every stock in `frames`, with their walk-forward track record. `save` logs
    tonight's calls to state/weekly.csv and scores finished weeks; without it the log is only read."""
    weeks = {t: week_frame(frames[t], prices[t], market) for t in frames}
    calls, record = {}, {}
    for question, target in QUESTIONS.items():
        record[question] = track_record(weeks, boosting.walk_forward(weeks, {t: None for t in weeks}, FEATURES, target), question)
        for ticker, p in boosting.predict_latest(weeks, list(weeks), FEATURES, target).items():
            calls.setdefault(ticker, {"feature_date": weeks[ticker].index[-1].date().isoformat()})[f"p_{question}"] = float(p)
    calls = {t: c for t, c in calls.items() if "p_up" in c and "p_beat" in c}
    for ticker, c in calls.items():
        start = pd.Timestamp(c["feature_date"])
        c["week_from"] = (start + pd.offsets.BDay(1)).date().isoformat()
        c["week_to"] = (start + pd.offsets.BDay(HORIZON)).date().isoformat()
    path = Path(state_dir) / "weekly.csv"
    if save:
        log = update_live(path, weeks, calls, now)
    else:
        log = pd.read_csv(path) if path.exists() and path.stat().st_size else pd.DataFrame(columns=COLUMNS)
    return {"horizon": HORIZON, "calls": calls, "record": record, "live": live_record(log)}
