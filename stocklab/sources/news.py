"""Headlines from RSS feeds (no key) and, optionally, Finnhub (free API key)."""
import calendar
import hashlib
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import quote_plus

import feedparser
import requests

USER_AGENT = "Mozilla/5.0 (compatible; stock-prediction-lab; +https://github.com/Stevnatsan/stock-prediction-lab)"
YAHOO_RSS = "https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
FINNHUB_NEWS = "https://finnhub.io/api/v1/company-news"


def headline_id(title):
    normalised = re.sub(r"[^a-z0-9 ]", "", title.lower())
    normalised = re.sub(r"\s+", " ", normalised).strip()
    return hashlib.sha1(normalised.encode()).hexdigest()[:16]


def _entry(title, published, source, link):
    title = re.sub(r"\s+", " ", title or "").strip()
    return {"id": headline_id(title), "title": title, "published": published.isoformat(), "source": source, "link": link or ""}


def _rss(url, source):
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
    response.raise_for_status()
    feed = feedparser.parse(response.content)
    items = []
    for e in feed.entries:
        stamp = e.get("published_parsed") or e.get("updated_parsed")
        if not stamp or not e.get("title"):
            continue
        published = datetime.fromtimestamp(calendar.timegm(stamp), tz=timezone.utc)
        items.append(_entry(e.title, published, source, e.get("link")))
    return items


def yahoo_headlines(ticker):
    return _rss(YAHOO_RSS.format(ticker=ticker), "yahoo_rss")


def google_headlines(ticker):
    return _rss(GOOGLE_NEWS_RSS.format(query=quote_plus(f"{ticker} stock")), "google_news")


def finnhub_headlines(ticker, api_key, now):
    params = {"symbol": ticker, "from": (now - timedelta(days=3)).date().isoformat(), "to": now.date().isoformat(), "token": api_key}
    response = requests.get(FINNHUB_NEWS, params=params, timeout=20)
    response.raise_for_status()
    return [_entry(item.get("headline"), datetime.fromtimestamp(item["datetime"], tz=timezone.utc), "finnhub", item.get("url"))
            for item in response.json() if item.get("headline") and item.get("datetime")]
