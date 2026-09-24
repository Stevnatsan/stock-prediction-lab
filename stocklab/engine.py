"""The learning loop. The same four steps run over history (to give each model experience) and
live every trading day:

    1. predict the next session using only what is known now
    2. wait until that session is over
    3. score the prediction against what actually happened
    4. learn from the outcome (bigger update when the prediction was confidently wrong)

A prediction is always recorded before the model sees the answer, so every accuracy number in
the reports is out-of-sample.

Each model answers one question (see features.TASKS): "up" models are scored on whether the stock
rose, "beat_*" models on whether it beat the market. The prediction log uses the same columns for
both: for beat models, outcome_up means "beat SPY" and session_return is the stock's return minus SPY's.
"""
import numpy as np
import pandas as pd

from .features import ENSEMBLES, LEAD_MODEL, TASKS, VARIANTS, task_of


def vector(row, variant):
    return np.array([row.get(f, np.nan) for f in VARIANTS[variant]], dtype=float)


def _to_json_list(x):
    return [float(v) if np.isfinite(v) else None for v in x]


def _from_json_list(values):
    return np.array([np.nan if v is None else v for v in values], dtype=float)


def outcome(row, variant):
    """(outcome 0/1, or None while unknown; realised return; today's outcome, for the "same as today" baseline)."""
    target, ret, today = TASKS[task_of(variant)]
    y = row[target]
    return (None if pd.isna(y) else int(y)), row[ret], float(row[today] > 0)


def _record(state, source, ticker, variant, date, row, p, now_iso):
    y, ret, persist = outcome(row, variant)
    return state.add_prediction(source=source, ticker=ticker, variant=variant, feature_date=date,
                                target_date=row["target_date"], p_up=round(float(p), 5), outcome_up=y,
                                correct=int((p >= 0.5) == bool(y)), persist_up=persist,
                                session_return=round(float(ret), 6), made_at=now_iso)


def replay(state, ticker, frame, source, now_iso, after=None, variants=VARIANTS):
    """Predict-then-learn over every row whose outcome is already known (optionally only after `after`).
    Days already in the log (e.g. real live calls) are learned from but not recorded twice.
    Returns the number of sessions replayed."""
    sessions = 0
    for variant in variants:
        target = TASKS[task_of(variant)][0]
        known = frame[frame[target].notna()]
        if after is not None:
            known = known[known.index > after]
        model = state.model(variant, ticker)
        for date, row in known.iterrows():
            x = vector(row, variant)
            p = model.predict_proba(x)          # 1. predict with what was known that evening
            model.update(x, int(row[target]))   # 4. then learn from the real outcome
            _record(state, source, ticker, variant, date, row, p, now_iso)
        sessions = max(sessions, len(known))
    return sessions


def record_boosting(state, ticker, variant, frame, probabilities, source, now_iso):
    """Store walk-forward boosting predictions (already out-of-sample) for one stock."""
    return sum(_record(state, source, ticker, variant, date, frame.loc[date], p, now_iso) for date, p in probabilities.items())


def add_ensembles(state):
    """For every scored day that has both member predictions but no ensemble yet, record the ensemble:
    the average of the two probabilities."""
    state.flush()
    df = state.predictions
    keys = ["ticker", "feature_date"]
    added = 0
    for ensemble, (a, b) in ENSEMBLES.items():
        first = df[df["variant"] == a].set_index(keys)
        second = df[df["variant"] == b].set_index(keys)
        done = set(df.loc[df["variant"] == ensemble, keys].itertuples(index=False, name=None))
        for key in second.index.intersection(first.index):
            if key in done:
                continue
            g, f = second.loc[key], first.loc[key]
            p = (float(g["p_up"]) + float(f["p_up"])) / 2
            source = g["source"] if g["source"] == f["source"] else "catch-up"
            added += state.add_prediction(**{**g.to_dict(), "ticker": key[0], "feature_date": key[1], "variant": ensemble,
                                             "source": source, "p_up": round(p, 5),
                                             "correct": int((p >= 0.5) == bool(g["outcome_up"]))})
    return added


def resolve_pending(state, ticker, frame, now_iso, give_up_days=10):
    """Score yesterday's live predictions now that the session is over, and learn from them."""
    remaining, resolved = [], 0
    last_date = frame.index[-1] if len(frame) else None
    for item in state.pending:
        if item["ticker"] != ticker:
            remaining.append(item)
            continue
        date = pd.Timestamp(item["feature_date"])
        variant = item["variant"]
        y = None
        if date in frame.index:
            row = frame.loc[date]
            y, ret, _ = outcome(row, variant)
        if y is not None:
            model = state.models.get((variant, ticker))
            x = item.get("x")
            if variant in VARIANTS and model is not None and x is not None and len(x) == len(model.features):
                model.update(_from_json_list(x), y)  # learn from exactly what we saw (boosting is refit instead)
            state.add_prediction(source="live", ticker=ticker, variant=variant, feature_date=date,
                                 target_date=row["target_date"], p_up=item["p_up"], outcome_up=y,
                                 correct=int((item["p_up"] >= 0.5) == bool(y)), persist_up=item["persist_up"],
                                 session_return=round(float(ret), 6), made_at=item["made_at"])
            resolved += 1
        elif last_date is not None and last_date - date > pd.Timedelta(days=give_up_days):
            continue  # the day vanished from the data (e.g. a revision); drop it rather than wait forever
        else:
            remaining.append(item)
    state.pending = remaining
    return resolved


def pending_for(state, ticker, date):
    return {p["variant"]: p["p_up"] for p in state.pending if p["ticker"] == ticker and pd.Timestamp(p["feature_date"]) == date}


def _rounded(value):
    return None if value is None or pd.isna(value) else round(float(value), 3)


def predict_latest(state, ticker, frame, live, now_iso):
    """Tonight's logistic predictions for the next session, from today's close plus everything collected
    tonight (`live`). Returns P(yes) per model made so far for this day."""
    date = frame.index[-1]
    calls = pending_for(state, ticker, date)
    if pd.notna(frame.at[date, "target_up"]):
        return calls
    row = frame.loc[date].copy()
    for key, value in live.items():
        row[key] = value
    for variant in VARIANTS:
        if variant in calls:
            continue
        x = vector(row, variant)
        p = round(state.model(variant, ticker).predict_proba(x), 5)
        state.pending.append({"ticker": ticker, "variant": variant, "feature_date": date.date().isoformat(),
                              "p_up": p, "x": _to_json_list(x), "persist_up": outcome(row, variant)[2],
                              "made_at": now_iso, "close": round(float(row["close"]), 4),
                              "headlines_24h": int(live.get("sent_count", 0)),
                              "sentiment_24h": _rounded(live.get("sent_mean")),
                              "finbert_24h": _rounded(live.get("finbert_mean"))})
        calls[variant] = p
    return calls


def add_pending(state, ticker, date, variant, p):
    """Queue a boosting or ensemble prediction next to the same day's pending logistic call."""
    lead = LEAD_MODEL[task_of(variant)]
    like = next(x for x in state.pending if x["ticker"] == ticker and x["variant"] == lead
                and x["feature_date"] == date.date().isoformat())
    state.pending.append({**like, "variant": variant, "p_up": round(float(p), 5), "x": None})
