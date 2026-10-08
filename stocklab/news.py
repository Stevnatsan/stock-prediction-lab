"""The News tab: what the press is saying about each stock, how the mood is moving, which stories
from established newsrooms are worth reading, and when the company reports earnings next.

Headlines are the ones the daily run collects (Yahoo Finance and Google News feeds, plus a Google News
search limited to major newsrooms), each scored by FinBERT (or VADER where FinBERT didn't run). Only
headlines that name the company or its ticker count here: the feeds also return market round-ups and
stories about other companies. A story counts as *from a major outlet* when its publisher is on
MAJOR_OUTLETS: newsrooms with their own reporters and editors. Content farms, stock-promotion sites,
reposted press releases (Morningstar's and Financial Post's news pages carry wire releases, and law-firm
"class action" notices are dropped by title) and sites that mostly republish partner content (The Globe
and Mail's and USA Today's stock pages carry The Motley Fool, for one) are left off the reading list;
they still count in the mood.
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import numpy as np
import pandas as pd

from .config import ROOT
from .sources.prices import NEW_YORK

MAJOR_OUTLETS = {
    "reuters": "Reuters", "bloomberg": "Bloomberg", "bloomberg.com": "Bloomberg", "the wall street journal": "The Wall Street Journal",
    "wsj": "The Wall Street Journal", "financial times": "Financial Times", "cnbc": "CNBC", "associated press": "Associated Press",
    "ap news": "Associated Press", "the new york times": "The New York Times", "the washington post": "The Washington Post",
    "barron's": "Barron's", "marketwatch": "MarketWatch", "axios": "Axios", "fortune": "Fortune", "business insider": "Business Insider",
    "investor's business daily": "Investor's Business Daily", "fox business": "Fox Business",
    "cnn": "CNN", "bbc": "BBC", "the verge": "The Verge", "techcrunch": "TechCrunch", "wired": "Wired",
    "the information": "The Information", "quartz": "Quartz",
}
DOMAINS = {
    "reuters.com": "Reuters", "bloomberg.com": "Bloomberg", "wsj.com": "The Wall Street Journal", "ft.com": "Financial Times",
    "cnbc.com": "CNBC", "apnews.com": "Associated Press", "nytimes.com": "The New York Times", "washingtonpost.com": "The Washington Post",
    "barrons.com": "Barron's", "marketwatch.com": "MarketWatch", "axios.com": "Axios", "fortune.com": "Fortune",
    "businessinsider.com": "Business Insider", "investors.com": "Investor's Business Daily", "foxbusiness.com": "Fox Business", "cnn.com": "CNN", "bbc.com": "BBC", "bbc.co.uk": "BBC", "theverge.com": "The Verge",
    "techcrunch.com": "TechCrunch", "wired.com": "Wired", "theinformation.com": "The Information",
    "qz.com": "Quartz",
}
# law-firm and investor-relations releases that newsroom sites also host
PRESS_RELEASE = re.compile(r"class action|shareholder alert|investor alert|securities fraud|lawsuit (?:filed|deadline)|investors who lost|"
                           r"law (?:firm|offices)|deadline alert|on behalf of investors|press release", re.I)
ALIASES = {"GOOGL": ["google"], "GOOG": ["google"], "META": ["facebook"]}  # names headlines use besides the company's own
SUFFIX = re.compile(r"\s+-\s+([^-]{2,60})$")
POSITIVE, NEGATIVE = 0.2, -0.2  # FinBERT score (P(positive) - P(negative)) beyond which a headline counts as one or the other


def words_for(ticker):
    """Words a headline about `ticker` would contain: the symbol, the company's first name word and any alias."""
    words = {ticker.lower(), *ALIASES.get(ticker, [])}
    catalogue = ROOT / "catalogue" / "sp500.csv"
    if catalogue.exists():
        rows = pd.read_csv(catalogue)
        for name in rows.loc[rows["symbol"] == ticker, "name"]:
            words.add(str(name).split()[0].strip(",.").lower())
    return words


