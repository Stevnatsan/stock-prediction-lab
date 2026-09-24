"""Every data source behind one interface. A failing source is recorded and skipped, never fatal,
because RSS feeds and free APIs change without notice."""
import importlib.util
import os
from collections import defaultdict

from . import events, filings, macro, news, options, prices, social


class LiveSources:
    def __init__(self, config):
        self.config = config
        self.health = defaultdict(lambda: {"ok": 0, "failed": 0, "items": 0, "last_error": ""})
        self.finnhub_key = self._key("finnhub", "FINNHUB_API_KEY")
        sec_agent = self._key("sec_filings", "SEC_USER_AGENT")
        self.edgar = filings.EdgarClient(sec_agent) if sec_agent else None
        reddit_id, reddit_secret = self._key("reddit", "REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET")
        self.reddit = social.RedditClient(reddit_id, reddit_secret) if reddit_id else None
        self.broker = None
        if config.paper_orders.get("enabled"):
            key, secret = self._key("alpaca", "ALPACA_API_KEY", "ALPACA_SECRET_KEY", enabled=True)
            if key:
                from ..alpaca import PaperBroker

                self.broker = PaperBroker(key, secret)

    def _key(self, source, *names, enabled=None):
        """The environment variables a source needs, or blanks (and a note in the report) if any is unset."""
        values = [os.environ.get(n, "").strip() for n in names]
        on = self.config.source_on(source) if enabled is None else enabled
        if on and not all(values):
            self.health[source]["last_error"] = f"skipped: set {' and '.join(names)} to enable"
        if not (on and all(values)):
            values = [""] * len(names)
        return values[0] if len(names) == 1 else values

    def _call(self, name, fn, *args):
        try:
            result = fn(*args)
        except Exception as exc:  # noqa: BLE001 - any feed can break in any way
            self.health[name]["failed"] += 1
            self.health[name]["last_error"] = f"{type(exc).__name__}: {exc}"[:200]
            return None
        self.health[name]["ok"] += 1
        self.health[name]["items"] += len(result) if hasattr(result, "__len__") else 0
        return result

    def prices(self, ticker, years):
        return self._call("prices", prices.fetch_prices, ticker, years)

    def headlines(self, ticker, now):
        found = []
        if self.config.source_on("yahoo_rss"):
            found += self._call("yahoo_rss", news.yahoo_headlines, ticker) or []
        if self.config.source_on("google_news"):
            found += self._call("google_news", news.google_headlines, ticker) or []
        if self.finnhub_key:
            found += self._call("finnhub", news.finnhub_headlines, ticker, self.finnhub_key, now) or []
        return found

    def finbert(self, texts):
        """FinBERT scores for `texts`, or None if FinBERT is off or can't run here."""
        if not texts or not self.config.source_on("finbert") or self.health["finbert"]["last_error"].startswith("skipped"):
            return None
        if importlib.util.find_spec("transformers") is None:
            self.health["finbert"]["last_error"] = "skipped: install requirements-finbert.txt to enable"
            return None
        from .. import sentiment

        return self._call("finbert", sentiment.finbert_scores, texts)

    def filing_dates(self, ticker):
        if self.edgar is None:
            return None
        return self._call("sec_filings", self.edgar.filing_dates, ticker)

    def earnings(self, ticker):
        return self._call("earnings", events.earnings_events, ticker) if self.config.source_on("earnings") else None

    def analysts(self, ticker):
        return self._call("analysts", events.analyst_actions, ticker) if self.config.source_on("analysts") else None

    def macro(self, years):
        if not self.config.source_on("fred"):
            return None
        data = self._call("fred", macro.fetch_fred, years, os.environ.get("FRED_API_KEY", "").strip())
        return data if data is not None else self._call("macro_yahoo", macro.fetch_yahoo, years)

    def options(self, ticker, now, spot):
        return self._call("options", options.options_snapshot, ticker, now, spot) if self.config.source_on("options") else None

    def social(self, ticker, now):
        """Posts from every social source that worked, or None if none did (unknown, not silence)."""
        found = []
        if self.config.source_on("stocktwits"):
            found.append(self._call("stocktwits", social.stocktwits_posts, ticker))
        if self.reddit:
            found.append(self._call("reddit", self.reddit.posts, ticker))
        working = [posts for posts in found if posts is not None]
        return [p for posts in working for p in posts] if working else None
