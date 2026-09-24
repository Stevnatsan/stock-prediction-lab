"""Turn the prediction log into reports/latest.md, three charts, and the README scoreboard."""
import math
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from .features import ALL_MODELS, LEAD_MODEL, task_of  # noqa: E402
from .strategy import CHAMPION_WINDOW, TOP_K, champion, models_of, ranked_calls, top_k_returns, top_picks  # noqa: E402

START, END = "<!-- scoreboard:start -->", "<!-- scoreboard:end -->"
BG, FG, MUTED, GRID, ACCENT, WARN = "#14120f", "#f5f1e6", "#9a958a", "#2e2b25", "#d7ff3f", "#ff7a59"
BASE_NAMES = {"full": "Logistic, all sources (VADER)", "finbert": "Logistic, all sources (FinBERT)",
              "price": "Logistic, price only", "gbm": "Gradient boosting", "ensemble": "Ensemble"}
COLOURS = {"full": ACCENT, "finbert": "#ffb86b", "price": FG, "gbm": "#6fc3ff", "ensemble": "#c792ea"}
QUESTIONS = {"up": "Up or down?", "beat": "Beats the market?"}
YES = {"up": "up", "beat": "beats SPY"}
BINS = [0, 0.40, 0.45, 0.48, 0.50, 0.52, 0.55, 0.60, 1.0001]
BIN_LABELS = ["under 40%", "40–45%", "45–48%", "48–50%", "50–52%", "52–55%", "55–60%", "60% or more"]
MIN_LIVE_FOR_CALIBRATION = 300

# kept for older imports
MODEL_NAMES = BASE_NAMES


def base(variant):
    return variant.removeprefix("beat_")


def name(variant):
    return BASE_NAMES[base(variant)]


def lname(variant):
    """The name mid-sentence: "logistic, all sources (VADER)"."""
    n = name(variant)
    return n[0].lower() + n[1:]


def _pct(x):
    return "–" if x is None or pd.isna(x) else f"{x:.1%}"


def _group(source):
    return "Live" if source == "live" else "Historical replay"


def _cost(task, cost_bps):
    return cost_bps / 1e4 * (2 if task == "beat" else 1)  # beat trades also short SPY: two trades


# ---------- numbers ----------
def accuracy_rows(resolved):
    rows = []
    for (group, variant), g in resolved.groupby([resolved["source"].map(_group), "variant"]):
        n = len(g)
        acc = g["correct"].mean()
        ci = 1.96 * math.sqrt(acc * (1 - acc) / n) if n else float("nan")
        always_yes = g["outcome_up"].mean()
        persistence = (g["persist_up"] == g["outcome_up"]).mean()
        best = max(always_yes, 1 - always_yes, persistence)
        verdict = "yes" if acc - ci > best else "within noise" if acc > best else "no"
        rows.append({"group": group, "variant": variant, "task": task_of(variant), "n": n, "accuracy": acc, "ci": ci,
                     "always_up": always_yes, "persistence": persistence,
                     "brier": ((g["p_up"] - g["outcome_up"]) ** 2).mean(), "beats": verdict})
    rank = {m: i for i, m in enumerate(ALL_MODELS)}
    return sorted(rows, key=lambda r: (r["group"] != "Live", rank.get(r["variant"], 99)))


def calibration(g):
    """Group predictions by how confident they were, and compare with how often the answer was yes."""
    bins = pd.cut(g["p_up"], BINS, right=False, labels=BIN_LABELS)
    t = g.groupby(bins, observed=True).agg(n=("p_up", "size"), predicted=("p_up", "mean"), actual=("outcome_up", "mean"))
    t = t[t["n"] > 0]
    error = float((t["n"] * (t["predicted"] - t["actual"]).abs()).sum() / t["n"].sum()) if len(t) else float("nan")
    return t, error


def calibration_sample(resolved, variant):
    g = resolved[resolved["variant"] == variant]
    live = g[g["source"] == "live"]
    return (live, "live") if len(live) >= MIN_LIVE_FOR_CALIBRATION else (g, "all scored")


