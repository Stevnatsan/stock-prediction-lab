"""python -m stocklab daily    fetch data, score yesterday, learn, predict the next session, publish
python -m stocklab report   rebuild the report from saved state without fetching anything"""
import argparse
import json
from datetime import datetime, timezone

from .config import ROOT, load_config


def main():
    parser = argparse.ArgumentParser(prog="stocklab", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["daily", "report"], nargs="?", default="daily")
    args = parser.parse_args()
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
