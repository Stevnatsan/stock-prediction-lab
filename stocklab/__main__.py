"""python -m stocklab daily                          fetch, score yesterday, learn, predict the next session, publish
python -m stocklab report                         rebuild the report from saved state without fetching anything
python -m stocklab watchlist --add "KO" --remove TSLA   change which stocks are predicted
python -m stocklab catalogue                      refresh the S&P 500 list (catalogue/sp500.csv, STOCKS.md)
python -m stocklab check [TICKER]                 call every data source once and show what came back
python -m stocklab insight [TICKERS]              plain-language brief (reports/insight.md) and phone page (docs/index.html)
python -m stocklab orders open|close              send the champion's picks to an Alpaca paper account (needs
                                                  ALPACA_API_KEY and ALPACA_SECRET_KEY)"""
import argparse
import json
import os
from datetime import datetime, timezone

from .config import ROOT, load_config


def main():
    parser = argparse.ArgumentParser(prog="stocklab", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["daily", "report", "watchlist", "catalogue", "orders", "check", "insight"], nargs="?", default="daily")
    parser.add_argument("step", nargs="?", help="orders: open or close; check: the ticker to try (default AAPL); insight: tickers, comma-separated")
    parser.add_argument("--add", default="", help="symbols to add, e.g. \"KO, PEP\"")
    parser.add_argument("--remove", default="", help="symbols to remove")
    args = parser.parse_args()
    if args.command == "catalogue":
        from . import catalogue

        print(f"{len(catalogue.refresh())} companies written to catalogue/sp500.csv and STOCKS.md")
        return
    if args.command == "watchlist":
        from . import watchlist

        try:
            tickers, notes = watchlist.update(args.add, args.remove)
        except ValueError as exc:
            raise SystemExit(f"Watchlist not changed: {exc}")
        for note in notes:
            print("note:", note)
        print(f"Watchlist ({len(tickers)}): {', '.join(tickers)}")
        return
    config = load_config()
    if args.command == "check":
        from .check import run_checks

        print("\n".join(run_checks(config, (args.step or "AAPL").upper())))
        return
    if args.command == "insight":
        from . import insight, site, weekly
        from .sources import LiveSources
        from .state import State

        tickers = [t.strip().upper() for t in (args.step or ",".join(config.tickers)).split(",") if t.strip()]
        sources, now = LiveSources(config), datetime.now(timezone.utc)
        state = State.load(ROOT / "state", config)
        market = sources.prices(config.market, config.history_years)
        prices = {t: sources.prices(t, config.history_years) for t in tickers}
        events = {t: {"earnings": sources.earnings(t), "analysts": sources.analysts(t)} for t in tickers}
        brief = insight.build(prices, market, state, now, tickers, events)
        if market is not None:
            from .features import build_frame
            from .sources.prices import drop_unfinished_session

            market = drop_unfinished_session(market, now)
            macro = sources.macro(config.history_years)
            frames = {t: build_frame(drop_unfinished_session(p, now), market, {**events[t],
                                                                               "filings": sources.filing_dates(t), "macro": macro})
                      for t, p in prices.items() if p is not None}
            brief["weekly"] = weekly.run(frames, {t: drop_unfinished_session(p, now) for t, p in prices.items() if p is not None},
                                         market, ROOT / "state", now, save=False)
        insight.write(brief, ROOT / "reports")
        site.write(brief, state, config, now)
        print(insight.to_markdown(brief))
        missing = [t for t in tickers if t not in brief["stocks"]]
        if missing:
            raise SystemExit(f"No price data for {', '.join(missing)}: {sources.health['prices']['last_error']}")
        return
    if args.command == "orders":
        from . import alpaca

        key, secret = os.environ.get("ALPACA_API_KEY", "").strip(), os.environ.get("ALPACA_SECRET_KEY", "").strip()
        if not (key and secret) or not config.paper_orders.get("enabled"):
            print("Paper orders are off: set paper_orders.enabled in config.yaml and the ALPACA_API_KEY and "
                  "ALPACA_SECRET_KEY secrets to turn them on.")
            return
        if args.step not in ("open", "close"):
            raise SystemExit("Say which step: python -m stocklab orders open|close")
        broker, now = alpaca.PaperBroker(key, secret), datetime.now(timezone.utc)
        notes = alpaca.open_orders(broker, ROOT / "state", config, now) if args.step == "open" else alpaca.close_orders(broker, now)
        print("\n".join(notes))
        return

    if args.command == "daily":
        from .pipeline import run_daily
        from .sources import LiveSources

        sources = LiveSources(config)
        summary = run_daily(config, sources, ROOT / "state", ROOT / "reports", ROOT / "README.md", docs_dir=ROOT / "docs")
        print(json.dumps({"sources": sources.health, "stocks": summary}, indent=1, default=str))
    else:
        from .report import build_report
        from .state import State

        build_report(State.load(ROOT / "state", config), config, ROOT / "reports", ROOT / "README.md",
                     datetime.now(timezone.utc), {}, {})


if __name__ == "__main__":
    main()
