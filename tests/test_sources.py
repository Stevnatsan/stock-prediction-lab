"""The live sources can't be reached from CI reliably, so their parsing is tested against canned responses."""
from datetime import datetime, timezone

import pandas as pd
import pytest

from stocklab.config import Config
from stocklab.sources import LiveSources, filings, news, prices

RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>t</title>
<item><title>Apple  beats estimates as iPhone sales surge</title><link>https://example.com/a</link>
<pubDate>Mon, 02 Mar 2026 20:15:00 GMT</pubDate></item>
<item><title>No date, should be skipped</title><link>https://example.com/b</link></item>
</channel></rss>"""


class FakeResponse:
    def __init__(self, content=b"", payload=None):
        self.content = content
        self.payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self.payload


def test_rss_headlines_are_parsed(monkeypatch):
    monkeypatch.setattr(news.requests, "get", lambda url, **kw: FakeResponse(RSS))
    items = news.yahoo_headlines("AAPL")
    assert len(items) == 1
    assert items[0]["title"] == "Apple beats estimates as iPhone sales surge"
    assert items[0]["published"] == "2026-03-02T20:15:00+00:00"
    assert items[0]["source"] == "yahoo_rss"
    assert items[0]["id"] == news.headline_id("apple beats estimates as iphone sales surge!")


def test_finnhub_headlines_are_parsed(monkeypatch):
    payload = [{"headline": "Microsoft raises guidance", "datetime": 1772481600, "url": "https://example.com/m"},
               {"headline": "", "datetime": 1772481600}]
    seen = {}

    def fake_get(url, params=None, timeout=None):
        seen.update(params)
        return FakeResponse(payload=payload)

    monkeypatch.setattr(news.requests, "get", fake_get)
    items = news.finnhub_headlines("MSFT", "key", datetime(2026, 3, 3, tzinfo=timezone.utc))
    assert [i["title"] for i in items] == ["Microsoft raises guidance"]
    assert seen["symbol"] == "MSFT" and seen["from"] == "2026-02-28" and seen["to"] == "2026-03-03"


def test_sec_8k_dates(monkeypatch):
    responses = {
        filings.TICKER_MAP: {"0": {"cik_str": 320193, "ticker": "AAPL", "title": "Apple Inc."}},
        filings.SUBMISSIONS.format(cik=320193): {"filings": {"recent": {
            "form": ["10-Q", "8-K", "4", "8-K"], "filingDate": ["2026-02-01", "2026-02-10", "2026-02-11", "2026-01-05"]}}},
    }
    monkeypatch.setattr(filings.requests, "get", lambda url, headers=None, timeout=None: FakeResponse(payload=responses[url]))
    dates = filings.EdgarClient("Test test@example.com").filing_dates("aapl")
    assert [d.isoformat() for d in dates] == ["2026-01-05", "2026-02-10"]


def test_yfinance_bars_are_normalised(monkeypatch):
    import yfinance

    idx = pd.DatetimeIndex(["2026-03-02 00:00", "2026-03-03 00:00", "2026-03-03 00:00"], tz="America/New_York")
    raw = pd.DataFrame({"Open": [1.0, 2.0, 2.5], "High": [1.2, 2.2, 2.6], "Low": [0.9, 1.9, 2.4], "Close": [1.1, 2.1, 2.55],
                        "Volume": [10, 20, 30], "Dividends": 0.0, "Stock Splits": 0.0}, index=idx)

    class FakeTicker:
        def __init__(self, symbol):
            pass

        def history(self, **kwargs):
            assert kwargs["auto_adjust"] and kwargs["interval"] == "1d"
            return raw

    monkeypatch.setattr(yfinance, "Ticker", FakeTicker)
    bars = prices.fetch_prices("AAPL", 1)
    assert list(bars.columns) == ["open", "high", "low", "close", "volume"]
    assert bars.index.tz is None and list(bars.index.strftime("%Y-%m-%d")) == ["2026-03-02", "2026-03-03"]
    assert bars.loc["2026-03-03", "close"] == 2.55  # duplicate day keeps the latest bar


def test_a_failing_source_is_recorded_not_fatal(monkeypatch):
    def boom(url, **kw):
        raise ConnectionError("feed is down")

    monkeypatch.setattr(news.requests, "get", boom)
    monkeypatch.delenv("FINNHUB_API_KEY", raising=False)
    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    live = LiveSources(Config(tickers=["AAPL"], sources={"yahoo_rss": True, "google_news": True, "finnhub": True, "sec_filings": True}))
    assert live.headlines("AAPL", datetime.now(timezone.utc)) == []
    assert live.health["yahoo_rss"]["failed"] == 1 and "feed is down" in live.health["yahoo_rss"]["last_error"]
    assert "FINNHUB_API_KEY" in live.health["finnhub"]["last_error"]
    assert live.filing_dates("AAPL") is None
    assert "SEC_USER_AGENT" in live.health["sec_filings"]["last_error"]


@pytest.mark.parametrize("ticker", ["AAPL", "BRK-B"])
def test_google_news_query_is_url_encoded(monkeypatch, ticker):
    urls = []
    monkeypatch.setattr(news.requests, "get", lambda url, **kw: urls.append(url) or FakeResponse(RSS))
    news.google_headlines(ticker)
    assert f"q={ticker}+stock" in urls[0]
