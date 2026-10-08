"""docs/index.html: one phone-friendly page with tonight's calls and the plain-language insight,
rewritten by every daily run. Turn on GitHub Pages (Settings -> Pages -> Deploy from a branch ->
main, /docs) and it lives at https://<user>.github.io/<repo>/, ready to add to a phone's home screen.
"""
import html
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from .config import ROOT
from .sources.prices import NEW_YORK, SESSION_OPEN
from .strategy import CHAMPION_WINDOW, champion

LEAN = 0.02  # a call more than 2 points from 50% counts as a lean
REPO_URL = "https://github.com/" + os.environ.get("GITHUB_REPOSITORY", "Stevnatsan/stock-prediction-lab")


def company_names():
    path = ROOT / "catalogue" / "sp500.csv"
    if not path.exists():
        return {}
    rows = pd.read_csv(path)
    return {s: str(n).split(" (")[0].replace(", Inc.", "").replace(" Inc.", "").replace(" Corporation", "") for s, n in zip(rows["symbol"], rows["name"])}


def next_session(after):
    """The next weekday after `after` (market holidays aside) and its 9:30 and 16:00 New York times."""
    day = pd.Timestamp(after) + pd.offsets.BDay(1)
    opens = datetime.combine(day.date(), SESSION_OPEN, NEW_YORK)
    return day.date(), opens, opens + timedelta(hours=6, minutes=30)


def _too_late(opens, text):
    """A notice the page shows (in the reader's browser) once `opens` has passed: the calls are for a
    session that has already started, and acting on them now would not be the call that was tested."""
    return f'<p class="stale" data-after="{opens.isoformat()}" hidden>{text}</p>'


def lean(p):
    if p is None:
        return "none", "No call"
    if p >= 0.5 + LEAN:
        return "up", "Leans up"
    if p <= 0.5 - LEAN:
        return "down", "Leans down"
    return "flat", "No clear lean"


def overall_record(state):
    resolved = state.predictions.dropna(subset=["outcome_up"])
    best, scores = champion(resolved, "up")
    rows = resolved[resolved["variant"] == best]
    days = sorted(rows["feature_date"].unique())[-CHAMPION_WINDOW:]
    recent = rows[rows["feature_date"].isin(days)]
    live = rows[rows["source"] == "live"]
    return {"accuracy": scores.get(best), "always_up": float(recent["outcome_up"].mean()) if len(recent) else None,
            "live_right": int(live["correct"].sum()), "live_total": int(len(live))}


# ---------- html ----------
def _e(x):
    return html.escape(str(x))


def _pct(x, signed=True, digits=1):
    if x is None:
        return "–"
    return f"{x:+.{digits}%}" if signed else f"{x:.{digits}%}"


def _day(d, long=False):
    d = pd.Timestamp(d)
    return f"{d:%A} {d.day} {d:%b}" if long else f"{d:%a} {d.day} {d:%b}"


def _sign(x):
    return "" if x is None else ("pos" if x >= 0 else "neg")


