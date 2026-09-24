"""Which model to trust, which stocks to pick, and how that would have paid: shared by the report
and the Alpaca paper orders so both always agree."""
import pandas as pd

from .features import ALL_MODELS, LEAD_MODEL, task_of

CHAMPION_WINDOW = 120  # sessions
TOP_K = 3


def models_of(task):
    return [m for m in ALL_MODELS if task_of(m) == task]


def champion(resolved, task="up"):
    """The model with the best accuracy over the most recent CHAMPION_WINDOW sessions."""
    candidates = models_of(task)
    rows = resolved[resolved["variant"].isin(candidates)] if len(resolved) else resolved
    if rows.empty:
        return LEAD_MODEL[task], {}
    recent_days = sorted(rows["feature_date"].unique())[-CHAMPION_WINDOW:]
    scores = rows[rows["feature_date"].isin(recent_days)].groupby("variant")["correct"].mean().to_dict()
    return max(candidates, key=lambda m: scores.get(m, -1)), scores


def ranked_calls(pending, model, task="up"):
    """Tonight's pending calls, best first, using `model` (or the task's lead model where it has none)."""
    by_ticker = {}
    for p in pending:
        by_ticker.setdefault(p["ticker"], {})[p["variant"]] = p
    calls = [v.get(model) or v.get(LEAD_MODEL[task]) for v in by_ticker.values()]
    return sorted([c for c in calls if c], key=lambda c: -c["p_up"])


def top_picks(pending, model, threshold, task="up", k=TOP_K):
    return [c for c in ranked_calls(pending, model, task)[:k] if c["p_up"] >= threshold]


def top_k_returns(resolved, cost, threshold, models, k=TOP_K):
    """Quant-style daily portfolio per model: each session split the money equally between the (up to)
    k stocks it rates highest, skipping any below `threshold`. Days with no pick stay in cash.
    `cost` is per trade, as a fraction. Returns {model: daily return Series, "all": every stock}."""
    out = {}
    for variant in [m for m in models if m in set(resolved["variant"])]:
        g = resolved[resolved["variant"] == variant]
        days = pd.Index(sorted(g["feature_date"].unique()))
        picks = g[g["p_up"] >= threshold].sort_values("p_up", ascending=False).groupby("feature_date").head(k)
        out[variant] = (picks["session_return"] - cost).groupby(picks["feature_date"]).mean().reindex(days, fill_value=0.0)
    if out:
        base = resolved[resolved["variant"] == next(iter(out))]
        out["all"] = (base["session_return"] - cost).groupby(base["feature_date"]).mean()
    return out
