"""python -m stocklab check [TICKER]: call every data source once and print what came back, so you can
confirm new API keys work without waiting for (or changing) a daily run. Nothing is saved."""
import re
from datetime import datetime, timezone

import numpy as np

from .features import score_headlines
from .sources import LiveSources


def run_checks(config, ticker="AAPL", now=None):
    now = now or datetime.now(timezone.utc)
    if not re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,9}", ticker):
        return [f"{ticker!r} doesn't look like a stock symbol."]
    s = LiveSources(config)
    lines = []

    def report(name, value, describe):
        h = s.health.get(name, {})
        if value is None:
            lines.append(f"  --  {name:<13} {h.get('last_error') or 'off in config.yaml'}")
        else:
            lines.append(f"  ok  {name:<13} {describe(value)}")

    prices = s.prices(ticker, 1)
    report("prices", prices, lambda p: f"{len(p)} daily bars, last {p.index[-1].date()} close {p['close'].iloc[-1]:.2f}")
    report("sec_filings", s.filing_dates(ticker), lambda d: f"{len(d)} 8-K filings, latest {d[-1] if d else '–'}")
    report("earnings", s.earnings(ticker), lambda e: f"{len(e)} reports, latest {e['released'].iloc[-1]:%Y-%m-%d %H:%M}")
    report("analysts", s.analysts(ticker), lambda a: f"{len(a)} actions, latest {a['time'].iloc[-1]:%Y-%m-%d}, "
                                                   f"{int(np.isfinite(a['target']).sum())} with a price-target change")
    report("fred", s.macro(1), lambda m: f"through {m.index[-1].date()}: VIX {m['vix'].dropna().iloc[-1]:.1f}, "
                                        f"10-year {m['rate_10y'].dropna().iloc[-1]:.2f}%, curve {m['curve'].dropna().iloc[-1]:+.2f}")
    spot = float(prices["close"].iloc[-1]) if prices is not None else 100.0
    report("options", s.options(ticker, now, spot), lambda o: f"at-the-money implied volatility {o['iv_atm']:.1%}, "
                                                            f"log put/call volume {o['put_call']:+.2f}")
    headlines = score_headlines(s.headlines(ticker, now))
    for name in ("yahoo_rss", "google_news", "finnhub"):
        count = sum(h["source"] == name for h in headlines)
        report(name, count if s.health.get(name, {}).get("ok") else None, lambda n: f"{n} headlines")
    sample = headlines[:5]
    finbert = s.finbert([h["title"] for h in sample])
    report("finbert", finbert, lambda f: f"scored {len(f)} headlines")
    for h, fb in zip(sample, finbert or [None] * len(sample)):
        lines.append(f"        VADER {h['score']:+.2f}  FinBERT {'  –  ' if fb is None else f'{fb:+.2f}'}  {h['title'][:80]}")
    posts = s.social(ticker, now)
    for name in ("stocktwits", "reddit"):
        count = sum(p["source"] == name for p in posts or [])
        report(name, count if s.health.get(name, {}).get("ok") else None, lambda n: f"{n} recent posts")
    if s.broker is not None:
        try:
            account, clock = s.broker.account(), s.broker.clock()
            lines.append(f"  ok  {'alpaca':<13} paper account equity ${float(account['equity']):,.2f}, "
                         f"market {'open' if clock['is_open'] else 'closed'}, next open {clock['next_open']}")
        except Exception as exc:  # noqa: BLE001
            lines.append(f"  --  {'alpaca':<13} {type(exc).__name__}: {exc}"[:200])
    else:
        report("alpaca", None, str)
    return [f"Checking every source with {ticker}:"] + lines