def _card(ticker, s, name, open_details=True):
    up = (s.get("models") or {}).get("up") or {}
    beat = (s.get("models") or {}).get("beat") or {}
    kind, label = lean(up.get("p"))
    r = s["returns"]
    span = s["high_1y"] - s["low_1y"]
    where = 100 * (s["close"] - s["low_1y"]) / span if span else 50
    acc = up.get("accuracy_recent")
    trust = ("It has had no real edge on this stock lately, so treat the call as a coin flip."
             if acc is None or acc < 0.53 else "It has had a small edge on this stock lately.")
    dots = "".join(f'<i class="dot {"hit" if c["right"] else "miss"}" title="{_e(c["date"])}: {"right" if c["right"] else "wrong"}"></i>'
                   for c in up.get("last_calls") or [])
    stats = [("1 month", r.get("1 month")), ("This year", s.get("ytd")), ("1 year", r.get("1 year")),
             ("vs S&amp;P, 1 year", (s.get("vs_market") or {}).get("1 year"))]
    facts = [x for x in s.get("summary", []) if not x.startswith("The models give")]
    heads = (s.get("news") or {}).get("headlines") or []
    return f"""
<article class="card" id="{_e(ticker.lower())}">
  <div class="top"><h3>{_e(name)} <span class="tick">{_e(ticker)}</span></h3><span class="price">${s['close']:,.2f}</span></div>
  <div class="call {kind}">
    <span class="chip">{label}</span>
    <span><b>{_pct(up.get('p'), False, 0)}</b> chance it closes above its open · <b>{_pct(beat.get('p'), False, 0)}</b> it beats the market</span>
  </div>
  <div class="stats">{''.join(f'<div><span class="label">{k}</span><span class="num {_sign(v)}">{_pct(v)}</span></div>' for k, v in stats)}</div>
  <div class="range"><span class="label">Where it sits in its 1-year range</span>
    <div class="bar"><i style="left:{max(0, min(100, where)):.0f}%"></i></div>
    <div class="ends"><span>${s['low_1y']:,.2f}</span><span>${s['high_1y']:,.2f}</span></div></div>
  <details{' open' if open_details else ''}><summary>What's going on</summary>
    <ul>{''.join(f'<li>{_e(x)}</li>' for x in facts)}</ul>
    {'<p class="label">Headlines this week</p><ul class="heads">' + ''.join(f'<li>{_e(h["title"])}</li>' for h in heads) + '</ul>' if heads else ''}
  </details>
  <div class="record"><span class="label">Last {len(up.get('last_calls') or [])} calls on {_e(ticker)}</span><span class="dots">{dots or '–'}</span>
    <p class="small">Right {_pct(acc, False)} of the last {up.get('recent_sessions', 0)} sessions. {trust}</p></div>
</article>"""



def _week_card(ticker, s, name, call, live):
    cx = call.get("context") or {}
    usual = call.get("source") != "model"
    kind, label = ("flat", "A usual week") if usual else lean(call.get("p_up"))
    r = s["returns"]
    stats = [("1 week", r.get("1 week")), ("1 month", r.get("1 month")), ("3 months", r.get("3 months"))]
    lv = live.get(ticker) or {}
    dots = "".join(f'<i class="dot {"hit" if c["right"] else "miss"}" title="{_e(c["date"])}"></i>' for c in lv.get("last", []))
    setup = ""
    if cx.get("state"):
        trend = "above" if cx.get("above_200d") else "below"
        setup = (f"Setup now: <b>{_e(cx['state'])}</b> (RSI {cx['rsi']:.0f}) and {trend} its 200-day average. "
                 f"In {cx['similar_weeks']:,} past weeks like this, {_e(ticker)} was higher a week later {_pct(cx.get('similar_up'), False, 0)} of the time, "
                 f"{_pct(cx.get('similar_avg'))} on average.")
    spread = (f"In 8 of 10 weeks over the past two years it moved between <b class=\"num neg\">{_pct(cx['range_low'])}</b> and "
              f"<b class=\"num pos\">{_pct(cx['range_high'])}</b>." if cx.get("range_low") is not None else "")
    odds = (f"<b>{_pct(call.get('p_up'), False, 0)}</b> chance it is higher after the week" +
            (" (the usual odds)" if usual else f" · <b>{_pct(call.get('p_beat'), False, 0)}</b> it beats the market"))
    return f"""
<article class="card" id="w-{_e(ticker.lower())}">
  <div class="top"><h3>{_e(name)} <span class="tick">{_e(ticker)}</span></h3><span class="price">${s['close']:,.2f}</span></div>
  <div class="call {kind}"><span class="chip">{label}</span><span>{odds}</span></div>
  <div class="stats three">{''.join(f'<div><span class="label">{k}</span><span class="num {_sign(v)}">{_pct(v)}</span></div>' for k, v in stats)}</div>
  <p>{spread}</p>
  <p>{setup}</p>
  {f'<div class="record"><span class="label">Last {len(lv.get("last", []))} weekly calls</span><span class="dots">{dots}</span></div>' if dots else ''}
</article>"""


