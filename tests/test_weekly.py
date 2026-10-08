import pandas as pd
import pytest

from stocklab import weekly
from stocklab.features import build_frame

from conftest import evening_after, synthetic_prices


def _setup(n=420):
    prices = {t: synthetic_prices(n, seed=s) for t, s in (("AAA", 1), ("BBB", 2))}
    market = synthetic_prices(n, seed=3)
    frames = {t: build_frame(p, market) for t, p in prices.items()}
    return prices, market, frames


def test_week_target_is_next_open_to_fifth_close():
    prices, market, frames = _setup()
    f = weekly.week_frame(frames["AAA"], prices["AAA"], market)
    day = f.index[100]
    i = prices["AAA"].index.get_loc(day)
    expected = prices["AAA"]["close"].iloc[i + 5] / prices["AAA"]["open"].iloc[i + 1] - 1
    assert f.at[day, "week_return"] == pytest.approx(expected)
    assert f.at[day, "target_date"] == prices["AAA"].index[i + 5]
    assert f["target_wk_up"].iloc[-5:].isna().all()  # the last week isn't over yet


def test_calls_are_logged_then_scored_when_the_week_ends(tmp_path):
    prices, market, frames = _setup()
    cut = {t: p.iloc[:-6] for t, p in prices.items()}
    early = {t: build_frame(p, market.iloc[:-6]) for t, p in cut.items()}
    first = weekly.run(early, cut, market.iloc[:-6], tmp_path, evening_after(cut["AAA"].index[-1]))
    assert set(first["calls"]) == {"AAA", "BBB"}
    call = first["calls"]["AAA"]
    assert pd.Timestamp(call["week_to"]) == pd.Timestamp(call["feature_date"]) + pd.offsets.BDay(5)
    assert 0 < first["record"]["up"]["all"]["calls"] and first["record"]["up"]["all"]["accuracy"] is not None
    log = pd.read_csv(tmp_path / "weekly.csv")
    assert len(log) == 2 and log["outcome_up"].isna().all()

    later = weekly.run(frames, prices, market, tmp_path, evening_after(prices["AAA"].index[-1]))
    log = pd.read_csv(tmp_path / "weekly.csv")
    scored = log[log["feature_date"] == call["feature_date"]]
    assert scored["outcome_up"].notna().all()
    wf = weekly.week_frame(frames["AAA"], prices["AAA"], market)
    assert scored.loc[scored["ticker"] == "AAA", "week_return"].iloc[0] == pytest.approx(wf.at[pd.Timestamp(call["feature_date"]), "week_return"], abs=1e-6)
    assert later["live"]["all"]["calls"] == 2


def test_preview_run_does_not_write_the_log(tmp_path):
    prices, market, frames = _setup()
    weekly.run(frames, prices, market, tmp_path, evening_after(prices["AAA"].index[-1]), save=False)
    assert not (tmp_path / "weekly.csv").exists()
