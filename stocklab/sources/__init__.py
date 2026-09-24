"""Every data source behind one interface. A failing source is recorded and skipped, never fatal,
because RSS feeds and free APIs change without notice."""
import os
from collections import defaultdict

from . import filings, news, prices


class LiveSources:
    def __init__(self, config):
        self.config = config
        self.health = defaultdict(lambda: {"ok": 0, "failed": 0, "items": 0, "last_error": ""})
        self.finnhub_key = os.environ.get("FINNHUB_API_KEY", "").strip()
        sec_agent = os.environ.get("SEC_USER_AGENT", "").strip()
        self.edgar = filings.EdgarClient(sec_agent) if sec_agent and config.source_on("sec_filings") else None
        if config.source_on("sec_filings") and not sec_agent:
            self.health["sec_filings"]["last_error"] = "skipped: set SEC_USER_AGENT to enable"
        if config.source_on("finnhub") and not self.finnhub_key:
            self.health["finnhub"]["last_error"] = "skipped: set FINNHUB_API_KEY to enable"

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
        if self.config.source_on("finnhub") and self.finnhub_key:
            found += self._call("finnhub", news.finnhub_headlines, ticker, self.finnhub_key, now) or []
        return found

    def filing_dates(self, ticker):
        if self.edgar is None:
            return None
        return self._call("sec_filings", self.edgar.filing_dates, ticker)