def weekly_panel(insight, names, focus, rest):
    wk = insight.get("weekly")
    if not wk or not wk.get("calls"):
        return '<section class="when"><h2>Week ahead</h2><p>The first week-ahead calls appear after the next nightly run.</p></section>'
    calls, live = wk["calls"], wk.get("live") or {}
    rec = wk["record"]["up"]
    stocks = insight["stocks"]
    shown = [t for t in focus if t in calls and t in stocks]
    others = sorted(t for t in calls if t in stocks and t not in shown)
    first = calls[(shown or others)[0]]
    start, end = pd.Timestamp(first["week_from"]), pd.Timestamp(first["week_to"])
    usual = first.get("source") != "model"
    if usual:
        headline = (f"The best forecast for any of your stocks this week is the usual odds: about <b>{_pct(first['p_up'], False, 0)}</b> "
                    "that it ends the week higher. Each stock below shows how far it typically moves in a week and how it did after setups like today's.")
    else:
        pills = "".join(f'<a class="pill {lean(calls[t]["p_up"])[0]}" href="#w-{_e(t.lower())}">{_e(t)} {lean(calls[t]["p_up"])[1].split()[1]}</a>'
                        for t in shown + others if lean(calls[t]["p_up"])[0] in ("up", "down"))
        headline = f'<span class="leans">{pills or "No stock has a clear lean for this week."}</span>'
    lv = live.get("all", {})
    u, m = rec.get("usual", {}), rec.get("model", {})
    folded = "".join(_week_card(t, stocks[t], names.get(t, t), calls[t], live) for t in others)
    week_opens = datetime.combine(start.date(), SESSION_OPEN, NEW_YORK)
    return f"""
<section class="when">
  <h2>Week ahead: {_day(start)} to {_day(end)}</h2>
  {_too_late(week_opens, "<b>This week has already started</b>, so these odds are no longer a call for it. New odds arrive after the US close.")}
  <ol>
    <li>Each call covers 5 trading days: from the open on <b>{_day(start)}</b> to the close on <b>{_day(end)}</b>.</li>
    <li>If you act, buy at that first open and hold until that last close. The odds are refreshed every night.</li>
  </ol>
  <p>{headline}</p>
</section>
<section class="list">{''.join(_week_card(t, stocks[t], names.get(t, t), calls[t], live) for t in shown)}</section>
{f'<details class="more"><summary>Your other {len(others)} stocks</summary><section class="list">{folded}</section></details>' if others else ''}
<section class="honest">
  <h2>How good are the weekly calls?</h2>
  <p>Every night two ways of calling the week are tested on {rec.get('weeks', 0):,} past weeks since {_e(rec.get('from') or '–')}, each using only what was known at the time.
  The usual odds (how often your stocks rose in the past year's weeks) were right <b>{_pct(u.get('accuracy'), False)}</b> of the time.
  A model using trend, momentum, volatility and market data was right <b>{_pct(m.get('accuracy'), False)}</b>.
  {'The usual odds are ahead, so this tab shows them. If the model pulls ahead, the tab switches to it by itself.' if usual else 'The model is ahead, so this tab shows its odds.'}
  {f"Live so far: {lv.get('right', 0)} of {lv.get('calls', 0)} weekly calls right." if lv.get('calls') else ''}</p>
  <p class="small">The setups and ranges describe the past. They are not a promise about this week. Not financial advice.</p>
</section>"""


MOOD = 0.1  # a week's average headline score beyond +-0.1 reads as positive or negative


def _mood_word(score):
    if score is None:
        return "none", "No headlines"
    return ("up", "Positive") if score > MOOD else ("down", "Negative") if score < -MOOD else ("flat", "Neutral")


def _in_days(n):
    return "today" if n == 0 else "tomorrow" if n == 1 else f"in {n} days"


def _spark(daily):
    """Daily mood as bars around a zero line, oldest on the left; blank days had no headlines."""
    w, h, gap = 14, 40, 4
    bars = []
    for i, d in enumerate(daily):
        if d["score"] is None:
            continue
        size = max(2.0, min(1.0, abs(d["score"]) / 0.5) * h / 2)
        y = h / 2 - size if d["score"] >= 0 else h / 2
        bars.append(f'<rect x="{i * (w + gap)}" y="{y:.1f}" width="{w}" height="{size:.1f}" rx="2" class="{"pos" if d["score"] >= 0 else "neg"}">'
                    f'<title>{_e(_day(d["date"]))}: {d["count"]} headlines, mood {d["score"]:+.2f}</title></rect>')
    width = len(daily) * (w + gap) - gap
    return (f'<svg class="spark" viewBox="0 0 {width} {h}" preserveAspectRatio="none" role="img" aria-label="Headline mood, last {len(daily)} days">'
            f'<line x1="0" x2="{width}" y1="{h / 2}" y2="{h / 2}"/>{"".join(bars)}</svg>')


