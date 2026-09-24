"""Turn the prediction log into reports/latest.md, two charts, and the README scoreboard."""
import math
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

START, END = "<!-- scoreboard:start -->", "<!-- scoreboard:end -->"
BG, FG, MUTED, GRID, ACCENT, WARN = "#14120f", "#f5f1e6", "#9a958a", "#2e2b25", "#d7ff3f", "#ff7a59"
MODEL_NAMES = {"full": "Logistic, price + news", "price": "Logistic, price only", "gbm": "Gradient boosting",
               "ensemble": "Ensemble"}
MODEL_ORDER = list(MODEL_NAMES)
COLOURS = {"full": ACCENT, "price": FG, "gbm": "#6fc3ff", "ensemble": "#c792ea"}
CHAMPION_WINDOW = 120  # sessions
TOP_K = 3


def champion(resolved):
    """The model with the best accuracy over the most recent CHAMPION_WINDOW sessions."""
    if resolved.empty:
        return "full", {}
    recent_days = sorted(resolved["feature_date"].unique())[-CHAMPION_WINDOW:]
    recent = resolved[resolved["feature_date"].isin(recent_days)]
    scores = recent.groupby("variant")["correct"].mean().to_dict()
    best = max(MODEL_ORDER, key=lambda m: scores.get(m, -1))
    return best, scores


def _group(source):
    return "Live" if source == "live" else "Historical replay"


def accuracy_rows(resolved):
    rows = []
    for (group, variant), g in resolved.groupby([resolved["source"].map(_group), "variant"]):
        n = len(g)
        acc = g["correct"].mean()
        ci = 1.96 * math.sqrt(acc * (1 - acc) / n) if n else float("nan")
        always_up = g["outcome_up"].mean()
        persistence = (g["persist_up"] == g["outcome_up"]).mean()
        best = max(always_up, 1 - always_up, persistence)
        if acc - ci > best:
            verdict = "yes"
        elif acc > best:
            verdict = "within noise"
        else:
            verdict = "no"
        rows.append({"group": group, "variant": variant, "n": n, "accuracy": acc, "ci": ci, "always_up": always_up,
                     "persistence": persistence, "brier": ((g["p_up"] - g["outcome_up"]) ** 2).mean(), "beats": verdict})
    rank = {m: i for i, m in enumerate(MODEL_ORDER)}
    return sorted(rows, key=lambda r: (r["group"] != "Live", rank.get(r["variant"], 9)))


def top_k_returns(resolved, cost_bps, threshold, k=TOP_K):
    """Quant-style daily portfolio per model: each session split the money equally between the (up to)
    k stocks it rates most likely to rise, skipping any below `threshold`; bought at the open, sold at
    the close. Days with no pick stay in cash. Returns {model: daily return Series}."""
    cost = cost_bps / 1e4
    out = {}
    for variant in [m for m in MODEL_ORDER if m in set(resolved["variant"])]:
        g = resolved[resolved["variant"] == variant]
        days = pd.Index(sorted(g["feature_date"].unique()))
        picks = g[g["p_up"] >= threshold].sort_values("p_up", ascending=False).groupby("feature_date").head(k)
        out[variant] = (picks["session_return"] - cost).groupby(picks["feature_date"]).mean().reindex(days, fill_value=0.0)
    base = resolved[resolved["variant"] == "full"]
    out["all"] = (base["session_return"] - cost).groupby(base["feature_date"]).mean()
    return out


def strategy_rows(resolved, cost_bps, threshold):
    rows = []
    for variant, daily in top_k_returns(resolved, cost_bps, threshold).items():
        if daily.empty:
            continue
        total = (1 + daily).prod() - 1
        years = max(len(daily) / 252, 1e-9)
        sharpe = daily.mean() / daily.std() * 252 ** 0.5 if daily.std() > 0 else float("nan")
        rows.append({"variant": variant, "days": len(daily), "total": total,
                     "annual": (1 + total) ** (1 / years) - 1, "sharpe": sharpe, "win": (daily > 0).mean()})
    return rows


def _style(ax):
    ax.set_facecolor(BG)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED)
    ax.grid(color=GRID, lw=0.8)
    ax.set_axisbelow(True)


def _shade_live(ax, resolved):
    live = resolved.loc[resolved["source"] == "live", "feature_date"]
    if len(live):
        ax.axvspan(live.min(), resolved["feature_date"].max(), color=ACCENT, alpha=0.07, lw=0)
        ax.text(live.min(), ax.get_ylim()[1], "  live", color=ACCENT, va="top", fontsize=10)


