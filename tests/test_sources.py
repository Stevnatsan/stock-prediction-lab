"""The live sources can't be reached from CI reliably, so their parsing is tested against canned responses."""
from datetime import datetime, timezone

import numpy as np
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


def test_earnings_dates_are_normalised():
    from stocklab.sources import events

    idx = pd.DatetimeIndex(["2026-04-30 16:30", "2026-01-29 00:00", "2025-10-30 16:30"], tz="America/New_York")
    raw = pd.DataFrame({"EPS Estimate": [1.6, 2.3, 1.7], "Reported EPS": [None, 2.4, 1.8], "Surprise(%)": [None, 4.3, 5.9]}, index=idx)
    e = events.normalise_earnings(raw)
    assert list(e["released"].dt.strftime("%Y-%m-%d %H:%M")) == ["2025-10-30 16:30", "2026-01-29 16:00", "2026-04-30 16:30"]
    assert np.isnan(e["surprise"].iloc[-1]) and e["surprise"].iloc[1] == 4.3


def test_analyst_actions_are_normalised():
    from stocklab.sources import events

    idx = pd.DatetimeIndex(["2026-03-03 11:00", "2026-03-02 09:00"], tz="UTC", name="GradeDate")
    raw = pd.DataFrame({"Firm": ["A", "B"], "ToGrade": ["Buy", "Sell"], "FromGrade": ["Hold", "Hold"], "Action": ["up", "down"],
                        "currentPriceTarget": [220.0, 0.0], "priorPriceTarget": [200.0, 180.0]}, index=idx)
    a = events.normalise_analysts(raw)
    assert list(a["rating"]) == [-1.0, 1.0]
    assert np.isnan(a["target"].iloc[0]) and np.isclose(a["target"].iloc[1], np.log(1.1))
    assert a["time"].iloc[1] == pd.Timestamp("2026-03-03 06:00")  # converted to New York time


def test_fred_csv_is_parsed():
    from stocklab.sources import macro

    s = macro.parse_fred_csv("observation_date,VIXCLS\n2026-03-02,18.5\n2026-03-03,.\n2026-03-04,\n", "VIXCLS")
    assert s.iloc[0] == 18.5 and s.iloc[1:].isna().all()


def test_option_chain_summary():
    from stocklab.sources import options

    calls = pd.DataFrame({"strike": [95.0, 100.0, 105.0], "impliedVolatility": [0.30, 0.25, 0.28], "volume": [10, 100, np.nan]})
    puts = pd.DataFrame({"strike": [95.0, 100.0, 105.0], "impliedVolatility": [0.33, 0.27, 0.0001], "volume": [50, 49, 0]})
    s = options.summarise_chain(calls, puts, spot=101.0)
    assert np.isclose(s["iv_atm"], 0.26) and np.isclose(s["put_call"], np.log(100 / 111))


def test_stocktwits_and_reddit_posts(monkeypatch):
    from stocklab.sources import social

    twits = {"messages": [{"created_at": "2026-03-02T20:15:00Z", "entities": {"sentiment": {"basic": "Bullish"}}},
                          {"created_at": "2026-03-02T19:00:00Z", "entities": {"sentiment": None}}]}
    monkeypatch.setattr(social.requests, "get", lambda url, **kw: FakeResponse(payload=twits))
    posts = social.stocktwits_posts("BRK-B")
    assert [p["mood"] for p in posts] == [1.0, None]

    reddit = {"data": {"children": [{"data": {"title": "$AAPL beats earnings, stock surges", "created_utc": 1772481600}},
                                    {"data": {"title": "Pineapple prices crash", "created_utc": 1772481600}}]}}
    monkeypatch.setattr(social.requests, "post", lambda url, **kw: FakeResponse(payload={"access_token": "t"}))
    monkeypatch.setattr(social.requests, "get", lambda url, **kw: FakeResponse(payload=reddit))
    posts = social.RedditClient("id", "secret").posts("AAPL")
    assert len(posts) == 1 and posts[0]["mood"] > 0


def test_optional_sources_are_skipped_without_keys(monkeypatch):
    for name in ("REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "ALPACA_API_KEY", "ALPACA_SECRET_KEY"):
        monkeypatch.delenv(name, raising=False)
    live = LiveSources(Config(tickers=["AAPL"], sources={"reddit": True, "finbert": False}, paper_orders={"enabled": True}))
    assert live.reddit is None and live.broker is None
    assert "REDDIT_CLIENT_ID" in live.health["reddit"]["last_error"]
    assert "ALPACA_API_KEY" in live.health["alpaca"]["last_error"]
    assert live.finbert(["Apple beats"]) is None and live.social("AAPL", None) is None