def _earnings_line(ticker, ev):
    if not ev:
        return "<p>No earnings dates came back from Yahoo Finance tonight.</p>"
    out = []
    if ev.get("next"):
        when = f", {ev['next_time']}" if ev.get("next_time") else ""
        out.append(f"<p><b>Next earnings: {_day(ev['next'], long=True)}{when}</b> ({_in_days(ev['days_until'])}).</p>")
    last = ev.get("last")
    if last:
        s, mv = last.get("surprise"), last.get("move")
        result = ("" if s is None else f" Profit per share came in {abs(s):.1f}% {'above' if s >= 0 else 'below'} what analysts expected"
                  f"{',' if mv is not None else '.'}")
        odd = (" A gap that large usually comes from one-off items, such as gains on investments, rather than the core business."
               if s is not None and abs(s) > 50 else "")
        move = "" if mv is None else f"{' and' if s is not None else ' After it,'} the stock moved <b class=\"num {_sign(mv)}\">{_pct(mv)}</b> the next session."
        out.append(f"<p>Last report: {_day(last['date'])}.{result}{move}{odd}</p>")
    if ev.get("typical_move") is not None and ev.get("reports", 0) >= 3:
        beats = (f" It beat estimates {ev['beat_count']} of the last {ev['beat_of']} times." if ev.get("beat_of") else "")
        out.append(f"<p>Over its last {ev['reports']} reports, {_e(ticker)} moved about <b>{ev['typical_move']:.1%}</b> on the day it reacted, "
                   f"up or down.{beats}</p>")
    return "".join(out)


def _analyst_line(a):
    if not a:
        return ""
    if not a["notes"]:
        return f"<p>Analysts: no new notes in the last {a['days']} days.</p>"
    moves = []
    if a["upgrades"] or a["downgrades"]:
        moves.append(f"{a['upgrades']} upgrade{'s' * (a['upgrades'] != 1)}, {a['downgrades']} downgrade{'s' * (a['downgrades'] != 1)}")
    if a["raised"] or a["cut"]:
        change = a["target_change"]
        avg = ("" if change is None else " (on average about unchanged)" if abs(change) < 0.0005
               else f" (average change <b class=\"num {_sign(change)}\">{_pct(change)}</b>)")
        who = " and ".join(x for x in (f"{a['raised']} raised their price target" if a["raised"] else "",
                                       (f"{a['cut']} cut it" if a["raised"] else f"{a['cut']} cut their price target") if a["cut"] else "") if x)
        moves.append(who + avg)
    return f"<p>Analysts, last {a['days']} days: {a['notes']} notes. {'; '.join(moves) + '.' if moves else 'No rating or target changes.'}</p>"


def _news_card(ticker, s, name):
    p = s.get("press") or {}
    wk = p.get("week") or {}
    kind, label = _mood_word(wk.get("score"))
    trend = {"improving": "better than", "worsening": "worse than", "steady": "about the same as"}.get(p.get("trend"))
    total = wk.get("count") or 0
    bar = "".join(f'<i class="{c}" style="width:{100 * wk.get(k, 0) / total:.1f}%"></i>'
                  for k, c in (("positive", "pos"), ("neutral", "neu"), ("negative", "neg"))) if total else ""
    reads = "".join(f'<li><a href="{_e(r["link"])}" target="_blank" rel="noopener">{_e(r["title"])}</a>'
                    f'<span class="small">{_e(r["outlet"])} · {_day(r["published"][:10])} · {_e(r["mood"])}</span></li>'
                    for r in p.get("read") or [])
    more = p.get("major_count", 0) - len(p.get("read") or [])
    return f"""
<article class="card" id="n-{_e(ticker.lower())}">
  <div class="top"><h3>{_e(name)} <span class="tick">{_e(ticker)}</span></h3><span class="price">${s['close']:,.2f}</span></div>
  <div class="call {kind}"><span class="chip">{label} news</span>
    <span>{total} headlines naming {_e(name)} this week{f", mood {trend} the week before" if trend else ""}.</span></div>
  {f'<div class="moodbar" aria-hidden="true">{bar}</div><div class="ends"><span class="pos">{wk.get("positive", 0)} positive</span><span>{wk.get("neutral", 0)} neutral</span><span class="neg">{wk.get("negative", 0)} negative</span></div>' if total else ''}
  {f'<div><span class="label">Mood, last {len(p["daily"])} days</span>{_spark(p["daily"])}</div>' if p.get("daily") else ''}
  <div class="facts">{_earnings_line(ticker, p.get("earnings"))}{_analyst_line(p.get("analysts"))}</div>
  <div><span class="label">Worth reading this week</span>
    {f'<ul class="reads">{reads}</ul>' if reads else f'<p class="small">No story naming {_e(name)} from a major newsroom this week.</p>'}
    {f'<p class="small more-note">{more} more from major newsrooms this week.</p>' if more > 0 else ''}</div>
</article>"""