def charts(resolved, threshold, cost_bps, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 4.6), facecolor=BG)
    _style(ax)
    for variant in MODEL_ORDER:
        g = resolved[resolved["variant"] == variant]
        if g.empty:
            continue
        daily = g.groupby("feature_date")["correct"].mean().rolling(60, min_periods=60).mean()
        ax.plot(daily.index, daily.values, color=COLOURS[variant], lw=1.6, label=MODEL_NAMES[variant])
    up = resolved[resolved["variant"] == "full"].groupby("feature_date")["outcome_up"].mean().rolling(60, min_periods=60).mean()
    ax.plot(up.index, up.values, color=MUTED, lw=1, ls="--", label="Always predict up")
    ax.axhline(0.5, color=WARN, lw=1, alpha=0.7)
    ax.set_title("Rolling 60-session accuracy (all stocks pooled)", color=FG, loc="left", fontsize=13, fontweight="bold")
    ax.legend(frameon=False, labelcolor=FG, loc="upper left", bbox_to_anchor=(0, -0.08), ncol=3)
    _shade_live(ax, resolved)
    fig.savefig(out_dir / "rolling_accuracy.png", dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.6), facecolor=BG)
    _style(ax)
    for variant, daily in top_k_returns(resolved, cost_bps, threshold).items():
        curve = (1 + daily).cumprod()
        name = "Buy every stock, every session" if variant == "all" else MODEL_NAMES[variant]
        ax.plot(curve.index, curve.values, color=MUTED if variant == "all" else COLOURS[variant], lw=1.4,
                ls="--" if variant == "all" else "-", label=name)
    ax.axhline(1.0, color=GRID, lw=1)
    ax.set_title(f"Paper trading: each model's top {TOP_K} picks with P(up) ≥ {threshold:.0%} (growth of $1, {cost_bps:g} bp cost)",
                 color=FG, loc="left", fontsize=13, fontweight="bold")
    ax.legend(frameon=False, labelcolor=FG, loc="upper left", bbox_to_anchor=(0, -0.08), ncol=3)
    _shade_live(ax, resolved)
    fig.savefig(out_dir / "paper_trading.png", dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def _pct(x):
    return "–" if pd.isna(x) else f"{x:.1%}"


def calls_table(state, threshold, best):
    by_ticker = {}
    for p in state.pending:
        by_ticker.setdefault(p["ticker"], {})[p["variant"]] = p
    ranked = sorted(by_ticker, key=lambda t: -(by_ticker[t].get(best) or by_ticker[t].get("full", {})).get("p_up", 0))
    lines = [f"| Rank | Stock | P(up), {MODEL_NAMES[best].lower()} (champion) | Call | Logistic | Boosting | Ensemble | Headlines (24 h) | News mood |",
             "|---|---|---|---|---|---|---|---|---|"]
    for rank, ticker in enumerate(ranked, 1):
        v = by_ticker[ticker]
        full = v.get("full", {})
        p = (v.get(best) or full).get("p_up")
        call = "–" if p is None else ("**Buy at open**" if rank <= TOP_K and p >= threshold else "Stay out")
        mood = full.get("sentiment_24h")
        mood_txt = "–" if mood is None else ("positive" if mood > 0.05 else "negative" if mood < -0.05 else "neutral") + f" ({mood:+.2f})"
        lines.append(f"| {rank} | {ticker} | **{_pct(p)}** | {call} | {_pct(full.get('p_up'))} | {_pct(v.get('gbm', {}).get('p_up'))} | "
                     f"{_pct(v.get('ensemble', {}).get('p_up'))} | {full.get('headlines_24h', 0)} | {mood_txt} |")
    as_of = max((p["feature_date"] for p in state.pending), default=None)
    if not by_ticker:
        lines = ["No open calls right now. New ones are made after each US market close."]
    return lines, as_of


def accuracy_table(rows):
    lines = ["| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['group']}, {MODEL_NAMES[r['variant']].lower()} | {r['n']:,} | **{r['accuracy']:.1%}** | "
                     f"{r['accuracy'] - r['ci']:.1%}–{r['accuracy'] + r['ci']:.1%} | {r['always_up']:.1%} | "
                     f"{r['persistence']:.1%} | {r['beats']} |")
    return lines


def per_stock_table(resolved):
    live = resolved[resolved["source"] == "live"]
    use = live if live.groupby("ticker").size().min(skipna=True) >= 20 else resolved
    label = "live" if use is live else "all resolved (mostly historical replay)"
    lines = [f"Based on {label} predictions.", "",
             "| Stock | Sessions | " + " | ".join(MODEL_NAMES.values()) + " | Always up |", "|---|---|" + "---|" * (len(MODEL_NAMES) + 1)]
    for ticker, g in use.groupby("ticker"):
        full = g[g["variant"] == "full"]
        accs = " | ".join(_pct(g.loc[g["variant"] == m, "correct"].mean()) for m in MODEL_NAMES)
        lines.append(f"| {ticker} | {len(full):,} | {accs} | {_pct(full['outcome_up'].mean())} |")
    return lines


def model_table(scores, best):
    lines = [f"| Model | Accuracy, last {CHAMPION_WINDOW} sessions |", "|---|---|"]
    for m in sorted(scores, key=lambda m: -scores[m]):
        lines.append(f"| {'**' + MODEL_NAMES[m] + ' (champion)**' if m == best else MODEL_NAMES[m]} | {scores[m]:.1%} |")
    return lines


def strategy_table(rows):
    lines = ["| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |", "|---|---|---|---|---|---|"]
    for r in rows:
        name = "Buy every stock, every session" if r["variant"] == "all" else f"Top {TOP_K} by {MODEL_NAMES[r['variant']].lower()}"
        lines.append(f"| {name} | {r['days']:,} | {r['total']:+.1%} | {r['annual']:+.1%} | {r['sharpe']:.2f} | {r['win']:.1%} |")
    return lines


def health_table(health):
    lines = ["| Source | Calls ok | Failed | Items | Note |", "|---|---|---|---|---|"]
    for name, h in sorted(health.items()):
        lines.append(f"| {name} | {h['ok']} | {h['failed']} | {h['items']} | {h['last_error'] or ''} |")
    return lines


def build_report(state, config, reports_dir, readme_path, now, health, summary):
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    state.flush()
    resolved = state.predictions.dropna(subset=["outcome_up"]).copy()
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    best, scores = champion(resolved)
    calls, as_of = calls_table(state, config.decision_threshold, best)

    board = [f"**Updated:** {stamp}" + (f" · predictions made after the close of {as_of}" if as_of else ""), ""]
    board += ["### Next-session calls", "", "Will each stock close above its opening price in the next session? "
              f"Calls use the **champion**: whichever of the four models was most accurate over the last {CHAMPION_WINDOW} sessions "
              f"(now: {MODEL_NAMES[best].lower()}). **Buy at open** marks the (up to) {TOP_K} highest-rated stocks with "
              f"P(up) ≥ {config.decision_threshold:.0%}: the paper-trading strategy.", ""] + calls + [""]
    if len(resolved):
        rows = accuracy_rows(resolved)
        charts(resolved, config.decision_threshold, config.cost_bps, reports_dir)
        board += ["### Which model is winning?", ""] + model_table(scores, best) + ["", "### How accurate has it been?", ""] + accuracy_table(rows) + [
            "", "Any model has to beat three simple rules: always predict up (*Always up* is the share of sessions that rose), "
                "always predict down, and predict the same direction as today (*Same as today*). "
                "*Beats baselines* is only \"yes\" when the whole 95% range is above all three.", "",
            "![Rolling accuracy](reports/rolling_accuracy.png)", "",
            "Full report, with per-stock results, paper trading and source health: [reports/latest.md](reports/latest.md)"]
    else:
        board += ["Accuracy appears here after the first predictions have been scored."]

    if readme_path and Path(readme_path).exists():
        text = Path(readme_path).read_text()
        if START in text and END in text:
            text = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + "\n".join(board) + "\n" + END, text, flags=re.S)
            Path(readme_path).write_text(text)

    report = [f"# Stock prediction lab: latest report", "", f"Generated {stamp}.", "", "## Next-session calls", ""] + calls
    if len(resolved):
        report += ["", "## Accuracy", ""] + accuracy_table(accuracy_rows(resolved))
        report += ["", "![Rolling accuracy](rolling_accuracy.png)", "", "## Per stock", ""] + per_stock_table(resolved)
        report += ["", "## Paper trading", "", f"Hypothetical only: no real orders are placed. Each session a strategy buys, at the open, "
                   f"the (up to) {TOP_K} stocks its model rates most likely to rise with P(up) ≥ {config.decision_threshold:.0%}, "
                   "and sells them at the close.", ""] + strategy_table(strategy_rows(resolved, config.cost_bps, config.decision_threshold))
        report += ["", "![Paper trading](paper_trading.png)"]
    report += ["", "## Data sources this run", ""] + health_table(health)
    report += ["", "## This run, per stock", "", "| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |",
               "|---|---|---|---|---|---|"]
    for ticker, info in summary.items():
        report.append(f"| {ticker} | {info.get('status')} | {info.get('data_through', '–')} | {info.get('history_replayed', 0)} | "
                      f"{info.get('scored', 0)} | {info.get('headlines_24h', 0)} |")
    report += ["", "---", "", "Educational project. Not financial advice."]
    (reports_dir / "latest.md").write_text("\n".join(report) + "\n")
