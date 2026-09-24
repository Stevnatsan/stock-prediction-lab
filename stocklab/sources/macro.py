"""Macro data: the VIX, the 10-year Treasury yield and the yield curve (10-year minus 3-month).

From FRED, the St. Louis Fed's free database: through its API when FRED_API_KEY is set (free, the
most reliable), otherwise its CSV download. FRED sometimes doesn't answer cloud servers such as
GitHub's, so the same three series are then taken from Yahoo Finance (^VIX, ^TNX, ^IRX) instead.
"""
import io
from datetime import date, timedelta

import pandas as pd
import requests

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}"
FRED_API = "https://api.stlouisfed.org/fred/series/observations"
SERIES = {"VIXCLS": "vix", "DGS10": "rate_10y", "T10Y3M": "curve"}
COLUMNS = list(SERIES.values())


def _start(years):
    return (date.today() - timedelta(days=int(365.25 * years) + 200)).isoformat()


def parse_fred_csv(text, series):
    df = pd.read_csv(io.StringIO(text), na_values=[".", ""])
    values = pd.to_numeric(df[series], errors="coerce")
    return pd.Series(values.to_numpy(float), index=pd.DatetimeIndex(pd.to_datetime(df.iloc[:, 0]), name="date"))


def parse_fred_api(payload):
    obs = payload["observations"]
    values = pd.to_numeric(pd.Series([o["value"] for o in obs]), errors="coerce")  # "." marks a missing day
    return pd.Series(values.to_numpy(float), index=pd.DatetimeIndex(pd.to_datetime([o["date"] for o in obs]), name="date"))


def fetch_fred(years, api_key=""):
    columns = {}
    for series, name in SERIES.items():
        if api_key:
            params = {"series_id": series, "api_key": api_key, "file_type": "json", "observation_start": _start(years)}
            response = requests.get(FRED_API, params=params, timeout=30)
            response.raise_for_status()
            columns[name] = parse_fred_api(response.json())
        else:
            response = requests.get(FRED_CSV.format(series=series, start=_start(years)), timeout=20,
                                    headers={"User-Agent": "stock-prediction-lab"})
            response.raise_for_status()
            columns[name] = parse_fred_csv(response.text, series)
    return pd.DataFrame(columns)[COLUMNS].dropna(how="all")


def fetch_yahoo(years):
    """The same series from Yahoo Finance: ^VIX, the 10-year yield ^TNX, and ^TNX minus the 13-week bill ^IRX."""
    from .prices import fetch_prices

    close = {symbol: fetch_prices(symbol, years)["close"] for symbol in ("^VIX", "^TNX", "^IRX")}
    return pd.DataFrame({"vix": close["^VIX"], "rate_10y": close["^TNX"], "curve": close["^TNX"] - close["^IRX"]}).dropna(how="all")