def news_panel(insight, names, focus, rest):
    stocks = insight.get("stocks", {})
    have = [t for t in focus + rest if (stocks[t].get("press") or {}).get("week") is not None]
    if not have:
        return '<section class="when"><h2>News</h2><p>News, mood and earnings dates appear after the next nightly run.</p></section>'
    shown, others = [t for t in focus if t in have], [t for t in rest if t in have]
    upcoming = sorted(((stocks[t]["press"].get("earnings") or {}).get("next"), t) for t in have
                      if ((stocks[t]["press"].get("earnings") or {}).get("days_until") or 999) <= 60)
    soon = "".join(
        f'<li><a href="#n-{_e(t.lower())}"><b>{_e(t)}</b><span class="small">{_e(names.get(t, t))}</span></a>'
        f'<span class="date"><b>{_day(d)}</b><span class="small">{_e(ev["next_time"]) + " · " if ev.get("next_time") else ""}{_in_days(ev["days_until"])}</span></span></li>'
        for d, t in upcoming for ev in [stocks[t]["press"]["earnings"]])
    pills = "".join(f'<a class="pill {_mood_word(stocks[t]["press"]["week"]["score"])[0]}" href="#n-{_e(t.lower())}">{_e(t)} '
                    f'{_mood_word(stocks[t]["press"]["week"]["score"])[1].lower()}</a>' for t in shown + others)
    rec = insight.get("news_record") or {}
    folded = "".join(_news_card(t, stocks[t], names.get(t, t)) for t in others)
    return f"""
<section class="when">
  <h2>Earnings coming up</h2>
  {f'<ul class="cal">{soon}</ul>' if soon else '<p>None of your stocks has a report date in the next 60 days.</p>'}
  <p class="small">Dates are from Yahoo Finance. One more than a few weeks away can be an estimate until the company confirms it. Stocks often move more than usual the day after a report.</p>
</section>
<section class="when">
  <h2>News mood this week</h2>
  <p class="leans">{pills}</p>
  <p class="small">Every headline is scored by FinBERT, a model trained on financial news, as positive, neutral or negative. Only headlines that name the company count.</p>
</section>
<section class="list">{''.join(_news_card(t, stocks[t], names.get(t, t)) for t in shown)}</section>
{f'<details class="more"><summary>Your other {len(others)} stocks</summary><section class="list">{folded}</section></details>' if others else ''}
<section class="honest">
  <h2>Does the news mood predict the price?</h2>
  <p>Not so far. {f"On the {rec['days']} nights where the headline mood leaned clearly one way, the stock went that way the next session {_pct(rec['matched'], False, 0)} of the time, about a coin flip." if rec.get('days') else "Results appear once enough nights have been scored."}
  Read the news to understand why a stock is moving and what is coming up, not to time a trade.</p>
</section>"""


