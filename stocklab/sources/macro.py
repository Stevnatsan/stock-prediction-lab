"""Macro data from FRED, the St. Louis Fed's free database. The CSV download needs no API key."""
import io
from datetime import date, timedelta

import pandas as pd
import requests

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}"
SERIES = {"VIXCLS": "vix", "DGS10": "rate_10y", "T10Y2Y": "curve"}


def parse_fred_csv(text, series):
    df = pd.read_csv(io.StringIO(text), na_values=[".", ""])
    values = pd.to_numeric(df[series], errors="coerce")
    return pd.Series(values.to_numpy(float), index=pd.DatetimeIndex(pd.to_datetime(df.iloc[:, 0]), name="date"))


def fetch_macro(years):
    start = (date.today() - timedelta(days=int(365.25 * years) + 200)).isoformat()
    columns = {}
    for series, name in SERIES.items():
        response = requests.get(FRED_CSV.format(series=series, start=start), timeout=30,
                                headers={"User-Agent": "stock-prediction-lab"})
        response.raise_for_status()
        columns[name] = parse_fred_csv(response.text, series)
    return pd.DataFrame(columns).dropna(how="all")
