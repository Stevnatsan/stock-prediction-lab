"""What traders are posting: StockTwits (no key; posters can tag a message Bullish or Bearish) and
Reddit's investing communities (needs a free Reddit app: REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET)."""
import re
from datetime import datetime, timezone

import requests

from .. import sentiment
from .news import USER_AGENT

STOCKTWITS = "https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json"
REDDIT_TOKEN = "https://www.reddit.com/api/v1/access_token"
REDDIT_SEARCH = "https://oauth.reddit.com/r/{subs}/search"
SUBREDDITS = "wallstreetbets+stocks+investing+StockMarket"


def stocktwits_posts(ticker):
    response = requests.get(STOCKTWITS.format(ticker=ticker.replace("-", ".")), headers={"User-Agent": USER_AGENT}, timeout=20)
    response.raise_for_status()
    posts = []
    for m in response.json().get("messages", []):
        label = ((m.get("entities") or {}).get("sentiment") or {}).get("basic")
        mood = 1.0 if label == "Bullish" else -1.0 if label == "Bearish" else None
        published = datetime.strptime(m["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        posts.append({"published": published.isoformat(), "mood": mood, "source": "stocktwits"})
    return posts


class RedditClient:
    def __init__(self, client_id, client_secret):
        self.auth = (client_id, client_secret)
        self.headers = {"User-Agent": USER_AGENT}

    def _login(self):
        if "Authorization" not in self.headers:
            response = requests.post(REDDIT_TOKEN, auth=self.auth, data={"grant_type": "client_credentials"},
                                     headers=self.headers, timeout=20)
            response.raise_for_status()
            self.headers["Authorization"] = f"bearer {response.json()['access_token']}"

    def posts(self, ticker):
        """This week's posts that mention the ticker as a word or $cashtag; mood is the title's sentiment."""
        self._login()
        params = {"q": ticker, "restrict_sr": 1, "sort": "new", "t": "week", "limit": 100}
        response = requests.get(REDDIT_SEARCH.format(subs=SUBREDDITS), params=params, headers=self.headers, timeout=20)
        response.raise_for_status()
        mention = re.compile(rf"(?<![A-Za-z])\$?{re.escape(ticker)}(?![A-Za-z])")
        posts = []
        for child in response.json().get("data", {}).get("children", []):
            d = child.get("data", {})
            if not mention.search(d.get("title", "")):
                continue
            score = sentiment.score(d["title"])
            posts.append({"published": datetime.fromtimestamp(d["created_utc"], tz=timezone.utc).isoformat(),
                          "mood": score if abs(score) >= 0.05 else None, "source": "reddit"})
        return posts