def build_page(insight, state, config, now):
    names = company_names()
    stocks = insight.get("stocks", {})
    focus = [t for t in getattr(config, "focus", []) if t in stocks]
    rest = sorted((t for t in stocks if t not in focus), key=lambda t: -(((stocks[t].get("models") or {}).get("up") or {}).get("p") or 0))
    as_of = max((p["feature_date"] for p in state.pending), default=None) if state is not None else None
    session, opens, closes = next_session(as_of) if as_of else (None, None, None)
    record = overall_record(state) if state is not None else {}
    mk = insight.get("market")
    updated = pd.Timestamp(now).tz_convert("UTC")
    made = max((p["made_at"] for p in state.pending if p["feature_date"] == as_of and p.get("made_at")), default=None) if as_of else None
    made = pd.Timestamp(made).tz_convert("UTC") if made else updated

    leans = []
    for t in focus + rest:
        kind, label = lean((((stocks[t].get("models") or {}).get("up")) or {}).get("p"))
        if kind in ("up", "down"):
            leans.append(f'<a class="pill {kind}" href="#{_e(t.lower())}">{_e(t)} {label.split()[1]}</a>')

    market = ""
    if mk:
        market = f"""
<section class="market"><span class="label">S&amp;P 500 (SPY)</span><span class="num">${mk['close']:,.2f}</span>
  <span>This year <b class="num {_sign(mk.get('ytd'))}">{_pct(mk.get('ytd'))}</b></span>
  <span>Past year <b class="num {_sign(mk['returns'].get('1 year'))}">{_pct(mk['returns'].get('1 year'))}</b></span>
  <span class="small">{_e(' '.join(mk.get('summary', [])))}</span></section>"""

    when = ""
    if session:
        when = f"""
<section class="when">
  <h2>Next day: {_day(session)}</h2>
  {_too_late(opens, f"<b>{_day(session, long=True)}'s session has already opened</b>, so it's too late to act on these calls. The next ones arrive after the US close.")}
  <ol>
    <li>New calls arrive every weekday night after the US market closes. These were made <b><time data-utc="{made.isoformat()}">{made:%a %d %b, %H:%M} UTC</time></b>, before the open.</li>
    <li>They are for <b>{_day(session, long=True)}</b>: from the open at <b><time data-utc="{opens.isoformat()}" data-short>9:30am New York</time></b> to the close at <b><time data-utc="{closes.isoformat()}" data-short>4:00pm New York</time></b>.</li>
    <li>If you act on a call, act at the open. The call is settled at that day's close.</li>
  </ol>
  <p class="leans">{''.join(leans) or 'No stock has a clear lean tonight.'}</p>
  <p class="small">The models are right a bit over half the time. Keep any bet small. Not financial advice.</p>
</section>"""

    others = "".join(_card(t, stocks[t], names.get(t, t), open_details=False) for t in rest)
    acc = record.get("accuracy")
    body = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Stock Lab</title>
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Stock Lab"><meta name="theme-color" content="#1f6f54">
<link rel="icon" href="data:image/svg+xml,{ICON}">
<link rel="apple-touch-icon" href="data:image/svg+xml,{ICON}">
<style>{CSS}</style></head>
<body><main>
<header><span class="label">Stock prediction lab</span>
  <h1>Your stock calls</h1>
  <p class="small">Prices up to {_e((mk or {}).get('as_of', '–'))} · models retrained every weekday night</p></header>
<input class="tabsel" type="radio" name="tab" id="tab-day" checked>
<input class="tabsel" type="radio" name="tab" id="tab-week">
<input class="tabsel" type="radio" name="tab" id="tab-news">
<nav class="tabs"><label for="tab-day">Next day</label><label for="tab-week">Next week</label><label for="tab-news">News</label></nav>
<div class="panel day">
{when}
{market}
<section class="list">{''.join(_card(t, stocks[t], names.get(t, t)) for t in focus)}</section>
{f'<details class="more"><summary>Your other {len(rest)} stocks</summary><section class="list">{others}</section></details>' if rest else ''}
<section class="honest">
  <h2>How good are the daily calls?</h2>
  <p>Over the last {CHAMPION_WINDOW} sessions the lead model was right <b>{_pct(acc, False)}</b> of the time. Simply guessing "up" every day was right {_pct(record.get('always_up'), False)}.
  Since it went live it has been right on {record.get('live_right', 0)} of {record.get('live_total', 0)} calls. Use the calls as one clue next to the trend and the news, not as a signal on their own.</p>