def mentions(title, words):
    return bool(re.search(r"\b(" + "|".join(re.escape(w) for w in sorted(words)) + r")\b", title, re.I)) if words else True


def split_title(item):
    """(headline without the " - Publisher" tail Google News adds, publisher name)."""
    title = item.get("title", "")
    match = SUFFIX.search(title)
    if match:
        return title[:match.start()].strip(), match.group(1).strip()
    host = urlparse(item.get("link") or "").netloc.lower().removeprefix("www.")
    return title, host or item.get("source", "")


def outlet(publisher):
    """The major outlet's display name, or None."""
    p = publisher.lower().strip()
    if p in MAJOR_OUTLETS:
        return MAJOR_OUTLETS[p]
    for domain, name in DOMAINS.items():
        if p == domain or p.endswith("." + domain):
            return name
    return None


def mood_of(item):
    s = item.get("finbert")
    if s is None:
        s = item.get("score", 0.0) * 2  # VADER compound runs smaller; roughly put it on FinBERT's scale
    return float(s)


def _label(score):
    return "positive" if score > POSITIVE else "negative" if score < NEGATIVE else "neutral"


def headlines(state_root, ticker):
    path = Path(state_root) / "news" / f"{ticker}.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines() if line] if path.exists() else []


def about(items, words):
    """Headlines that name the company, each story once (the same title from two publishers counts once)."""
    out, seen = [], set()
    for h in sorted(items, key=lambda h: h["published"]):
        title = split_title(h)[0]
        key = re.sub(r"[^a-z0-9]", "", title.lower())
        if key in seen or not mentions(title, words):
            continue
        seen.add(key)
        out.append(h)
    return out


def mood(items):
    if not items:
        return {"count": 0, "score": None, "positive": 0, "neutral": 0, "negative": 0}
    scores = [mood_of(h) for h in items]
    labels = [_label(s) for s in scores]
    return {"count": len(items), "score": float(sum(scores) / len(scores)),
            **{k: labels.count(k) for k in ("positive", "neutral", "negative")}}


def daily_mood(items, now, days=14):
    """Average mood per New York calendar day, oldest first (None on days without headlines)."""
    by_day = {}
    for h in items:
        day = pd.Timestamp(h["published"]).tz_convert(NEW_YORK).date()
        by_day.setdefault(day, []).append(mood_of(h))
    today = pd.Timestamp(now).tz_convert(NEW_YORK).date()
    out = []
    for i in range(days - 1, -1, -1):
        day = today - pd.Timedelta(days=i)
        values = by_day.get(day, [])
        out.append({"date": day.isoformat(), "count": len(values), "score": sum(values) / len(values) if values else None})
    return out


def _timing(released):
    if released.hour >= 16:
        return "after the close"
    if released.hour < 10:
        return "before the open"
    return None


def reaction(released, prices):
    """The stock's move over the first session that could react to a report: the close-to-close
    change into the first session that closed after the release."""
    if prices is None or not len(prices):
        return None
    close = prices["close"].dropna()
    closes_at = pd.DatetimeIndex(close.index).normalize() + pd.Timedelta(hours=16)
    after = np.flatnonzero(closes_at > released)
    if not len(after) or after[0] == 0:
        return None
    i = after[0]
    return float(close.iloc[i] / close.iloc[i - 1] - 1)


