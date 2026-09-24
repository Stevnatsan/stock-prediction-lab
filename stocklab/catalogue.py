"""The list of stocks you can choose from: every S&P 500 company, grouped by sector.

    python -m stocklab catalogue     # refresh catalogue/sp500.csv and STOCKS.md
"""
import csv
import io
from collections import defaultdict

import requests

from .config import ROOT

SOURCE = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
CSV_PATH = ROOT / "catalogue" / "sp500.csv"
MARKDOWN_PATH = ROOT / "STOCKS.md"


def yahoo_symbol(symbol):
    """Yahoo writes share classes with a dash: BRK.B -> BRK-B."""
    return symbol.strip().upper().replace(".", "-")


def load(path=CSV_PATH):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def refresh():
    response = requests.get(SOURCE, timeout=30)
    response.raise_for_status()
    rows = [{"symbol": yahoo_symbol(r["Symbol"]), "name": r["Security"].strip(), "sector": r["GICS Sector"].strip(),
             "industry": r["GICS Sub-Industry"].strip()} for r in csv.DictReader(io.StringIO(response.text))]
    rows.sort(key=lambda r: (r["sector"], r["symbol"]))
    CSV_PATH.parent.mkdir(exist_ok=True)
    with open(CSV_PATH, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["symbol", "name", "sector", "industry"])
        writer.writeheader()
        writer.writerows(rows)
    write_markdown(rows)
    return rows


def write_markdown(rows):
    by_sector = defaultdict(list)
    for r in rows:
        by_sector[r["sector"]].append(r)
    lines = ["# Stocks you can choose", "",
             f"All {len(rows)} companies in the S&P 500, the index of the largest US companies, grouped by sector.",
             "Add any of them to the watchlist with the **choose stocks** workflow (see the [README](README.md#choose-your-stocks)).",
             "Symbols are in Yahoo Finance format, so share classes use a dash (`BRK-B`).", ""]
    for sector in sorted(by_sector):
        items = by_sector[sector]
        lines += [f"<details><summary><b>{sector}</b> ({len(items)})</summary>", "", "| Symbol | Company | Industry |", "|---|---|---|"]
        lines += [f"| `{r['symbol']}` | {r['name']} | {r['industry']} |" for r in items]
        lines += ["", "</details>", ""]
    MARKDOWN_PATH.write_text("\n".join(lines))
