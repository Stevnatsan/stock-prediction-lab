"""python -m stocklab daily                          fetch, score yesterday, learn, predict the next session, publish
python -m stocklab report                         rebuild the report from saved state without fetching anything
python -m stocklab watchlist --add "KO" --remove TSLA   change which stocks are predicted
python -m stocklab catalogue                      refresh the S&P 500 list (catalogue/sp500.csv, STOCKS.md)"""
import argparse
import json
from datetime import datetime, timezone

from .config import ROOT, load_config


def main():
    parser = argparse.ArgumentParser(prog="stocklab", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["daily", "report", "watchlist", "catalogue"], nargs="?", default="daily")
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

    if args.command == "daily":
        from .pipeline import run_daily
        from .sources import LiveSources

        sources = LiveSources(config)
        summary = run_daily(config, sources, ROOT / "state", ROOT / "reports", ROOT / "README.md")
        print(json.dumps({"sources": sources.health, "stocks": summary}, indent=1, default=str))
    else:
        from .report import build_report
        from .state import State

        build_report(State.load(ROOT / "state", config), config, ROOT / "reports", ROOT / "README.md",
                     datetime.now(timezone.utc), {}, {})


if __name__ == "__main__":
    main()