def earnings_info(events, now, prices=None, history=8):
    """Next scheduled report, and the last few: EPS surprise vs estimates and how the stock moved next."""
    if events is None or not len(events):
        return None
    released = pd.DatetimeIndex(events["released"])
    stamp = pd.Timestamp(now).tz_convert(NEW_YORK).tz_localize(None)
    upcoming, past = events[released > stamp], events[released <= stamp]
    out = {}
    if len(upcoming):
        nxt = pd.Timestamp(upcoming["released"].iloc[0])
        out["next"] = nxt.date().isoformat()
        out["next_time"] = _timing(nxt)
        out["days_until"] = (nxt.normalize() - stamp.normalize()).days
    reports = []
    for _, row in past.tail(history).iterrows():
        when = pd.Timestamp(row["released"])
        reports.append({"date": when.date().isoformat(), "surprise": None if pd.isna(row["surprise"]) else float(row["surprise"]),
                        "move": reaction(when, prices)})
    if reports:
        out["last"] = reports[-1]
        moves = [abs(r["move"]) for r in reports if r["move"] is not None]
        out["typical_move"] = float(np.mean(moves)) if moves else None
        out["reports"] = len(moves)
        beats = [r["surprise"] for r in reports if r["surprise"] is not None]
        out["beat_count"], out["beat_of"] = sum(s > 0 for s in beats), len(beats)
    return out or None


def analyst_info(actions, now, days=30):
    if actions is None or not len(actions):
        return None
    stamp = pd.Timestamp(now).tz_convert(NEW_YORK).tz_localize(None)
    recent = actions[pd.DatetimeIndex(actions["time"]) >= stamp - pd.Timedelta(days=days)]
    targets = recent["target"].dropna()
    targets = targets[targets != 0]
    return {"days": days, "notes": int(len(recent)), "upgrades": int((recent["rating"] > 0).sum()),
            "downgrades": int((recent["rating"] < 0).sum()), "raised": int((targets > 0).sum()), "cut": int((targets < 0).sum()),
            "target_change": float(np.exp(targets.mean()) - 1) if len(targets) else None}


def track_record(state, col="finbert_mean"):
    """How often a clearly positive or negative headline mood (the night before) matched the next session."""
    live, preds = state.live, state.predictions
    if live.empty or col not in live:
        return None
    done = preds.loc[(preds["variant"] == "full") & preds["outcome_up"].notna(), ["ticker", "feature_date", "outcome_up"]]
    s = live.merge(done, on=["ticker", "feature_date"])
    s = s[s[col].abs() >= 0.05]
    if s.empty:
        return None
    return {"days": int(len(s)), "matched": float(((s[col] > 0) == (s["outcome_up"] == 1)).mean())}


def brief(state_root, ticker, now, earnings=None, analysts=None, prices=None, words=None, read=5):
    """Everything the News tab shows for one stock."""
    words = words_for(ticker) if words is None else words
    items = about(headlines(state_root, ticker), words)
    now_ts = pd.Timestamp(now)
    week = [h for h in items if pd.Timestamp(h["published"]) >= now_ts - pd.Timedelta(days=7)]
    before = [h for h in items if now_ts - pd.Timedelta(days=14) <= pd.Timestamp(h["published"]) < now_ts - pd.Timedelta(days=7)]
    this, last = mood(week), mood(before)
    trend = None
    if this["score"] is not None and last["score"] is not None:
        delta = this["score"] - last["score"]
        trend = "improving" if delta > 0.05 else "worsening" if delta < -0.05 else "steady"
    major, picked = [], []
    for h in sorted(week, key=lambda h: h["published"], reverse=True):
        title, publisher = split_title(h)
        name = outlet(publisher)
        if name is None or PRESS_RELEASE.search(title):
            continue
        major.append(h)
        if len(picked) < read and sum(p["outlet"] == name for p in picked) < 2:  # newest first, at most 2 per outlet
            picked.append({"title": title, "outlet": name, "link": h.get("link", ""), "published": h["published"],
                           "mood": _label(mood_of(h))})
    return {"week": this, "previous_week": last, "trend": trend, "major_mood": mood(major),
            "daily": daily_mood(items, now), "read": picked, "major_count": len(major),
            "earnings": earnings_info(earnings, now, prices), "analysts": analyst_info(analysts, now)}
