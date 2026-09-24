"""Simulated orders with real fills, on an Alpaca *paper-trading* account (fake money, real market prices).

Each trading day:

    before the open   buy the champion's top picks with market-on-open orders (`orders open`)
    before the close  sell them with market-on-close orders (`orders close`)
    after the close   fetch what actually filled, at what price, into state/orders.csv (daily run)

Only the paper endpoint is used, so no real money can ever be touched. Every order carries a client
order id "stocklab-<session>-<ticker>-<buy|sell|exit>", which makes resubmitting harmless (Alpaca
rejects a repeated id) and lets the fills be matched back to the predictions.
"""
import math
from datetime import timedelta

import pandas as pd
import requests

from .sources.prices import NEW_YORK
from .state import State
from .strategy import champion, top_picks

PAPER_URL = "https://paper-api.alpaca.markets"
PREFIX = "stocklab-"
ORDER_COLUMNS = ["session", "ticker", "qty", "buy_price", "sell_price", "trade_return", "buy_status", "sell_status"]


class PaperBroker:
    def __init__(self, key, secret, session=None):
        self.http = session or requests.Session()
        self.headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}

    def _get(self, path, **params):
        response = self.http.get(PAPER_URL + path, params=params, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()

    def clock(self):
        return self._get("/v2/clock")

    def account(self):
        return self._get("/v2/account")

    def calendar(self, start, end):
        return self._get("/v2/calendar", start=start.isoformat(), end=end.isoformat())

    def positions(self):
        return {p["symbol"]: float(p["qty"]) for p in self._get("/v2/positions")}

    def orders(self, after):
        return self._get("/v2/orders", status="all", after=after.isoformat(), limit=500, direction="asc")

    def submit(self, symbol, qty, side, time_in_force, client_order_id):
        """Returns None if accepted, or Alpaca's reason if rejected (e.g. the id was already used)."""
        order = {"symbol": symbol, "qty": str(int(qty)), "side": side, "type": "market",
                 "time_in_force": time_in_force, "client_order_id": client_order_id}
        response = self.http.post(PAPER_URL + "/v2/orders", json=order, headers=self.headers, timeout=30)
        if response.status_code in (403, 409, 422):
            return f"{response.status_code} {response.text[:160]}"
        response.raise_for_status()
        return None


def alpaca_symbol(ticker):
    return ticker.replace("-", ".")  # BRK-B on Yahoo is BRK.B at Alpaca


def order_id(session, ticker, leg):
    return f"{PREFIX}{session}-{ticker}-{leg}"


def trades(orders):
    """Group the bot's orders by (session, ticker) -> {"buy": order, "sell": order, "exit": order}."""
    out = {}
    for o in orders:
        cid = o.get("client_order_id") or ""
        if not cid.startswith(PREFIX):
            continue  # not one of ours (the paper account may also be traded by hand)
        body = cid[len(PREFIX):]
        session, (ticker, leg) = body[:10], body[11:].rsplit("-", 1)
        out.setdefault((session, ticker), {})[leg] = o
    return out


def _filled(order):
    return float(order.get("filled_qty") or 0) if order else 0.0


def _today(now):
    return now.astimezone(NEW_YORK).date()


def open_orders(broker, state_dir, config, now):
    """Before the open: exit anything a missed closing run left behind, then buy tonight's picks at the open."""
    clock = broker.clock()
    today = _today(now)
    if clock["is_open"]:
        return ["The market is already open; opening orders have to go in before 9:28 New York time."]
    if pd.Timestamp(clock["next_open"]).tz_convert(NEW_YORK).date() != today:
        return [f"No session today (next open {clock['next_open']})."]
    sessions = [pd.Timestamp(d["date"]).date() for d in broker.calendar(today - timedelta(days=10), today)]
    previous = max(d for d in sessions if d < today).isoformat()
    notes = []

    held = broker.positions()
    for (session, ticker), legs in trades(broker.orders(now - timedelta(days=10))).items():
        left = _filled(legs.get("buy")) - _filled(legs.get("sell")) - _filled(legs.get("exit"))
        qty = min(left, held.get(alpaca_symbol(ticker), 0))
        if session < today.isoformat() and qty >= 1 and "exit" not in legs:
            reason = broker.submit(alpaca_symbol(ticker), qty, "sell", "opg", order_id(session, ticker, "exit"))
            notes.append(f"{ticker}: {int(qty)} shares from {session} were still held; selling at the open"
                         + (f" (rejected: {reason})" if reason else ""))

    state = State.load(state_dir, config)
    best, _ = champion(state.predictions.dropna(subset=["outcome_up"]), "up")
    tonight = [p for p in state.pending if p["feature_date"] == previous]
    picks = top_picks(tonight, best, config.decision_threshold)
    if not tonight:
        return notes + [f"No calls from the {previous} close, so nothing to buy."]
    if not picks:
        return notes + [f"No stock reached P(up) >= {config.decision_threshold:.0%}; staying in cash."]
    budget = float(config.paper_orders.get("budget_per_stock", 10000))
    for pick in picks:
        qty = math.floor(budget / pick["close"]) if pick.get("close") else 0
        if qty < 1:
            notes.append(f"{pick['ticker']}: one share costs more than the budget, skipped")
            continue
        reason = broker.submit(alpaca_symbol(pick["ticker"]), qty, "buy", "opg", order_id(today, pick["ticker"], "buy"))
        notes.append(f"{pick['ticker']}: buy {qty} at the open, P(up) {pick['p_up']:.1%} ({best})"
                     + (f" (rejected: {reason})" if reason else ""))
    return notes


def close_orders(broker, now):
    """Before the close: sell whatever this morning's orders bought, at the closing price."""
    if not broker.clock()["is_open"]:
        return ["The market isn't open right now, so there is nothing to close."]
    today = _today(now).isoformat()
    held = broker.positions()
    notes = []
    for (session, ticker), legs in trades(broker.orders(now - timedelta(days=2))).items():
        qty = min(_filled(legs.get("buy")), held.get(alpaca_symbol(ticker), 0))
        if session != today or "sell" in legs or qty < 1:
            continue
        reason = broker.submit(alpaca_symbol(ticker), qty, "sell", "cls", order_id(session, ticker, "sell"))
        notes.append(f"{ticker}: sell {int(qty)} at the close" + (f" (rejected: {reason})" if reason else ""))
    return notes or ["Nothing was bought today, so nothing to sell."]


def sync(broker, state_dir, now, days=45):
    """Record the real fills of the bot's recent orders in state/orders.csv."""
    rows = []
    for (session, ticker), legs in trades(broker.orders(now - timedelta(days=days))).items():
        buy, sell = legs.get("buy"), legs.get("sell") or legs.get("exit")
        buy_price = float(buy["filled_avg_price"]) if buy and buy.get("filled_avg_price") else None
        sell_price = float(sell["filled_avg_price"]) if sell and sell.get("filled_avg_price") else None
        rows.append({"session": session, "ticker": ticker, "qty": _filled(buy), "buy_price": buy_price,
                     "sell_price": sell_price, "trade_return": sell_price / buy_price - 1 if buy_price and sell_price else None,
                     "buy_status": buy.get("status") if buy else None, "sell_status": sell.get("status") if sell else None})
    path = state_dir / "orders.csv"
    old = pd.read_csv(path) if path.exists() and path.stat().st_size else pd.DataFrame(columns=ORDER_COLUMNS)
    new = pd.DataFrame(rows, columns=ORDER_COLUMNS)
    merged = new if old.empty else pd.concat([old, new]).drop_duplicates(["session", "ticker"], keep="last")
    if len(merged):
        merged.sort_values(["session", "ticker"]).to_csv(path, index=False, float_format="%.6g")
    return merged
