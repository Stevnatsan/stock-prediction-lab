"""The tests that make the accuracy numbers trustworthy."""
import numpy as np
import pandas as pd

from stocklab import engine
from stocklab.features import PRICE_FEATURES, VARIANTS, build_frame
from stocklab.model import OnlineLogisticRegression
from stocklab.state import State

from conftest import synthetic_prices


def _replay_accuracy(tmp_path, config, persistence, tickers=6, days=1200):
    state = State(tmp_path, config)
    market = synthetic_prices(days, seed=99)
    for i in range(tickers):
        frame = build_frame(synthetic_prices(days, seed=i, persistence=persistence), market)
        engine.replay(state, f"T{i}", frame, "backtest", "2026-01-01T00:00:00+00:00")
    state.flush()
    return state.predictions


def test_features_only_use_the_past():
    prices, market = synthetic_prices(300, seed=1), synthetic_prices(300, seed=2)
    full = build_frame(prices, market)
    for cut in (120, 200, 299):
        day = prices.index[cut]
        partial = build_frame(prices.iloc[: cut + 1], market.iloc[: cut + 1])
        pd.testing.assert_series_equal(full.loc[day, PRICE_FEATURES], partial.loc[day, PRICE_FEATURES], check_names=False)


def test_target_is_the_next_session():
    prices = synthetic_prices(120, seed=3)
    frame = build_frame(prices, prices)
    day = frame.index[10]
    nxt = prices.index[prices.index.get_loc(day) + 1]
    expected = prices.at[nxt, "close"] / prices.at[nxt, "open"] - 1
    assert np.isclose(frame.at[day, "target_ret"], expected)
    assert frame.at[day, "target_up"] == float(expected > 0)
    assert pd.isna(frame["target_up"].iloc[-1])  # tomorrow is unknown


def test_random_walk_is_a_coin_flip(tmp_path, config):
    """If this ever shows a clear edge on pure noise, something is leaking future information."""
    preds = _replay_accuracy(tmp_path, config, persistence=0.0)
    for variant in VARIANTS:
        acc = preds.loc[preds["variant"] == variant, "correct"].mean()
        assert 0.47 < acc < 0.53, (variant, acc)


def test_a_real_pattern_is_learned(tmp_path, config):
    preds = _replay_accuracy(tmp_path, config, persistence=0.6)
    later = preds[preds["feature_date"] > preds["feature_date"].quantile(0.3)]
    acc = later.loc[later["variant"] == "price", "correct"].mean()
    assert acc > 0.62, acc


def test_prediction_is_recorded_before_the_model_sees_the_answer(tmp_path, config):
    frame = build_frame(synthetic_prices(200, seed=5), synthetic_prices(200, seed=6))
    state = State(tmp_path, config)
    engine.replay(state, "AAA", frame.iloc[:3], "backtest", "now")
    state.flush()
    recorded = state.predictions[state.predictions["variant"] == "price"]["p_up"].to_numpy()

    shadow = OnlineLogisticRegression(VARIANTS["price"], config.learning_rate, config.l2)
    expected = []
    for _, row in frame.iloc[:3].iterrows():
        x = engine.vector(row, "price")
        expected.append(shadow.predict_proba(x))
        shadow.update(x, int(row["target_up"]))
    assert recorded[0] == 0.5  # a brand-new model knows nothing
    np.testing.assert_allclose(recorded, np.round(expected, 5))


def test_confident_mistakes_teach_the_most():
    def weight_change(y):
        m = OnlineLogisticRegression(["a", "b"])
        for x in ([1.0, 0.0], [-1.0, 0.0], [0.0, 1.0], [0.0, -1.0]):  # give it some feature statistics
            m.update(x, 1)
        m.weights = np.array([2.2, 0.0])  # the model is now confident the example below goes up
        x = [1.0, 0.0]
        before = m.weights.copy()
        m.update(x, y)
        return np.abs(m.weights - before).sum()

    assert weight_change(0) > 5 * weight_change(1)


def test_model_survives_a_round_trip_to_json():
    m = OnlineLogisticRegression(["a", "b", "c"])
    rng = np.random.default_rng(0)
    for _ in range(50):
        m.update(rng.normal(size=3), int(rng.random() > 0.5))
    clone = OnlineLogisticRegression.from_dict(m.to_dict())
    x = rng.normal(size=3)
    assert abs(clone.predict_proba(x) - m.predict_proba(x)) < 1e-6


def test_missing_values_are_treated_as_average():
    m = OnlineLogisticRegression(["a", "b"])
    for v in range(10):
        m.update([float(v), float(v % 3)], v % 2)
    assert np.isfinite(m.predict_proba([np.nan, 1.0]))
    assert np.isfinite(m.update([np.nan, np.nan], 1))
