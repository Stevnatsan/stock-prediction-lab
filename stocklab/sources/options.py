"""What the options market expects, from Yahoo Finance's option chains (via yfinance). Only today's
chain is available, so these features are collected live and saved from then on."""
from datetime import date

import numpy as np

from .prices import NEW_YORK

MIN_DAYS = 7  # the nearest weekly expiries are dominated by noise; use the first one at least a week out


def options_snapshot(ticker, now, spot):
    import yfinance as yf

    t = yf.Ticker(ticker)
    today = now.astimezone(NEW_YORK).date()
    expiry = next((e for e in t.options if (date.fromisoformat(e) - today).days >= MIN_DAYS), None)
    if expiry is None:
        raise ValueError("no option expiry at least a week out")
    chain = t.option_chain(expiry)
    return summarise_chain(chain.calls, chain.puts, spot)


def _atm_iv(side, spot):
    side = side[(side["impliedVolatility"] > 0.01) & side["strike"].notna()]
    if side.empty:
        return np.nan
    return float(side.iloc[int((side["strike"] - spot).abs().to_numpy().argmin())]["impliedVolatility"])


def summarise_chain(calls, puts, spot):
    """At-the-money implied volatility (average of the call and put nearest the price) and the
    put/call volume ratio."""
    ivs = [v for v in (_atm_iv(calls, spot), _atm_iv(puts, spot)) if np.isfinite(v)]
    put_volume, call_volume = puts["volume"].fillna(0).sum(), calls["volume"].fillna(0).sum()
    return {"iv_atm": float(np.mean(ivs)) if ivs else np.nan,
            "put_call": float(np.log((put_volume + 1) / (call_volume + 1)))}