</section>
</div>
<div class="panel week">
{weekly_panel(insight, names, focus, rest)}
</div>
<div class="panel news">
{news_panel(insight, names, focus, rest)}
</div>
<footer><p><a href="{REPO_URL}/blob/main/reports/latest.md">Full report</a> · <a href="{REPO_URL}">Project on GitHub</a></p>
  <p>Educational project. Not financial advice.</p></footer>
</main>
<script>{JS}</script>
</body></html>
"""
    return body


def write(insight, state, config, now, docs_dir=ROOT / "docs"):
    docs_dir = Path(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / ".nojekyll").write_text("")
    (docs_dir / "index.html").write_text(build_page(insight, state, config, now))


ICON = ("%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231f6f54'/%3E"
        "%3Cpath d='M12 44l13-14 9 8 17-20' stroke='white' stroke-width='6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")

CSS = """
:root{--bg:#f6f7f4;--surface:#fff;--fg:#1d2420;--muted:#5d6a63;--line:#dfe4df;--accent:#1f6f54;--up:#1f7a4d;--down:#b4442f;--flat:#6b6f6c;--track:#e7ece8;
--display:Georgia,"Iowan Old Style",serif;--body:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#121614;--surface:#1a201d;--fg:#e6ebe7;--muted:#9aa8a0;--line:#2b3430;--accent:#5cc49b;--up:#5cc48c;--down:#ec8a74;--flat:#a3aaa6;--track:#26302b;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 var(--body);padding:max(20px,env(safe-area-inset-top)) 16px max(40px,env(safe-area-inset-bottom))}
main{max-width:680px;margin:0 auto;display:flex;flex-direction:column;gap:24px}
h1,h2,h3{font-family:var(--display);margin:0;line-height:1.2;text-wrap:balance}
h1{font-size:1.9rem}h2{font-size:1.3rem}h3{font-size:1.2rem}
p{margin:0}a{color:var(--accent)}
.label{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}
.small{font-size:.86rem;color:var(--muted)}
.num,.price{font-family:var(--mono);font-variant-numeric:tabular-nums}
.pos{color:var(--up)}.neg{color:var(--down)}
header{display:flex;flex-direction:column;gap:6px}
.when{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:18px;display:flex;flex-direction:column;gap:12px}
.when ol{margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:6px}
.leans{display:flex;flex-wrap:wrap;gap:8px}
.pill{font-weight:600;font-size:.9rem;padding:4px 12px;border-radius:99px;border:1px solid currentColor;text-decoration:none}
.pill.up{color:var(--up)}.pill.down{color:var(--down)}
.market{border-block:1px solid var(--line);padding-block:12px;display:flex;flex-wrap:wrap;gap:6px 20px;align-items:baseline}
.list{display:flex;flex-direction:column;gap:16px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:18px;display:flex;flex-direction:column;gap:14px}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.tick{font:600 .8rem var(--mono);color:var(--muted)}
.price{font-size:1.3rem}
.call{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.chip{font-weight:600;font-size:.85rem;padding:2px 10px;border-radius:99px;border:1px solid currentColor}
.call.up .chip{color:var(--up)}.call.down .chip{color:var(--down)}.call.flat .chip,.call.none .chip{color:var(--flat)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.stats div{display:flex;flex-direction:column;min-width:0}
@media (max-width:520px){.stats{grid-template-columns:repeat(2,1fr)}}
.stats.three{grid-template-columns:repeat(3,1fr)}
.range{display:flex;flex-direction:column;gap:6px}
.bar{position:relative;height:8px;background:var(--track);border-radius:4px}
.bar i{position:absolute;top:-4px;width:4px;height:16px;border-radius:2px;background:var(--accent);transform:translateX(-50%)}
.ends{display:flex;justify-content:space-between;font:.8rem var(--mono);color:var(--muted)}
details summary{cursor:pointer;font-weight:600;color:var(--accent)}
details ul{margin:10px 0 0;padding-left:1.1em;display:flex;flex-direction:column;gap:6px}
.heads{font-size:.9rem;color:var(--muted)}
.more>summary{font-family:var(--display);font-size:1.2rem;padding-block:6px}
.more .list{margin-top:12px}
.record{border-top:1px solid var(--line);padding-top:12px;display:flex;flex-direction:column;gap:6px}
.dots{display:flex;gap:6px}
.dot{width:14px;height:14px;border-radius:50%;display:inline-block}
.dot.hit{background:var(--up)}.dot.miss{background:var(--down);opacity:.75}
.honest{display:flex;flex-direction:column;gap:10px}
footer{font-size:.86rem;color:var(--muted);display:flex;flex-direction:column;gap:6px}
.tabsel{position:absolute;opacity:0;pointer-events:none}
.tabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:2;display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;padding:4px;background:var(--track);border-radius:10px}
.tabs label{text-align:center;padding:9px 0;border-radius:8px;font-weight:600;cursor:pointer;color:var(--muted)}
#tab-day:checked~.tabs label[for=tab-day],#tab-week:checked~.tabs label[for=tab-week],#tab-news:checked~.tabs label[for=tab-news]{background:var(--surface);color:var(--fg);box-shadow:0 1px 2px rgba(0,0,0,.12)}
#tab-day:focus-visible~.tabs label[for=tab-day],#tab-week:focus-visible~.tabs label[for=tab-week],#tab-news:focus-visible~.tabs label[for=tab-news]{outline:2px solid var(--accent)}
.panel{display:flex;flex-direction:column;gap:24px}
.panel.week,.panel.news,#tab-week:checked~.panel.day,#tab-news:checked~.panel.day{display:none}
#tab-week:checked~.panel.week,#tab-news:checked~.panel.news{display:flex}
.pill.flat{color:var(--flat)}
.stale{margin:0;padding:10px 12px;border-left:3px solid var(--down);background:var(--track);border-radius:6px}
.stale[hidden]{display:none}
.moodbar{display:flex;height:8px;border-radius:4px;overflow:hidden;background:var(--track)}
.moodbar i{display:block;height:100%}.moodbar .pos{background:var(--up)}.moodbar .neu{background:var(--flat);opacity:.35}.moodbar .neg{background:var(--down)}
.spark{display:block;width:100%;height:44px;margin-top:6px}
.spark line{stroke:var(--line);stroke-width:1}.spark .pos{fill:var(--up)}.spark .neg{fill:var(--down)}
.facts{display:flex;flex-direction:column;gap:8px}
.reads{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;gap:12px}
.reads li{display:flex;flex-direction:column;gap:2px}
.reads a{color:var(--fg);font-weight:600;text-decoration:none}
.reads a:active{color:var(--accent)}
.cal{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.cal li{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 0;border-top:1px solid var(--line)}
.cal li:first-child{border-top:0}
.cal a,.cal .date{display:flex;flex-direction:column;min-width:0}
.cal a{text-decoration:none;color:var(--fg)}
.cal .date{text-align:right}
.more-note{margin-top:10px}
"""

JS = """
const week = document.getElementById('tab-week'), day = document.getElementById('tab-day'), news = document.getElementById('tab-news');
if (location.hash === '#weekly' || location.hash.startsWith('#w-')) week.checked = true;
if (location.hash === '#news' || location.hash.startsWith('#n-')) news.checked = true;
week.addEventListener('change', () => history.replaceState(null, '', '#weekly'));
news.addEventListener('change', () => history.replaceState(null, '', '#news'));
day.addEventListener('change', () => history.replaceState(null, '', location.pathname));
for (const el of document.querySelectorAll('.stale[data-after]')) if (Date.now() >= Date.parse(el.dataset.after)) el.hidden = false;
for (const el of document.querySelectorAll('time[data-utc]')) {
  const d = new Date(el.dataset.utc);
  if (isNaN(d)) continue;
  const opts = el.hasAttribute('data-short') ? {hour: 'numeric', minute: '2-digit'} : {weekday: 'short', day: 'numeric', month: 'short', hour: 'numeric', minute: '2-digit'};
  const local = d.toLocaleString([], opts);
  el.textContent = el.hasAttribute('data-short') ? el.textContent + ' (' + local + ' your time)' : local + ' your time';
}
"""


def write_from_reports(state, config, now, reports_dir=ROOT / "reports", docs_dir=ROOT / "docs"):
    """Rebuild the page from the last saved insight (no downloads)."""
    path = Path(reports_dir) / "insight.json"
    if path.exists():
        write(json.loads(path.read_text()), state, config, now, docs_dir)
