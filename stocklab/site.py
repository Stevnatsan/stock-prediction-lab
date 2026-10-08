"""docs/index.html: one phone-friendly page with tonight's calls and the plain-language insight,
rewritten by every daily run. Turn on GitHub Pages (Settings -> Pages -> Deploy from a branch ->
main, /docs) and it lives at https://<user>.github.io/<repo>/, ready to add to a phone's home screen.
"""
import html
import json
import os
from datetime import datetime, time, timedelta
from pathlib import Path

import pandas as pd

from .config import ROOT
from .sources.prices import NEW_YORK
from .strategy import CHAMPION_WINDOW, champion

LEAN = 0.02  # a call more than 2 points from 50% counts as a lean
REPO_URL = "https://github.com/" + os.environ.get("GITHUB_REPOSITORY", "Stevnatsan/stock-prediction-lab")


def company_names():
    path = ROOT / "catalogue" / "sp500.csv"
    if not path.exists():
        return {}
    rows = pd.read_csv(path)
    return {s: str(n).split(" (")[0].replace(" Inc.", "").replace(" Corporation", "") for s, n in zip(rows["symbol"], rows["name"])}


def next_session(after):
    """The next weekday after `after` (market holidays aside) and its 9:30 and 16:00 New York times."""
    day = pd.Timestamp(after) + pd.offsets.BDay(1)
    opens = datetime.combine(day.date(), time(9, 30), NEW_YORK)
    return day.date(), opens, opens + timedelta(hours=6, minutes=30)


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



def _week_card(ticker, s, name, call, record, live):
    kind, label = lean(call.get("p_up"))
    r, rec = s["returns"], record.get(ticker) or {}
    stats = [("1 week", r.get("1 week")), ("1 month", r.get("1 month")), ("3 months", r.get("3 months"))]
    trend = (s.get("summary") or [""])[0]
    lv = live.get(ticker) or {}
    dots = "".join(f'<i class="dot {"hit" if c["right"] else "miss"}" title="{_e(c["date"])}"></i>' for c in lv.get("last", []))
    acc, base = rec.get("accuracy"), rec.get("always_yes")
    edge = ("better than" if acc is not None and base is not None and acc > base + 0.01 else
            "no better than" if acc is not None and base is not None and acc < base - 0.01 else "about the same as")
    when_up = rec.get("avg_week_when_leaning_up")
    lean_line = (f" In weeks when it clearly leaned up, {_e(ticker)} moved {_pct(when_up)} on average, against {_pct(rec.get('avg_week'))} for an average week."
                 if when_up is not None else "")
    return f"""
<article class="card" id="w-{_e(ticker.lower())}">
  <div class="top"><h3>{_e(name)} <span class="tick">{_e(ticker)}</span></h3><span class="price">${s['close']:,.2f}</span></div>
  <div class="call {kind}">
    <span class="chip">{label}</span>
    <span><b>{_pct(call.get('p_up'), False, 0)}</b> chance it is higher after the week · <b>{_pct(call.get('p_beat'), False, 0)}</b> it beats the market</span>
  </div>
  <div class="stats">{''.join(f'<div><span class="label">{k}</span><span class="num {_sign(v)}">{_pct(v)}</span></div>' for k, v in stats)}</div>
  <p>{_e(trend)}</p>
  <div class="record">
    {f'<span class="label">Last {len(lv.get("last", []))} weekly calls</span><span class="dots">{dots}</span>' if dots else ''}
    <p class="small">Tested on {rec.get('calls', 0):,} past weeks of {_e(ticker)}: right {_pct(acc, False)} of the time, {edge} always guessing "up" ({_pct(base, False)}).{lean_line}</p>
  </div>
</article>"""


