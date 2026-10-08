import json
from datetime import timedelta

import numpy as np
import pandas as pd

from stocklab import news, site
from stocklab.pipeline import run_daily
from stocklab.sources.news import headline_id
from stocklab.state import State

from conftest import FakeSources, evening_after, synthetic_prices

NOW = pd.Timestamp("2026-10-08 22:30", tz="UTC")


def _item(title, hours_ago, finbert=0.0, source="google_news", link=""):
    return {"id": headline_id(title), "title": title, "published": (NOW - timedelta(hours=hours_ago)).isoformat(),
            "source": source, "link": link, "score": 0.0, "finbert": finbert}


def _store(root, ticker, items):
    (root / "news").mkdir(parents=True, exist_ok=True)
    (root / "news" / f"{ticker}.jsonl").write_text("".join(json.dumps(h) + "\n" for h in items))


def test_publishers_are_read_from_the_title_or_the_link():
    assert news.split_title({"title": "Nvidia hits a record - Reuters"}) == ("Nvidia hits a record", "Reuters")
    assert news.split_title({"title": "Nvidia hits a record", "link": "https://www.cnbc.com/2026/x.html"}) == ("Nvidia hits a record", "cnbc.com")
    assert news.outlet("Reuters") == "Reuters" and news.outlet("cnbc.com") == "CNBC" and news.outlet("markets.wsj.com") == "The Wall Street Journal"
    assert news.outlet("The Motley Fool") is None and news.outlet("MarketBeat") is None and news.outlet("The Globe and Mail") is None


def test_only_headlines_naming_the_company_count_once_each():
    words = {"nvda", "nvidia"}
    items = [_item("Nvidia hits a record - Reuters", 5), _item("Nvidia hits a record - Yahoo Finance", 4),
             _item("Dow closes higher as banks rally - CNBC", 3), _item("Why NVDA stock is moving - MarketBeat", 2)]
    kept = [news.split_title(h)[0] for h in news.about(items, words)]
    assert kept == ["Nvidia hits a record", "Why NVDA stock is moving"]


def test_brief_mood_trend_and_reading_list(tmp_path):
    items = [_item("Nvidia slumps on export curbs - Reuters", 200, -0.8),       # last week
             _item("Nvidia falls again - Bloomberg", 190, -0.6),
             _item("Nvidia wins huge order - Reuters", 30, 0.9),                # this week
             _item("Nvidia beats estimates - Reuters", 20, 0.7),
             _item("Nvidia guidance strong - Reuters", 10, 0.5),
             _item("Nvidia: 3 reasons to buy now - The Motley Fool", 8, 0.6),
             _item("NVDA Investor Alert: class action filed against Nvidia - Business Insider", 6, -0.3),
             _item("Nvidia supplier news - CNBC", 4, 0.0)]
    _store(tmp_path, "NVDA", items)
    b = news.brief(tmp_path, "NVDA", NOW, words={"nvda", "nvidia"})
    assert b["week"]["count"] == 6 and b["previous_week"]["count"] == 2
    assert b["week"]["positive"] == 4 and b["week"]["negative"] == 1 and b["trend"] == "improving"
    outlets = [r["outlet"] for r in b["read"]]
    assert outlets == ["CNBC", "Reuters", "Reuters"]  # newest first, at most 2 per outlet, no Motley Fool, no law-firm notice
    assert b["read"][1]["title"] == "Nvidia guidance strong" and b["read"][1]["mood"] == "positive"
    assert b["major_count"] == 4 and len(b["daily"]) == 14


def test_earnings_dates_surprises_and_the_next_day_move():
    events = pd.DataFrame({"released": pd.to_datetime(["2026-05-27 16:20", "2026-08-26 16:20", "2026-11-18 16:00"]),
                           "surprise": [5.0, -2.0, np.nan]})
    days = pd.bdate_range("2026-05-01", "2026-10-08")
    prices = pd.DataFrame({"close": 100.0}, index=days)
    prices.loc["2026-08-27", "close"] = 90.0  # the session after the 26 Aug evening report
    e = news.earnings_info(events, NOW, prices)
    assert e["next"] == "2026-11-18" and e["next_time"] == "after the close" and e["days_until"] == 41
    assert e["last"]["date"] == "2026-08-26" and e["last"]["surprise"] == -2.0
    assert abs(e["last"]["move"] + 0.10) < 1e-9
    assert e["beat_count"] == 1 and e["beat_of"] == 2
    before_open = news.earnings_info(pd.DataFrame({"released": pd.to_datetime(["2026-10-20 07:00"]), "surprise": [np.nan]}), NOW)
    assert before_open["next_time"] == "before the open" and "last" not in before_open


def test_analyst_counts_cover_the_last_30_days():
    actions = pd.DataFrame({"time": pd.to_datetime(["2026-08-01", "2026-09-20", "2026-10-01", "2026-10-05"]),
                            "rating": [1.0, 1.0, 0.0, -1.0], "target": [0.5, np.log(1.1), np.nan, np.log(0.9)]})
    a = news.analyst_info(actions, NOW)
    assert (a["notes"], a["upgrades"], a["downgrades"], a["raised"], a["cut"]) == (3, 1, 1, 1, 1)
    assert abs(a["target_change"] - (np.exp((np.log(1.1) + np.log(0.9)) / 2) - 1)) < 1e-9


def test_the_page_has_a_news_tab(tmp_path, config):
    config.focus = ["BBB"]
    full = {t: synthetic_prices(400, seed=s) for t, s in (("AAA", 1), ("BBB", 2), ("SPY", 3))}
    now = evening_after(full["AAA"].index[-1])
    earnings = pd.DataFrame({"released": [pd.Timestamp(now).tz_localize(None).normalize() + pd.Timedelta(days=20, hours=16)],
                             "surprise": [np.nan]})
    sources = FakeSources(full, {"BBB": [{"id": "x", "title": "BBB wins a big contract - Reuters", "published": (now - timedelta(hours=2)).isoformat(),
                                          "source": "major_news", "link": "https://example.com/bbb"}]},
                          context={"BBB": {"earnings": earnings}})
    run_daily(config, sources, tmp_path / "state", tmp_path / "reports", None, now, docs_dir=tmp_path / "docs")
    page = (tmp_path / "docs" / "index.html").read_text()
    assert 'id="tab-news"' in page and 'id="n-bbb"' in page and "Earnings coming up" in page
    assert "BBB wins a big contract" in page and "in 20 days" in page
    # the models never see the major-newsroom search: their headline count stays where it was
    live = State.load(tmp_path / "state", config).live
    assert live.loc[live["ticker"] == "BBB", "sent_count"].iloc[-1] == 0


def test_an_old_insight_without_news_still_renders(config):
    brief = {"stocks": {"AAA": {"close": 10.0, "returns": {}, "high_1y": 12.0, "low_1y": 8.0}}, "market": None}
    assert "News, mood and earnings dates appear after the next nightly run" in site.news_panel(brief, {}, ["AAA"], [])
