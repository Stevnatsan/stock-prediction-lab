"""One daily run: fetch every source, score yesterday, learn, predict tomorrow, publish."""
from datetime import datetime, time, timezone

from . import boosting, engine
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
    state.pending = [p for p in state.pending if p["ticker"] in config.tickers]  # stocks removed from the watchlist
    summary = {}

    market = sources.prices(config.market, config.history_years)
    if market is None:
        build_report(state, config, reports_dir, readme_path, now, sources.health, summary)
        raise RuntimeError(f"Could not download {config.market} prices, so no features can be built today.")
    market = drop_unfinished_session(market, now)

    # 1. Online logistic models, one per stock: learn from history once, then score and learn daily.
    frames = {}
    for ticker in config.tickers:
        prices = sources.prices(ticker, config.history_years)
        if prices is None or len(prices) < MIN_HISTORY:
            summary[ticker] = {"status": "no price data"}
            continue
        frame = build_frame(drop_unfinished_session(prices, now), market, sources.filing_dates(ticker))
        frames[ticker] = frame
        info = summary[ticker] = {"status": "ok", "data_through": frame.index[-1].date().isoformat()}
        missing = state.missing_models(ticker)
        if missing:  # first time we see this stock: learn from its history
            info["history_replayed"] = engine.replay(state, ticker, frame, "backtest", now_iso, variants=missing)
        info["scored"] = engine.resolve_pending(state, ticker, frame, now_iso)
        info["caught_up"] = engine.replay(state, ticker, frame, "catch-up", now_iso,
                                          after=state.last_feature_date(ticker, "full"))

    # 2. Gradient boosting across all stocks: fill in any history it hasn't predicted yet.
    starts = {t: state.last_feature_date(t, "gbm") for t in frames}
    for ticker, probabilities in boosting.walk_forward(frames, starts).items():
        source = "backtest" if starts[ticker] is None else "catch-up"
        engine.record_boosting(state, ticker, frames[ticker], probabilities, source, now_iso)
    engine.add_ensembles(state)

    # 3. Tonight's predictions for the next session.
    ready = []
    for ticker, frame in frames.items():
        info = summary[ticker]
        stored = state.store_headlines(ticker, score_headlines(sources.headlines(ticker, now)), now)
        news = news_features(stored, now)
        info["headlines_24h"] = int(news["sent_count"])
        latest = frame.index[-1]
        if next_session_started(latest, now) and not engine.pending_for(state, ticker, latest):
            info["prediction"] = "skipped: the next session had already opened"
            continue
        info["prediction"] = engine.predict_latest(state, ticker, frame, news, now_iso)
        if "gbm" not in engine.pending_for(state, ticker, latest):
            ready.append(ticker)
    if ready:
        for ticker, p in boosting.predict_latest(frames, ready).items():
            day = frames[ticker].index[-1]
            like = next(x for x in state.pending if x["ticker"] == ticker and x["variant"] == "full"
                        and x["feature_date"] == day.date().isoformat())
            engine.add_pending(state, ticker, "gbm", p, like)
            engine.add_pending(state, ticker, "ensemble", (p + like["p_up"]) / 2, like)
            summary[ticker]["prediction"] = engine.pending_for(state, ticker, day)

    state.save()
    build_report(state, config, reports_dir, readme_path, now, sources.health, summary)
    return summary
