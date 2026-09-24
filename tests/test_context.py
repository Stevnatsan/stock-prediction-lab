"""The new historical features (earnings, analysts, macro) and the beat-the-market target: correct,
and never built from anything that wasn't public at the time."""
import numpy as np
import pandas as pd

from stocklab.features import HISTORICAL, analyst_features, build_frame, earnings_features, macro_features

from conftest import synthetic_prices

DAYS = pd.bdate_range("2026-03-02", periods=10)  # Mon 2 Mar ... Fri 13 Mar


def _earnings():
    return pd.DataFrame({"released": pd.to_datetime(["2025-12-04 16:30", "2026-03-04 16:30", "2026-03-10 07:00"]),
                         "surprise": [2.0, 8.5, -4.0]})


def test_earnings_flags_the_session_that_reacts():
    f = earnings_features(DAYS, _earnings())
    flagged = list(f.index[f["earn_next"] == 1].strftime("%m-%d"))
    # after-close report on Wed 4th -> Thursday reacts, so the Wednesday row is flagged;
    # pre-market report on Tue 10th -> Tuesday reacts, so the Monday row is flagged
    assert flagged == ["03-04", "03-09"]


def test_earnings_surprise_is_only_known_after_the_release():
    f = earnings_features(DAYS, _earnings())
    assert f.at[pd.Timestamp("2026-03-04"), "earn_surprise"] == 2.0   # the 16:30 report isn't out at the 16:00 close
    assert f.at[pd.Timestamp("2026-03-05"), "earn_surprise"] == 8.5
    assert f.at[pd.Timestamp("2026-03-10"), "earn_surprise"] == -4.0  # released 07:00 that morning
    assert f.at[pd.Timestamp("2026-03-05"), "earn_days_since"] == 0


def test_no_earnings_calendar_means_unknown_not_zero():
    assert earnings_features(DAYS, None).isna().all().all()
    far = earnings_features(pd.bdate_range("2020-01-01", periods=5), _earnings())
    assert far.isna().all().all()  # years before the calendar starts


def test_analyst_window_counts_only_public_actions():
    actions = pd.DataFrame({"time": pd.to_datetime(["2026-02-01 09:00", "2026-03-03 08:00", "2026-03-04 16:30", "2026-03-04 18:30"]),
                            "rating": [1.0, -1.0, 1.0, 1.0], "target": [np.nan, np.log(0.9), np.log(1.2), np.nan]})
    f = analyst_features(DAYS, actions)
    assert f.at[pd.Timestamp("2026-03-02"), "analyst_rating_30d"] == 1   # only the 1 February upgrade
    assert f.at[pd.Timestamp("2026-03-03"), "analyst_rating_30d"] == -1  # which has aged out; one downgrade
    assert f.at[pd.Timestamp("2026-03-04"), "analyst_rating_30d"] == 0   # 16:30 counts, 18:30 is after the run
    assert np.isclose(f.at[pd.Timestamp("2026-03-04"), "analyst_target_30d"], (np.log(0.9) + np.log(1.2)) / 2)
    assert f.at[pd.Timestamp("2026-03-05"), "analyst_rating_30d"] == 1   # the 18:30 one, the next day


def test_macro_uses_only_the_previous_days_value():
    macro = pd.DataFrame({"vix": np.arange(20.0, 30.0), "rate_10y": np.linspace(4, 4.9, 10), "curve": 0.5},
                         index=pd.bdate_range("2026-03-02", periods=10))
    f = macro_features(DAYS, macro)
    assert np.isnan(f.at[DAYS[0], "vix"])            # nothing published before the first day
    assert f.at[DAYS[3], "vix"] == 22.0              # Thursday sees Wednesday's value, not its own
    assert np.isclose(f.at[DAYS[8], "vix_chg_5"], np.log(27 / 22))


def test_beat_target_is_the_next_session_versus_the_market():
    prices, market = synthetic_prices(120, seed=3), synthetic_prices(120, seed=4)
    frame = build_frame(prices, market)
    day = frame.index[10]
    nxt = prices.index[prices.index.get_loc(day) + 1]
    excess = prices.at[nxt, "close"] / prices.at[nxt, "open"] - market.at[nxt, "close"] / market.at[nxt, "open"]
    assert np.isclose(frame.at[day, "target_excess"], excess)
    assert frame.at[day, "target_beat"] == float(excess > 0)
    assert 0.3 < frame["target_beat"].mean() < 0.7


def test_historical_features_only_use_the_past():
    prices, market = synthetic_prices(300, seed=1), synthetic_prices(300, seed=2)
    released = pd.to_datetime([d + pd.Timedelta(hours=16, minutes=5) for d in prices.index[::63]])
    context = {
        "earnings": pd.DataFrame({"released": released, "surprise": np.arange(len(released), dtype=float)}),
        "analysts": pd.DataFrame({"time": prices.index[::7] + pd.Timedelta(hours=10), "rating": 1.0, "target": 0.01}),
        "macro": pd.DataFrame({"vix": np.linspace(15, 30, 300), "rate_10y": 4.0, "curve": 0.2}, index=prices.index),
    }
    full = build_frame(prices, market, context)
    assert full[HISTORICAL].notna().mean().min() > 0.5 or full["filings_5d"].isna().all()
    for cut in (120, 200, 299):
        day = prices.index[cut]
        partial = build_frame(prices.iloc[: cut + 1], market.iloc[: cut + 1],
                              {**context, "macro": context["macro"].iloc[: cut + 1],
                               "analysts": context["analysts"][context["analysts"]["time"] <= day + pd.Timedelta(hours=17)]})
        pd.testing.assert_series_equal(full.loc[day, HISTORICAL], partial.loc[day, HISTORICAL], check_names=False)
