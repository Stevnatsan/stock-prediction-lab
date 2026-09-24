"""Add or remove stocks from the watchlist in config.yaml.

    python -m stocklab watchlist --add "KO, PEP" --remove TSLA
"""
import re

import yaml

from . import catalogue
from .config import ROOT

MAX_STOCKS = 40  # each stock means more downloads and headlines on every run
SYMBOL = re.compile(r"^[A-Z][A-Z0-9-]{0,9}$")
TICKERS_LINE = re.compile(r"^tickers:.*$", re.M)


def parse(text):
    """'aapl, brk.b  msft' -> ['AAPL', 'BRK-B', 'MSFT']"""
    return [catalogue.yahoo_symbol(s) for s in re.split(r"[\s,;]+", text or "") if s.strip()]


def update(add="", remove="", config_path=ROOT / "config.yaml", known=None):
    """Returns (new watchlist, notes). Raises ValueError for anything that can't be applied."""
    text = config_path.read_text()
    current = [t.upper() for t in yaml.safe_load(text)["tickers"]]
    to_add, to_remove = parse(add), set(parse(remove))
    bad = [s for s in to_add + sorted(to_remove) if not SYMBOL.match(s)]
    if bad:
        raise ValueError(f"Not valid stock symbols: {', '.join(bad)}")
    if known is None:
        known = {r["symbol"] for r in catalogue.load()}
    notes = [f"{s} is not in the S&P 500 list; it will be tried on Yahoo Finance anyway." for s in to_add if s not in known]
    notes += [f"{s} was not on the watchlist." for s in sorted(to_remove) if s not in current]
    result = [t for t in current if t not in to_remove]
    result += [s for s in dict.fromkeys(to_add) if s not in result]
    if not result:
        raise ValueError("The watchlist can't be empty.")
    if len(result) > MAX_STOCKS:
        raise ValueError(f"That would make {len(result)} stocks; the limit is {MAX_STOCKS}.")
    config_path.write_text(TICKERS_LINE.sub(f"tickers: [{', '.join(result)}]", text, count=1))
    return result, notes
