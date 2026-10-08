"""A plain-language market brief for each stock: where the price stands, how it compares with the
market, how jumpy it is, what the news mood is, and what the models think of the next session (with
how much that is worth). Written to reports/insight.md for people and reports/insight.json for tools.

Everything here is description, not a forecast: the trend and risk numbers say what has happened,
and the model section says how often the models have been right on that stock.
"""
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from .strategy import CHAMPION_WINDOW, champion, ranked_calls

TRADING_DAYS = 252
PERIODS = {"1 week": 5, "1 month": 21, "3 months": 63, "1 year": TRADING_DAYS}


def _ret(close, days):
    return float(close.iloc[-1] / close.iloc[-1 - days] - 1) if len(close) > days else None


def _ytd(close):
    last_year = close[close.index.year < close.index[-1].year]
    return float(close.iloc[-1] / last_year.iloc[-1] - 1) if len(last_year) else None


def _rsi(close, window=14):
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / window, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / window, adjust=False).mean()
    return float(100 - 100 / (1 + gain.iloc[-1] / loss.iloc[-1])) if loss.iloc[-1] else 100.0


def price_stats(prices, market=None):
    """Descriptive numbers from daily bars (needs about a year of history for all of them)."""
    close = prices["close"].dropna()
    daily = close.pct_change().dropna()
    year = close.iloc[-TRADING_DAYS:]
    stats = {
        "as_of": close.index[-1].date().isoformat(),
        "close": round(float(close.iloc[-1]), 2),
        "returns": {name: _ret(close, days) for name, days in PERIODS.items()},
        "ytd": _ytd(close),
        "high_1y": round(float(year.max()), 2),
        "low_1y": round(float(year.min()), 2),
        "off_high": float(close.iloc[-1] / year.max() - 1),
        "sma50": float(close.iloc[-50:].mean()) if len(close) >= 50 else None,
        "sma200": float(close.iloc[-200:].mean()) if len(close) >= 200 else None,
        "rsi_14": _rsi(close),
        "vol_now": float(daily.iloc[-20:].std() * math.sqrt(TRADING_DAYS)),
        "vol_1y": float(daily.iloc[-TRADING_DAYS:].std() * math.sqrt(TRADING_DAYS)),
        "typical_day": float(daily.iloc[-60:].abs().median()),
        "up_days_1y": float((daily.iloc[-TRADING_DAYS:] > 0).mean()),
    }
    if market is not None:
        mclose = market["close"].dropna()
        stats["vs_market"] = {}
        for name in ("3 months", "1 year"):
            mine, theirs = stats["returns"][name], _ret(mclose, PERIODS[name])
            stats["vs_market"][name] = mine - theirs if mine is not None and theirs is not None else None
        both = pd.concat([daily, mclose.pct_change()], axis=1, join="inner").dropna().iloc[-TRADING_DAYS:]
        stats["beta"] = float(np.cov(both.iloc[:, 0], both.iloc[:, 1])[0, 1] / both.iloc[:, 1].var()) if len(both) > 60 else None
    return stats


def model_stats(state, ticker):
    """Tonight's champion calls for `ticker` and how the models have done on it."""
    resolved = state.predictions.dropna(subset=["outcome_up"])
    out = {}
    for task in ("up", "beat"):
        best, _ = champion(resolved, task)
        call = next((c for c in ranked_calls(state.pending, best, task) if c["ticker"] == ticker), None)
        rows = resolved[(resolved["ticker"] == ticker) & (resolved["variant"] == best)]
        recent = rows[rows["feature_date"].isin(sorted(rows["feature_date"].unique())[-CHAMPION_WINDOW:])]
        live = rows[rows["source"] == "live"]
        out[task] = {
            "model": best,
            "p": call["p_up"] if call else None,
            "for_session_after": call["feature_date"] if call else None,
            "accuracy_recent": float(recent["correct"].mean()) if len(recent) else None,
            "recent_sessions": int(len(recent)),
            "accuracy_live": float(live["correct"].mean()) if len(live) else None,
            "live_sessions": int(len(live)),
            "base_rate": float(rows["outcome_up"].mean()) if len(rows) else None,
            "last_calls": [{"date": pd.Timestamp(r.feature_date).date().isoformat(), "p": float(r.p_up), "right": bool(r.correct)}
                           for r in live.sort_values("feature_date").tail(10).itertuples()],
        }
    return out