def strategy_rows(resolved, cost_bps, threshold, task="up"):
    rows = []
    daily_by_model = top_k_returns(resolved, _cost(task, cost_bps), threshold, models_of(task))
    for variant, daily in daily_by_model.items():
        if daily.empty:
            continue
        total = (1 + daily).prod() - 1
        years = max(len(daily) / 252, 1e-9)
        sharpe = daily.mean() / daily.std() * 252 ** 0.5 if daily.std() > 0 else float("nan")
        rows.append({"variant": variant, "days": len(daily), "total": total,
                     "annual": (1 + total) ** (1 / years) - 1, "sharpe": sharpe, "win": (daily > 0).mean()})
    return rows


# ---------- charts ----------
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


def _two_panels(title):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8.4), facecolor=BG, sharex=False)
    fig.suptitle(title, color=FG, x=0.02, ha="left", fontsize=13, fontweight="bold")
    for ax in axes:
        _style(ax)
    return fig, axes


def _finish(fig, axes, path):
    for ax in axes:
        if ax.get_legend_handles_labels()[0]:
            ax.legend(frameon=False, labelcolor=FG, loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def charts(resolved, threshold, cost_bps, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = _two_panels("Rolling 60-session accuracy (all stocks pooled)")
    for ax, task in zip(axes, QUESTIONS):
        for variant in models_of(task):
            g = resolved[resolved["variant"] == variant]
            if g.empty:
                continue
            daily = g.groupby("feature_date")["correct"].mean().rolling(60, min_periods=60).mean()
            ax.plot(daily.index, daily.values, color=COLOURS[base(variant)], lw=1.4, label=name(variant))
        lead = resolved[resolved["variant"] == LEAD_MODEL[task]]
        yes = lead.groupby("feature_date")["outcome_up"].mean().rolling(60, min_periods=60).mean()
        ax.plot(yes.index, yes.values, color=MUTED, lw=1, ls="--", label=f"Always predict {YES[task]}")
        ax.axhline(0.5, color=WARN, lw=1, alpha=0.7)
        ax.set_title(QUESTIONS[task], color=FG, loc="left", fontsize=11)
        _shade_live(ax, resolved)
    _finish(fig, axes, out_dir / "rolling_accuracy.png")

    fig, axes = _two_panels(f"Paper trading: each model's top {TOP_K} picks with P ≥ {threshold:.0%} (growth of $1, after costs)")
    for ax, task in zip(axes, QUESTIONS):
        for variant, daily in top_k_returns(resolved, _cost(task, cost_bps), threshold, models_of(task)).items():
            curve = (1 + daily).cumprod()
            label = ("Buy every stock" if task == "up" else "Every stock, minus SPY") if variant == "all" else name(variant)
            ax.plot(curve.index, curve.values, color=MUTED if variant == "all" else COLOURS[base(variant)], lw=1.3,
                    ls="--" if variant == "all" else "-", label=label)
        ax.axhline(1.0, color=GRID, lw=1)
        ax.set_title("Up or down: buy at the open, sell at the close" if task == "up"
                     else "Beats the market: buy the picks and short SPY (market-neutral)", color=FG, loc="left", fontsize=11)
        _shade_live(ax, resolved)
    _finish(fig, axes, out_dir / "paper_trading.png")

    fig, axes = plt.subplots(1, 2, figsize=(11, 5), facecolor=BG)
    fig.suptitle("Calibration: when a model says X%, does it happen X% of the time?", color=FG, x=0.02, ha="left",
                 fontsize=13, fontweight="bold")
    for ax, task in zip(axes, QUESTIONS):
        _style(ax)
        lo, hi = 0.40, 0.62
        ax.plot([lo, hi], [lo, hi], color=MUTED, lw=1, ls="--", label="Perfectly honest")
        for variant in models_of(task):
            g, _ = calibration_sample(resolved, variant)
            if g.empty:
                continue
            t, _ = calibration(g)
            ax.plot(t["predicted"], t["actual"], marker="o", ms=4, color=COLOURS[base(variant)], lw=1.3, label=name(variant))
        ax.set_xlim(lo - 0.02, hi + 0.02)
        ax.set_ylim(lo - 0.08, hi + 0.08)
        ax.set_xlabel("Predicted probability", color=MUTED)
        ax.set_ylabel(f"Share that {'went up' if task == 'up' else 'beat SPY'}", color=MUTED)
        ax.set_title(QUESTIONS[task], color=FG, loc="left", fontsize=11)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, labelcolor=FG, loc="lower center", ncol=3, fontsize=9, bbox_to_anchor=(0.5, -0.08))
    fig.tight_layout()
    fig.savefig(out_dir / "calibration.png", dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


# ---------- tables ----------
def _latest_pending(state):
    as_of = max((p["feature_date"] for p in state.pending), default=None)
    return [p for p in state.pending if p["feature_date"] == as_of], as_of


def _mood(value):
    if value is None:
        return "–"
    return ("positive" if value > 0.05 else "negative" if value < -0.05 else "neutral") + f" ({value:+.2f})"


def calls_table(state, threshold, best):
    """`best`: {task: champion}."""
    pending, as_of = _latest_pending(state)
    if not pending:
        return ["No open calls right now. New ones are made after each US market close."], None
    up = ranked_calls(pending, best["up"], "up")
    beat = {c["ticker"]: c["p_up"] for c in ranked_calls(pending, best["beat"], "beat")}
    buy = {c["ticker"] for c in top_picks(pending, best["up"], threshold, "up")}
    outperform = {c["ticker"] for c in top_picks(pending, best["beat"], threshold, "beat")}
    lines = ["| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |",
             "|---|---|---|---|---|---|---|---|---|"]
    for rank, c in enumerate(up, 1):
        t = c["ticker"]
        lines.append(f"| {rank} | {t} | **{_pct(c['p_up'])}** | {'**Buy at open**' if t in buy else 'Stay out'} | "
                     f"{_pct(beat.get(t))} | {'**Outperform**' if t in outperform else '–'} | {c.get('headlines_24h', 0)} | "
                     f"{_mood(c.get('sentiment_24h'))} | {_mood(c.get('finbert_24h'))} |")
    return lines, as_of


def model_breakdown_table(state):
    pending, _ = _latest_pending(state)
    models = [m for m in ALL_MODELS if any(p["variant"] == m for p in pending)]
    if not models:
        return []
    by_ticker = {}
    for p in pending:
        by_ticker.setdefault(p["ticker"], {})[p["variant"]] = p["p_up"]
    header = " | ".join(f"{'P(beats SPY)' if task_of(m) == 'beat' else 'P(up)'}: {lname(m)}" for m in models)
    lines = [f"| Stock | {header} |", "|---|" + "---|" * len(models)]
    for ticker in sorted(by_ticker):
        lines.append(f"| {ticker} | " + " | ".join(_pct(by_ticker[ticker].get(m)) for m in models) + " |")
    return lines


def winners_table(scores, best):
    lines = [f"| Model | {QUESTIONS['up']} | {QUESTIONS['beat']} |", "|---|---|---|"]
    for m in BASE_NAMES:
        cells = []
        for task in QUESTIONS:
            variant = m if task == "up" else f"beat_{m}"
            s = scores[task].get(variant)
            cell = "–" if s is None else f"{s:.1%}"
            cells.append(f"**{cell} (champion)**" if best[task] == variant and s is not None else cell)
        lines.append(f"| {BASE_NAMES[m]} | " + " | ".join(cells) + " |")
    return lines


def accuracy_table(rows, task, brier=False):
    yes = "Always up" if task == "up" else "Always beats"
    lines = [f"| | Predictions | Accuracy | 95% range | {yes} | Same as today | Beats baselines? |" + (" Brier |" if brier else ""),
             "|---|---|---|---|---|---|---|" + ("---|" if brier else "")]
    for r in rows:
        if r["task"] != task:
            continue
        lines.append(f"| {r['group']}, {lname(r['variant'])} | {r['n']:,} | **{r['accuracy']:.1%}** | "
                     f"{r['accuracy'] - r['ci']:.1%}–{r['accuracy'] + r['ci']:.1%} | {r['always_up']:.1%} | "
                     f"{r['persistence']:.1%} | {r['beats']} |" + (f" {r['brier']:.4f} |" if brier else ""))
    return lines


def calibration_table(resolved, variant):
    g, sample = calibration_sample(resolved, variant)
    if g.empty:
        return [], float("nan"), sample
    t, error = calibration(g)
    what = "went up" if task_of(variant) == "up" else "beat SPY"
    lines = [f"| Predicted | Calls | Average prediction | Actually {what} | Verdict |", "|---|---|---|---|---|"]
    for label, r in t.iterrows():
        ci = 1.96 * math.sqrt(max(r["predicted"] * (1 - r["predicted"]), 1e-9) / r["n"])
        gap = r["actual"] - r["predicted"]
        verdict = "honest" if abs(gap) <= ci else ("happened more often than predicted" if gap > 0 else "happened less often than predicted")
        lines.append(f"| {label} | {int(r['n']):,} | {r['predicted']:.1%} | **{r['actual']:.1%}** | {verdict} |")
    return lines, error, sample


def calibration_matrix(resolved, task):
    """Every model of one question side by side: share that happened, per confidence bin."""
    models = [m for m in models_of(task) if (resolved["variant"] == m).any()]
    if not models:
        return []
    results = {m: calibration(calibration_sample(resolved, m)[0]) for m in models}
    lines = ["| Predicted | " + " | ".join(name(m) for m in models) + " |", "|---|" + "---|" * len(models)]
    for label in BIN_LABELS:
        cells = []
        for m in models:
            t = results[m][0]
            cells.append(f"{t.at[label, 'actual']:.1%} (n={int(t.at[label, 'n']):,})" if label in t.index else "–")
        if any(c != "–" for c in cells):
            lines.append(f"| {label} | " + " | ".join(cells) + " |")
    lines.append("| **Average gap** | " + " | ".join(f"**{results[m][1] * 100:.1f} pts**" for m in models) + " |")
    return lines


def sentiment_section(state, resolved):
    live = state.live
    lines = []
    if live.empty:
        return ["Both scorers read every headline from the first live run on; results appear here once those calls are scored."]
    outcomes = resolved.loc[resolved["variant"] == "full", ["ticker", "feature_date", "outcome_up", "session_return"]]
    joined = live.merge(outcomes, on=["ticker", "feature_date"])
    lines += ["| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | "
              "negative mood | Rank correlation with return |", "|---|---|---|---|---|---|"]
    for label, col in (("VADER", "sent_mean"), ("FinBERT", "finbert_mean")):
        s = joined[joined[col].abs() >= 0.05] if col in joined else joined.iloc[0:0]
        if s.empty:
            lines.append(f"| {label} | 0 | – | – | – | – |")
            continue
        hit = ((s[col] > 0) == (s["outcome_up"] == 1)).mean()
        pos, neg = s.loc[s[col] > 0, "session_return"].mean(), s.loc[s[col] < 0, "session_return"].mean()
        corr = s[col].corr(s["session_return"], method="spearman") if len(s) > 2 else float("nan")
        lines.append(f"| {label} | {len(s):,} | {_pct(hit)} | {_pct(pos) if not pd.isna(pos) else '–'} | "
                     f"{_pct(neg) if not pd.isna(neg) else '–'} | {'–' if pd.isna(corr) else f'{corr:+.3f}'} |")
    both = live.dropna(subset=["sent_mean", "finbert_mean"])
    if len(both):
        agree = (np.sign(both["sent_mean"].round(2)) == np.sign(both["finbert_mean"].round(2))).mean()
        lines += ["", f"The two scorers agree on the direction of the mood on {agree:.0%} of {len(both):,} stock-days with headlines."]
    return lines


def per_stock_table(resolved, task="up"):
    models = models_of(task)
    use_all = resolved[resolved["variant"].isin(models)]
    live = use_all[use_all["source"] == "live"]
    counts = live.groupby("ticker").size()
    use = live if len(counts) and counts.min() >= 20 * len(models) else use_all
    label = "live" if use is live else "all scored (mostly historical replay)"
    present = [m for m in models if (use["variant"] == m).any()]
    yes = "Always up" if task == "up" else "Always beats"
    lines = [f"Based on {label} predictions.", "",
             "| Stock | Sessions | " + " | ".join(name(m) for m in present) + f" | {yes} |", "|---|---|" + "---|" * (len(present) + 1)]
    for ticker, g in use.groupby("ticker"):
        lead = g[g["variant"] == present[0]]
        accs = " | ".join(_pct(g.loc[g["variant"] == m, "correct"].mean()) for m in present)
        lines.append(f"| {ticker} | {len(lead):,} | {accs} | {_pct(lead['outcome_up'].mean())} |")
    return lines


def strategy_table(rows, task):
    lines = ["| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |", "|---|---|---|---|---|---|"]
    for r in rows:
        if r["variant"] == "all":
            label = "Buy every stock, every session" if task == "up" else "Every stock minus SPY"
        else:
            label = f"Top {TOP_K} by {lname(r['variant'])}"
        lines.append(f"| {label} | {r['days']:,} | {r['total']:+.1%} | {r['annual']:+.1%} | {r['sharpe']:.2f} | {r['win']:.1%} |")
    return lines


def orders_section(state_root, resolved):
    path = Path(state_root) / "orders.csv"
    if not path.exists() or not path.stat().st_size:
        return ["No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are "
                "sent as real simulated orders every session."]
    orders = pd.read_csv(path)
    done = orders.dropna(subset=["trade_return"])
    lines = []
    if len(done):
        assumed = resolved[resolved["variant"] == "full"].assign(session=lambda d: d["target_date"].dt.strftime("%Y-%m-%d"))
        done = done.merge(assumed[["ticker", "session", "session_return"]], on=["ticker", "session"], how="left")
        pnl = (done["qty"] * (done["sell_price"] - done["buy_price"])).sum()
        slippage = (done["trade_return"] - done["session_return"]).mean()
        lines += [f"**{len(done)} round trips, profit/loss ${pnl:+,.2f}**, average {done['trade_return'].mean():+.2%} per trade. "
                  f"Real fills vs. the open → close prices the backtest assumes: {slippage:+.3%} per trade on average.", ""]
    lines += ["| Session | Stock | Shares | Bought at | Sold at | Return | Status |", "|---|---|---|---|---|---|---|"]
    for _, r in orders.sort_values(["session", "ticker"], ascending=[False, True]).head(20).iterrows():
        money = lambda v: "–" if pd.isna(v) else f"${v:,.2f}"  # noqa: E731
        lines.append(f"| {r['session']} | {r['ticker']} | {int(r['qty']) if pd.notna(r['qty']) else 0} | {money(r['buy_price'])} | "
                     f"{money(r['sell_price'])} | {_pct(r['trade_return'])} | {r['buy_status']} / {r['sell_status'] if pd.notna(r['sell_status']) else '–'} |")
    return lines


def health_table(health):
    lines = ["| Source | Calls ok | Failed | Items | Note |", "|---|---|---|---|---|"]
    for source, h in sorted(health.items()):
        lines.append(f"| {source} | {h['ok']} | {h['failed']} | {h['items']} | {h['last_error'] or ''} |")
    return lines


# ---------- assembly ----------
def build_report(state, config, reports_dir, readme_path, now, health, summary, notes=()):
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    state.flush()
    resolved = state.predictions.dropna(subset=["outcome_up"]).copy()
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    best, scores = {}, {}
    for task in QUESTIONS:
        best[task], scores[task] = champion(resolved, task)
    calls, as_of = calls_table(state, config.decision_threshold, best)
    t = config.decision_threshold

    board = [f"**Updated:** {stamp}" + (f" · predictions made after the close of {as_of}" if as_of else ""), ""]
    board += ["### Next-session calls", "",
              "Two questions for every stock: will it close above its opening price, and will it beat the market (SPY) over the "
              f"same session? Each is answered by its **champion**, the model most accurate over the last {CHAMPION_WINDOW} sessions "
              f"(now: {lname(best['up'])} and {lname(best['beat'])}). **Buy at open** marks the (up to) {TOP_K} "
              f"highest-rated stocks with P(up) ≥ {t:.0%}: the paper-trading strategy, sent to Alpaca when connected. "
              f"**Outperform** marks the top {TOP_K} with P(beats SPY) ≥ {t:.0%}.", ""] + calls + [""]
    if len(resolved):
        rows = accuracy_rows(resolved)
        charts(resolved, t, config.cost_bps, reports_dir)
        cal_lines, cal_error, cal_sample = calibration_table(resolved, best["up"])
        board += ["### Which model is winning?", "", f"Accuracy over the last {CHAMPION_WINDOW} sessions.", ""] + winners_table(scores, best)
        for task in QUESTIONS:
            board += ["", f"### How accurate has it been? {QUESTIONS[task]}", ""] + accuracy_table(rows, task)
        board += ["", "Any model has to beat simple rules: always say yes (*Always up* / *Always beats* is how often the answer was yes), "
                  "always say no, or repeat today's answer (*Same as today*). *Beats baselines* is only \"yes\" when the whole 95% "
                  "range is above all of them.", "",
                  "### Are the probabilities honest?", "",
                  f"When the champion ({lname(best['up'])}) says a stock has a given chance of rising, how often does it? "
                  f"Based on {cal_sample} predictions; on average its probabilities are off by **{cal_error * 100:.1f} percentage points**.", ""]
        board += cal_lines + ["", "![Rolling accuracy](reports/rolling_accuracy.png)", "",
                              "Full report, with calibration of every model, VADER vs FinBERT, paper trading, real Alpaca fills and "
                              "source health: [reports/latest.md](reports/latest.md)"]
    else:
        board += ["Accuracy appears here after the first predictions have been scored."]

    if readme_path and Path(readme_path).exists():
        text = Path(readme_path).read_text()
        if START in text and END in text:
            text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: START + "\n" + "\n".join(board) + "\n" + END, text, flags=re.S)
            Path(readme_path).write_text(text)

    report = ["# Stock prediction lab: latest report", "", f"Generated {stamp}.", ""]
    report += [f"> {n}" for n in notes] + ([""] if notes else [])
    report += ["## Next-session calls", ""] + calls
    breakdown = model_breakdown_table(state)
    if breakdown:
        report += ["", "Every model's probability:", ""] + breakdown
    if len(resolved):
        rows = accuracy_rows(resolved)
        for task in QUESTIONS:
            report += ["", f"## Accuracy: {QUESTIONS[task].lower()}", ""] + accuracy_table(rows, task, brier=True)
        report += ["", "*Brier* is the mean squared error of the probabilities (lower is better; always saying 50% scores 0.25).",
                   "", "![Rolling accuracy](rolling_accuracy.png)", "", "## Calibration", "",
                   "Predictions grouped by confidence. For an honest model, the share that happened matches the prediction: of all the "
                   "\"55–60%\" calls, about 57% should come true. *Average gap* is the weighted average distance between the two "
                   f"(expected calibration error). Uses live predictions once a model has {MIN_LIVE_FOR_CALIBRATION}, before that all "
                   "scored ones.", ""]
        for task in QUESTIONS:
            report += [f"**{QUESTIONS[task]}**", ""] + calibration_matrix(resolved, task) + [""]
        report += ["![Calibration](calibration.png)", "", "## Headline sentiment: VADER vs FinBERT", "",
                   "Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical "
                   "logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood "
                   "predict the next session?", ""] + sentiment_section(state, resolved)
        for task in QUESTIONS:
            report += ["", f"## Per stock: {QUESTIONS[task].lower()}", ""] + per_stock_table(resolved, task)
        report += ["", "## Paper trading (simulated from prices)", "",
                   f"Hypothetical: each session a strategy buys, at the open, the (up to) {TOP_K} stocks its model rates highest with "
                   f"P ≥ {t:.0%}, and sells them at the close, paying {config.cost_bps:g} bp per trade. The *beats the market* version "
                   "also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).",
                   "", "**Up or down**", ""] + strategy_table(strategy_rows(resolved, config.cost_bps, t, "up"), "up")
        report += ["", "**Beats the market (market-neutral)**", ""] + strategy_table(strategy_rows(resolved, config.cost_bps, t, "beat"), "beat")
        report += ["", "![Paper trading](paper_trading.png)"]
    report += ["", "## Paper orders at Alpaca (real fills)", ""] + orders_section(state.root, resolved)
    report += ["", "## Data sources this run", ""] + health_table(health)
    report += ["", "## This run, per stock", "", "| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |",
               "|---|---|---|---|---|---|"]
    for ticker, info in summary.items():
        report.append(f"| {ticker} | {info.get('status')} | {info.get('data_through', '–')} | {info.get('history_replayed', 0)} | "
                      f"{info.get('scored', 0)} | {info.get('headlines_24h', 0)} |")
    report += ["", "---", "", "Educational project. Not financial advice."]
    (reports_dir / "latest.md").write_text("\n".join(report) + "\n")
