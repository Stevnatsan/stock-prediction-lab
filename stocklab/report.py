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
VARIANT_NAMES = {"full": "Price + news", "price": "Price only"}


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
    order = {("Live", "full"): 0, ("Live", "price"): 1, ("Historical replay", "full"): 2, ("Historical replay", "price"): 3}
    return sorted(rows, key=lambda r: order.get((r["group"], r["variant"]), 9))


def paper_trading(resolved, threshold, cost_bps):
    """Equal-weight daily portfolio: buy at the open, sell at the close when P(up) >= threshold."""
    cost = cost_bps / 1e4
    curves = {}
    for variant, g in resolved.groupby("variant"):
        traded = (g["p_up"] >= threshold).astype(float)
        daily = (traded * (g["session_return"] - cost)).groupby(g["feature_date"]).mean()
        curves[VARIANT_NAMES.get(variant, variant)] = (1 + daily).cumprod()
    base = resolved[resolved["variant"] == "full"]
    curves["Buy every session"] = (1 + (base["session_return"] - cost).groupby(base["feature_date"]).mean()).cumprod()
    return curves


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
    for variant, colour in (("full", ACCENT), ("price", FG)):
        g = resolved[resolved["variant"] == variant]
        daily = g.groupby("feature_date")["correct"].mean().rolling(60, min_periods=60).mean()
        ax.plot(daily.index, daily.values, color=colour, lw=2 if variant == "full" else 1.2, label=VARIANT_NAMES[variant])
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
    colours = {"Price + news": ACCENT, "Price only": FG, "Buy every session": MUTED}
    for name, curve in paper_trading(resolved, threshold, cost_bps).items():
        ax.plot(curve.index, curve.values, color=colours.get(name, FG), lw=2 if name == "Price + news" else 1.2,
                ls="--" if name == "Buy every session" else "-", label=name)
    ax.axhline(1.0, color=GRID, lw=1)
    ax.set_title(f"Paper trading, growth of $1 (trades when P(up) ≥ {threshold:.2f}, {cost_bps:g} bp cost)",
                 color=FG, loc="left", fontsize=13, fontweight="bold")
    ax.legend(frameon=False, labelcolor=FG, loc="upper left", bbox_to_anchor=(0, -0.08), ncol=3)
    _shade_live(ax, resolved)
    fig.savefig(out_dir / "paper_trading.png", dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def _pct(x):
    return "–" if pd.isna(x) else f"{x:.1%}"


def calls_table(state, threshold):
    by_ticker = {}
    for p in state.pending:
        by_ticker.setdefault(p["ticker"], {})[p["variant"]] = p
    lines = ["| Stock | P(up), price + news | P(up), price only | Call | Headlines (24 h) | News mood |",
             "|---|---|---|---|---|---|"]
    for ticker, v in sorted(by_ticker.items()):
        full, price = v.get("full", {}), v.get("price", {})
        p = full.get("p_up")
        call = "–" if p is None else ("**Buy at open**" if p >= threshold else "Stay out")
        mood = full.get("sentiment_24h")
        mood_txt = "–" if mood is None else ("positive" if mood > 0.05 else "negative" if mood < -0.05 else "neutral") + f" ({mood:+.2f})"
        lines.append(f"| {ticker} | {_pct(p)} | {_pct(price.get('p_up'))} | {call} | {full.get('headlines_24h', 0)} | {mood_txt} |")
    as_of = max((p["feature_date"] for p in state.pending), default=None)
    return lines, as_of


def accuracy_table(rows):
    lines = ["| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['group']}, {VARIANT_NAMES[r['variant']].lower()} | {r['n']:,} | **{r['accuracy']:.1%}** | "
                     f"{r['accuracy'] - r['ci']:.1%}–{r['accuracy'] + r['ci']:.1%} | {r['always_up']:.1%} | "
                     f"{r['persistence']:.1%} | {r['beats']} |")
    return lines


def per_stock_table(resolved):
    live = resolved[resolved["source"] == "live"]
    use = live if live.groupby("ticker").size().min(skipna=True) >= 20 else resolved
    label = "live" if use is live else "all resolved (mostly historical replay)"
    lines = [f"Based on {label} predictions.", "",
             "| Stock | Predictions | Price + news | Price only | Always up |", "|---|---|---|---|---|"]
    for ticker, g in use.groupby("ticker"):
        full, price = g[g["variant"] == "full"], g[g["variant"] == "price"]
        lines.append(f"| {ticker} | {len(full):,} | {_pct(full['correct'].mean())} | {_pct(price['correct'].mean())} | "
                     f"{_pct(full['outcome_up'].mean())} |")
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
    calls, as_of = calls_table(state, config.decision_threshold)

    board = [f"**Last run:** {stamp}" + (f" · predictions made after the close of {as_of}" if as_of else ""), ""]
    board += ["### Next-session calls", "", "Will each stock close above its opening price in the next session?", ""] + calls + [""]
    if len(resolved):
        rows = accuracy_rows(resolved)
        charts(resolved, config.decision_threshold, config.cost_bps, reports_dir)
        board += ["### How accurate has it been?", ""] + accuracy_table(rows) + [
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
        report += ["", "## Paper trading", "", "Hypothetical only: no real orders are placed.", "",
                   "![Paper trading](paper_trading.png)"]
    report += ["", "## Data sources this run", ""] + health_table(health)
    report += ["", "## This run, per stock", "", "| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |",
               "|---|---|---|---|---|---|"]
    for ticker, info in summary.items():
        report.append(f"| {ticker} | {info.get('status')} | {info.get('data_through', '–')} | {info.get('history_replayed', 0)} | "
                      f"{info.get('scored', 0)} | {info.get('headlines_24h', 0)} |")
    report += ["", "---", "", "Educational project. Not financial advice."]
    (reports_dir / "latest.md").write_text("\n".join(report) + "\n")
