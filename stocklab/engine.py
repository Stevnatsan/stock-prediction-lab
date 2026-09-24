"""The learning loop. The same four steps run over history (to give each model experience) and
live every trading day:

    1. predict the next session using only what is known now
    2. wait until that session is over
    3. score the prediction against what actually happened
    4. learn from the outcome (bigger update when the prediction was confidently wrong)

A prediction is always recorded before the model sees the answer, so every accuracy number in
the reports is out-of-sample.
"""
import numpy as np
import pandas as pd

from .features import VARIANTS


def vector(row, variant):
    return np.array([row.get(f, np.nan) for f in VARIANTS[variant]], dtype=float)


def _to_json_list(x):
    return [float(v) if np.isfinite(v) else None for v in x]


def _from_json_list(values):
    return np.array([np.nan if v is None else v for v in values], dtype=float)


def replay(state, ticker, frame, source, now_iso, after=None):
    """Predict-then-learn over every row whose outcome is already known (optionally only after `after`)."""
    known = frame[frame["target_up"].notna()]
    if after is not None:
        known = known[known.index > after]
    for date, row in known.iterrows():
        y = int(row["target_up"])
        for variant in VARIANTS:
            model = state.model(variant, ticker)
            x = vector(row, variant)
            p = model.predict_proba(x)  # 1. predict with what was known that evening
            model.update(x, y)          # 4. then learn from the real outcome
            state.add_prediction(source=source, ticker=ticker, variant=variant, feature_date=date,
                                 target_date=row["target_date"], p_up=round(p, 5), outcome_up=y,
                                 correct=int((p >= 0.5) == bool(y)), persist_up=float(row["session_ret"] > 0),
                                 session_return=round(float(row["target_ret"]), 6), made_at=now_iso)
    return len(known)


def resolve_pending(state, ticker, frame, now_iso, give_up_days=10):
    """Score yesterday's live predictions now that the session is over, and learn from them."""
    remaining, resolved = [], 0
    last_date = frame.index[-1] if len(frame) else None
    for item in state.pending:
        if item["ticker"] != ticker:
            remaining.append(item)
            continue
        date = pd.Timestamp(item["feature_date"])
        if date in frame.index and pd.notna(frame.at[date, "target_up"]):
            row = frame.loc[date]
            y = int(row["target_up"])
            state.model(item["variant"], ticker).update(_from_json_list(item["x"]), y)  # learn from exactly what we saw
            state.add_prediction(source="live", ticker=ticker, variant=item["variant"], feature_date=date,
                                 target_date=row["target_date"], p_up=item["p_up"], outcome_up=y,
                                 correct=int((item["p_up"] >= 0.5) == bool(y)), persist_up=item["persist_up"],
                                 session_return=round(float(row["target_ret"]), 6), made_at=item["made_at"])
            resolved += 1
        elif last_date is not None and last_date - date > pd.Timedelta(days=give_up_days):
            continue  # the day vanished from the data (e.g. a revision); drop it rather than wait forever
        else:
            remaining.append(item)
    state.pending = remaining
    return resolved


def predict_latest(state, ticker, frame, news, now_iso):
    """Make tomorrow's prediction from today's close plus today's headlines. Returns P(up) per variant."""
    date = frame.index[-1]
    existing = {p["variant"]: p["p_up"] for p in state.pending
                if p["ticker"] == ticker and pd.Timestamp(p["feature_date"]) == date}
    if existing or pd.notna(frame.at[date, "target_up"]):
        return existing
    row = frame.loc[date].copy()
    for key, value in news.items():
        row[key] = value
    calls = {}
    for variant in VARIANTS:
        x = vector(row, variant)
        p = round(state.model(variant, ticker).predict_proba(x), 5)
        state.pending.append({"ticker": ticker, "variant": variant, "feature_date": date.date().isoformat(),
                              "p_up": p, "x": _to_json_list(x), "persist_up": float(row["session_ret"] > 0),
                              "made_at": now_iso, "headlines_24h": int(news.get("sent_count", 0)),
                              "sentiment_24h": None if pd.isna(news.get("sent_mean")) else round(news["sent_mean"], 3)})
        calls[variant] = p
    return calls