def _names(ticker):
    """Words a headline about `ticker` would contain: the symbol and the company's first name word."""
    names = {ticker.lower()}
    catalogue = Path(__file__).resolve().parents[1] / "catalogue" / "sp500.csv"
    if catalogue.exists():
        rows = pd.read_csv(catalogue)
        for name in rows.loc[rows["symbol"] == ticker, "name"]:
            names.add(str(name).split()[0].strip(",.").lower())
    return names


def news_stats(state_root, ticker, now, days=7, top=3):
    path = Path(state_root) / "news" / f"{ticker}.jsonl"
    items = [json.loads(line) for line in path.read_text().splitlines() if line] if path.exists() else []
    cutoff = pd.Timestamp(now) - pd.Timedelta(days=days)
    recent = [h for h in items if pd.Timestamp(h["published"]) >= cutoff]
    scores = [h["finbert"] if h.get("finbert") is not None else h.get("score", 0.0) for h in recent]
    recent.sort(key=lambda h: h["published"], reverse=True)
    names = _names(ticker)
    about = [h for h in recent if any(n in h["title"].lower() for n in names)] or recent
    loudest = sorted(about[:40], key=lambda h: -abs(h.get("finbert") if h.get("finbert") is not None else h.get("score", 0.0)))
    return {"count_7d": len(recent), "mood_7d": float(np.mean(scores)) if scores else None,
            "headlines": [{"title": h["title"], "published": h["published"][:10]} for h in loudest[:top]]}


# ---------- words ----------
def _pct(x, signed=True):
    return "n/a" if x is None else (f"{x:+.1%}" if signed else f"{x:.1%}")


def _trend(s):
    close, s50, s200 = s["close"], s.get("sma50"), s.get("sma200")
    if s50 is None or s200 is None:
        return "Not enough history to judge the trend."
    if close > s50 > s200:
        return "Uptrend: the price is above its 50-day and 200-day averages, and the shorter one is above the longer one."
    if close < s50 < s200:
        return "Downtrend: the price is below its 50-day and 200-day averages, and the shorter one is below the longer one."
    if close > s200:
        return "Long-term uptrend, but the last couple of months have been mixed (the price and its 50-day average disagree)."
    return "Long-term trend is down (below the 200-day average), with some recent recovery."


def _heat(s):
    rsi = s["rsi_14"]
    if rsi >= 70:
        return f"Stretched: RSI {rsi:.0f} (above 70 often means it ran up fast and may pause)."
    if rsi <= 30:
        return f"Beaten down: RSI {rsi:.0f} (below 30 often means it sold off fast and may bounce)."
    return f"Neither overbought nor oversold (RSI {rsi:.0f}, normal range 30 to 70)."


def _risk(s):
    ratio = s["vol_now"] / s["vol_1y"] if s["vol_1y"] else 1
    mood = "calmer than" if ratio < 0.8 else "choppier than" if ratio > 1.25 else "about as jumpy as"
    return (f"A typical day moves it about {s['typical_day']:.1%}. Lately it is {mood} its usual year "
            f"({s['vol_now']:.0%} vs {s['vol_1y']:.0%} annualised volatility).")


def _model_line(m):
    up = m["up"]
    if up["p"] is None:
        return "No call from the models for the next session."
    acc = up["accuracy_recent"]
    lean = "rise" if up["p"] >= 0.5 else "fall"
    worth = ("which is no better than a coin flip" if acc is None or acc < 0.53
             else "a small but real edge" if acc < 0.56 else "a meaningful edge, if it lasts")
    return (f"The models give {up['p']:.0%} odds the next session closes above its open (a slight lean to {lean}). "
            f"On this stock they were right {_pct(acc, False)} of the time over the last {up['recent_sessions']} sessions, {worth}.")