def weekly_panel(insight, names, focus, rest):
    wk = insight.get("weekly")
    if not wk or not wk.get("calls"):
        return '<section class="when"><h2>Week ahead</h2><p>The first week-ahead calls appear after the next nightly run.</p></section>'
    calls, record, live = wk["calls"], wk["record"]["up"], wk.get("live") or {}
    stocks = insight["stocks"]
    shown = [t for t in focus if t in calls]
    others = sorted((t for t in calls if t in stocks and t not in shown), key=lambda t: -calls[t]["p_up"])
    first = next(iter(calls.values()))
    start, end = pd.Timestamp(first["week_from"]), pd.Timestamp(first["week_to"])
    pills = []
    for t in shown + others:
        kind, label = lean(calls[t]["p_up"])
        if kind in ("up", "down"):
            pills.append(f'<a class="pill {kind}" href="#w-{_e(t.lower())}">{_e(t)} {label.split()[1]}</a>')
    overall = record.get("all", {})
    lv = live.get("all", {})
    folded = "".join(_week_card(t, stocks[t], names.get(t, t), calls[t], record, live) for t in others)
    return f"""
<section class="when">
  <h2>Week ahead: {start:%a %d %b} to {end:%a %d %b}</h2>
  <ol>
    <li>Each call is for one week of 5 trading days: from the open on <b>{start:%a %d %b}</b> to the close on <b>{end:%a %d %b}</b>.</li>
    <li>If you act on one, buy at that first open and hold until that last close. The calls are refreshed every night, so check again before you buy.</li>
  </ol>
  <p class="leans">{''.join(pills) or 'No stock has a clear lean for this week.'}</p>
</section>
<section class="list">{''.join(_week_card(t, stocks[t], names.get(t, t), calls[t], record, live) for t in shown)}</section>
{f'<details class="more"><summary>Your other {len(others)} stocks</summary><section class="list">{folded}</section></details>' if others else ''}
<section class="honest">
  <h2>How good are the weekly calls?</h2>
  <p>Tested on {overall.get('calls', 0):,} past weeks since {_e(overall.get('from') or '–')}, each predicted only from what was known at the time: right <b>{_pct(overall.get('accuracy'), False)}</b> of the time.
  Always guessing "up" was right {_pct(overall.get('always_yes'), False)}, because stocks rise in most weeks. When the model was fairly sure (at least 55% one way), it was right {_pct(overall.get('confident_accuracy'), False)} of {overall.get('confident_calls', 0):,} calls.
  {f"Live so far: {lv.get('right', 0)} of {lv.get('calls', 0)} weekly calls right." if lv.get('calls') else 'Live weekly calls are scored here as each week ends.'}</p>
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
  <h2>Next day: {session:%a %d %b}</h2>
  <ol>
    <li>New calls arrive every weekday night after the US market closes. This page was updated <b><time data-utc="{updated.isoformat()}">{updated:%a %d %b, %H:%M} UTC</time></b>.</li>
    <li>They are for <b>{session:%A %d %b}</b>: from the open at <b><time data-utc="{opens.isoformat()}" data-short>9:30am New York</time></b> to the close at <b><time data-utc="{closes.isoformat()}" data-short>4:00pm New York</time></b>.</li>
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
<nav class="tabs"><label for="tab-day">Next day</label><label for="tab-week">Next week</label></nav>
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
<footer><a href="{REPO_URL}/blob/main/reports/latest.md">Full report</a> · <a href="{REPO_URL}">Project on GitHub</a>
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
.tabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:4px;background:var(--track);border-radius:10px}
.tabs label{text-align:center;padding:9px 0;border-radius:8px;font-weight:600;cursor:pointer;color:var(--muted)}
#tab-day:checked~.tabs label[for=tab-day],#tab-week:checked~.tabs label[for=tab-week]{background:var(--surface);color:var(--fg);box-shadow:0 1px 2px rgba(0,0,0,.12)}
#tab-day:focus-visible~.tabs label[for=tab-day],#tab-week:focus-visible~.tabs label[for=tab-week]{outline:2px solid var(--accent)}
.panel{display:flex;flex-direction:column;gap:24px}
.panel.week,#tab-week:checked~.panel.day{display:none}
#tab-week:checked~.panel.week{display:flex}
"""

JS = """
const week = document.getElementById('tab-week'), day = document.getElementById('tab-day');
if (location.hash === '#weekly' || location.hash.startsWith('#w-')) week.checked = true;
week.addEventListener('change', () => history.replaceState(null, '', '#weekly'));
day.addEventListener('change', () => history.replaceState(null, '', location.pathname));
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
