"""One daily run: fetch every source, score yesterday, learn, predict tomorrow, publish."""
from datetime import datetime, time, timezone

from . import engine
from .features import build_frame, news_features, score_headlines
from .report import build_report
from .sources.prices import NEW_YORK, drop_unfinished_session
from .state import State

MIN_HISTORY = 80  # trading days needed before the 50-day features exist
SESSION_OPEN = time(9, 30)


def next_session_started(last_date, now):
    """True once a weekday session after `last_date` has opened (market holidays aside). A prediction
    made then would already know part of the session it claims to predict, so it isn't made."""
    now_ny = now.astimezone(NEW_YORK)
    return now_ny.date() > last_date.date() and now_ny.weekday() < 5 and now_ny.time() >= SESSION_OPEN


def run_daily(config, sources, state_dir, reports_dir, readme_path=None, now=None):
    now = now or datetime.now(timezone.utc)
    now_iso = now.isoformat(timespec="seconds")
    state = State.load(state_dir, config)
    summary = {}

    market = sources.prices(config.market, config.history_years)
    if market is None:
        build_report(state, config, reports_dir, readme_path, now, sources.health, summary)
        raise RuntimeError(f"Could not download {config.market} prices, so no features can be built today.")
    market = drop_unfinished_session(market, now)

    for ticker in config.tickers:
        prices = sources.prices(ticker, config.history_years)
        if prices is None or len(prices) < MIN_HISTORY:
            summary[ticker] = {"status": "no price data"}
            continue
        prices = drop_unfinished_session(prices, now)
        frame = build_frame(prices, market, sources.filing_dates(ticker))
        info = {"status": "ok", "data_through": frame.index[-1].date().isoformat()}

        if not state.has_models(ticker):  # first time we see this stock: learn from its history
            info["history_replayed"] = engine.replay(state, ticker, frame, "backtest", now_iso)
        info["scored"] = engine.resolve_pending(state, ticker, frame, now_iso)
        info["caught_up"] = engine.replay(state, ticker, frame, "catch-up", now_iso, after=state.last_feature_date(ticker))

        stored = state.store_headlines(ticker, score_headlines(sources.headlines(ticker, now)), now)
        news = news_features(stored, now)
        info["headlines_24h"] = int(news["sent_count"])
        latest = frame.index[-1]
        if next_session_started(latest, now) and not engine.pending_for(state, ticker, latest):
            info["prediction"] = "skipped: the next session had already opened"
        else:
            info["prediction"] = engine.predict_latest(state, ticker, frame, news, now_iso)
        summary[ticker] = info

    state.save()
    build_report(state, config, reports_dir, readme_path, now, sources.health, summary)
    return summary