def describe(ticker, s, m, n):
    lines = [_trend(s), _heat(s), _risk(s)]
    vs = (s.get("vs_market") or {}).get("1 year")
    if vs is not None:
        lines.append(f"Over the past year it {'beat' if vs >= 0 else 'lagged'} the S&P 500 (SPY) by {abs(vs) * 100:.0f} percentage points.")
    if s["off_high"] < -0.1:
        lines.append(f"It sits {abs(s['off_high']):.0%} below its 1-year high of ${s['high_1y']:,.2f}.")
    else:
        lines.append(f"It is close to its 1-year high of ${s['high_1y']:,.2f} ({_pct(s['off_high'])}).")
    if n and n["mood_7d"] is not None:
        tone = "positive" if n["mood_7d"] > 0.05 else "negative" if n["mood_7d"] < -0.05 else "mixed"
        lines.append(f"News mood over the last week: {tone} ({n['count_7d']} headlines).")
    if m:
        lines.append(_model_line(m))
    return lines


def build(prices, market, state, now, tickers=None):
    """The insight for every stock in `prices` (or just `tickers`), as a JSON-ready dict."""
    out = {"generated": pd.Timestamp(now).isoformat(timespec="seconds"), "market": None, "stocks": {}}
    if market is not None:
        out["market"] = price_stats(market)
        out["market"]["summary"] = [_trend(out["market"]), _risk(out["market"])]
    for ticker in tickers or list(prices):
        if prices.get(ticker) is None or len(prices[ticker]) < 60:
            continue
        s = price_stats(prices[ticker], market)
        m = model_stats(state, ticker) if state is not None else None
        n = news_stats(state.root, ticker, now) if state is not None else None
        out["stocks"][ticker] = {**s, "models": m, "news": n, "summary": describe(ticker, s, m, n)}
    return out


def to_markdown(insight):
    lines = ["# Market insight", "", f"Generated {insight['generated'][:16].replace('T', ' ')} UTC. "
             "Plain-language snapshot of each stock. Describes what has happened; it is not a forecast or advice.", ""]
    mk = insight.get("market")
    if mk:
        lines += [f"## The market (SPY) · ${mk['close']:,.2f} on {mk['as_of']}", ""] + [f"- {x}" for x in mk["summary"]]
        lines += [f"- Last month {_pct(mk['returns']['1 month'])}, this year {_pct(mk['ytd'])}, past year {_pct(mk['returns']['1 year'])}.", ""]
    lines += ["| Stock | Price | 1 week | 1 month | 3 months | This year | 1 year | vs SPY (1 y) | Off 1-y high | P(up) next session |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for t, s in insight["stocks"].items():
        r, p = s["returns"], ((s.get("models") or {}).get("up") or {}).get("p")
        lines.append(f"| {t} | ${s['close']:,.2f} | {_pct(r['1 week'])} | {_pct(r['1 month'])} | {_pct(r['3 months'])} | "
                     f"{_pct(s['ytd'])} | {_pct(r['1 year'])} | {_pct((s.get('vs_market') or {}).get('1 year'))} | "
                     f"{_pct(s['off_high'])} | {'–' if p is None else f'{p:.0%}'} |")
    for t, s in insight["stocks"].items():
        lines += ["", f"## {t} · ${s['close']:,.2f} on {s['as_of']}", ""] + [f"- {x}" for x in s["summary"]]
        heads = (s.get("news") or {}).get("headlines") or []
        if heads:
            lines += ["", "Headlines with the strongest tone this week:", ""] + [f"- {h['published']}: {h['title']}" for h in heads]
    return "\n".join(lines) + "\n"


def write(insight, reports_dir):
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "insight.json").write_text(json.dumps(insight, indent=1, default=str))
    (reports_dir / "insight.md").write_text(to_markdown(insight))
