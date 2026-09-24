"""Paper orders, against a fake of Alpaca's paper-trading API (the real one needs an account)."""
from datetime import datetime, timezone

import pandas as pd
import pytest

from stocklab import alpaca
from stocklab.state import State


class Response:
    def __init__(self, payload=None, status=200):
        self.payload, self.status_code, self.text = payload, status, str(payload)

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(self.status_code)

    def json(self):
        return self.payload


class FakeAlpaca:
    """Just enough of the API: a clock, a calendar, positions, and orders that fill when told to."""

    def __init__(self, is_open, next_open, positions=None, orders=None):
        self.clock = {"is_open": is_open, "next_open": next_open}
        self.positions = positions or []
        self.orders = orders or []
        self.submitted = []

    def get(self, url, params=None, headers=None, timeout=None):
        assert url.startswith("https://paper-api.alpaca.markets/") and headers["APCA-API-KEY-ID"] == "key"
        path = url.split(".markets")[1]
        if path == "/v2/clock":
            return Response(self.clock)
        if path == "/v2/calendar":
            return Response([{"date": d} for d in ("2026-03-05", "2026-03-06", "2026-03-09")])
        if path == "/v2/positions":
            return Response(self.positions)
        if path == "/v2/orders":
            return Response(self.orders)
        raise AssertionError(path)

    def post(self, url, json=None, headers=None, timeout=None):
        if any(o["client_order_id"] == json["client_order_id"] for o in self.orders + self.submitted):
            return Response({"message": "client_order_id must be unique"}, status=422)
        self.submitted.append(json)
        return Response({"id": "x", **json})


MONDAY_MORNING = datetime(2026, 3, 9, 12, 45, tzinfo=timezone.utc)   # 8:45 in New York
MONDAY_AFTERNOON = datetime(2026, 3, 9, 19, 5, tzinfo=timezone.utc)


def _pending(close=250.0):
    rows = []
    for ticker, p in (("AAA", 0.61), ("BBB", 0.57), ("CCC", 0.53), ("DDD", 0.58), ("BRK-B", 0.50)):
        for variant in ("full", "gbm"):
            rows.append({"ticker": ticker, "variant": variant, "feature_date": "2026-03-06", "close": close,
                         "p_up": p if variant == "full" else 1 - p})
    return rows


def _state(tmp_path, config, pending):
    state = State(tmp_path, config)
    state.pending = pending
    state.save()
    return tmp_path


def test_top_picks_are_bought_at_the_open(tmp_path, config):
    config.decision_threshold = 0.55
    api = FakeAlpaca(False, "2026-03-09T09:30:00-04:00")
    notes = alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), _state(tmp_path, config, _pending()), config, MONDAY_MORNING)
    orders = api.submitted
    assert [o["symbol"] for o in orders] == ["AAA", "DDD", "BBB"]  # champion ("full" with no history) order, all >= 55%
    assert all(o["side"] == "buy" and o["time_in_force"] == "opg" and o["qty"] == "40" for o in orders)
    assert orders[0]["client_order_id"] == "stocklab-2026-03-09-AAA-buy"
    assert len(notes) == 3
    # a second run the same morning changes nothing
    alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), tmp_path, config, MONDAY_MORNING)
    api.orders, api.submitted = api.submitted, []
    alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), tmp_path, config, MONDAY_MORNING)
    assert api.submitted == []


@pytest.mark.parametrize("is_open,next_open,expected", [
    (True, "2026-03-10T09:30:00-04:00", "already open"),
    (False, "2026-03-10T09:30:00-04:00", "No session today"),
])
def test_no_orders_when_the_market_is_open_or_closed_today(tmp_path, config, is_open, next_open, expected):
    api = FakeAlpaca(is_open, next_open)
    notes = alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), _state(tmp_path, config, _pending()), config, MONDAY_MORNING)
    assert api.submitted == [] and expected in notes[0]


def test_stale_calls_and_weak_calls_are_not_traded(tmp_path, config):
    api = FakeAlpaca(False, "2026-03-09T09:30:00-04:00")
    old = [dict(p, feature_date="2026-03-05") for p in _pending()]
    notes = alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), _state(tmp_path, config, old), config, MONDAY_MORNING)
    assert api.submitted == [] and "No calls from the 2026-03-06 close" in notes[-1]
    config.decision_threshold = 0.9
    notes = alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), _state(tmp_path, config, _pending()), config, MONDAY_MORNING)
    assert api.submitted == [] and "staying in cash" in notes[-1]


def _order(cid, side, filled, price, status="filled"):
    return {"client_order_id": cid, "side": side, "filled_qty": str(filled), "filled_avg_price": str(price), "status": status}


def test_todays_buys_are_sold_at_the_close(tmp_path, config):
    api = FakeAlpaca(True, "2026-03-10T09:30:00-04:00", positions=[{"symbol": "AAA", "qty": "40"}, {"symbol": "BRK.B", "qty": "3"}],
                     orders=[_order("stocklab-2026-03-09-AAA-buy", "buy", 40, 250.1),
                             _order("stocklab-2026-03-09-BRK-B-buy", "buy", 3, 480.0),
                             _order("manual-order", "buy", 5, 10.0)])
    alpaca.close_orders(alpaca.PaperBroker("key", "secret", api), MONDAY_AFTERNOON)
    assert [(o["symbol"], o["qty"], o["side"], o["time_in_force"]) for o in api.submitted] == [
        ("AAA", "40", "sell", "cls"), ("BRK.B", "3", "sell", "cls")]
    assert api.submitted[1]["client_order_id"] == "stocklab-2026-03-09-BRK-B-sell"


def test_leftovers_from_a_missed_close_are_sold_at_the_next_open(tmp_path, config):
    api = FakeAlpaca(False, "2026-03-09T09:30:00-04:00", positions=[{"symbol": "AAA", "qty": "40"}],
                     orders=[_order("stocklab-2026-03-06-AAA-buy", "buy", 40, 250.0)])
    config.decision_threshold = 0.99
    notes = alpaca.open_orders(alpaca.PaperBroker("key", "secret", api), _state(tmp_path, config, _pending()), config, MONDAY_MORNING)
    assert [(o["symbol"], o["side"], o["time_in_force"], o["client_order_id"]) for o in api.submitted] == [
        ("AAA", "sell", "opg", "stocklab-2026-03-06-AAA-exit")]
    assert "still held" in notes[0]


def test_real_fills_are_recorded(tmp_path, config):
    api = FakeAlpaca(False, "2026-03-10T09:30:00-04:00", orders=[
        _order("stocklab-2026-03-09-AAA-buy", "buy", 40, 250.0), _order("stocklab-2026-03-09-AAA-sell", "sell", 40, 252.5),
        _order("stocklab-2026-03-09-BBB-buy", "buy", 0, "", status="canceled")])
    orders = alpaca.sync(alpaca.PaperBroker("key", "secret", api), tmp_path, MONDAY_AFTERNOON)
    saved = pd.read_csv(tmp_path / "orders.csv").set_index("ticker")
    assert saved.at["AAA", "trade_return"] == pytest.approx(0.01) and saved.at["AAA", "sell_status"] == "filled"
    assert saved.at["BBB", "buy_status"] == "canceled" and pd.isna(saved.at["BBB", "trade_return"])
    assert len(orders) == 2
