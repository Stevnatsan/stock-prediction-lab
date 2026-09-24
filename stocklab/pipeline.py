"""One daily run: fetch every source, score yesterday, learn, predict tomorrow, publish."""
from datetime import datetime, time, timezone

from . import boosting, engine
from .features import BOOSTED, ENSEMBLES, TASKS, VARIANTS, build_frame, live_features, score_headlines, task_of
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
    notes = []
    rebuilt = state.drop_stale_models()
    if rebuilt:
        notes.append(f"Rebuilt from history because their inputs changed: {', '.join(rebuilt)}.")
    summary = {}

    market = sources.prices(config.market, config.history_years)
    if market is None:
        build_report(state, config, reports_dir, readme_path, now, sources.health, summary, notes)
        raise RuntimeError(f"Could not download {config.market} prices, so no features can be built today.")
    market = drop_unfinished_session(market, now)
    macro = sources.macro(config.history_years)

    # 1. Online logistic models, one per stock: learn from history once, then score and learn daily.
    frames = {}
    for ticker in config.tickers:
        prices = sources.prices(ticker, config.history_years)
        if prices is None or len(prices) < MIN_HISTORY:
            summary[ticker] = {"status": "no price data"}
            continue
        context = {"filings": sources.filing_dates(ticker), "earnings": sources.earnings(ticker),
                   "analysts": sources.analysts(ticker), "macro": macro}
        frame = build_frame(drop_unfinished_session(prices, now), market, context)
        frames[ticker] = frame
        info = summary[ticker] = {"status": "ok", "data_through": frame.index[-1].date().isoformat()}
        missing = state.missing_models(ticker)
        if missing:  # first time we see this stock (or a model was rebuilt): learn from its history
            info["history_replayed"] = engine.replay(state, ticker, frame, "backtest", now_iso, variants=missing)
        info["scored"] = engine.resolve_pending(state, ticker, frame, now_iso)
        info["caught_up"] = max(engine.replay(state, ticker, frame, "catch-up", now_iso, variants=[v],
                                              after=state.last_feature_date(ticker, v)) for v in VARIANTS)

    # 2. Gradient boosting across all stocks: fill in any history it hasn't predicted yet.
    for variant, features in BOOSTED.items():
        target = TASKS[task_of(variant)][0]
        starts = {t: state.resume_after(t, variant) for t in frames}
        for ticker, probabilities in boosting.walk_forward(frames, starts, features, target).items():
            source = "backtest" if starts[ticker] is None else "catch-up"
            engine.record_boosting(state, ticker, variant, frames[ticker], probabilities, source, now_iso)
    engine.add_ensembles(state)

    # 3. Tonight's inputs and predictions for the next session.
    ready = []
    for ticker, frame in frames.items():
        info = summary[ticker]
        headlines = state.store_headlines(ticker, score_headlines(sources.headlines(ticker, now)), now, sources.finbert)
        latest = frame.index[-1]
        if next_session_started(latest, now) and not engine.pending_for(state, ticker, latest):
            info["prediction"] = "skipped: the next session had already opened"
            continue
        row = frame.loc[latest]
        live = live_features(row, headlines, sources.options(ticker, now, float(row["close"])), sources.social(ticker, now), now)
        info["headlines_24h"] = int(live["sent_count"])
        state.record_live(ticker, latest, live)
        info["prediction"] = engine.predict_latest(state, ticker, frame, live, now_iso)
        if any(v not in info["prediction"] for v in BOOSTED):
            ready.append(ticker)
    if ready:
        for variant, features in BOOSTED.items():
            needed = [t for t in ready if variant not in engine.pending_for(state, t, frames[t].index[-1])]
            if needed:
                target = TASKS[task_of(variant)][0]
                for ticker, p in boosting.predict_latest(frames, needed, features, target).items():
                    engine.add_pending(state, ticker, frames[ticker].index[-1], variant, p)
        for ticker in ready:
            day = frames[ticker].index[-1]
            calls = engine.pending_for(state, ticker, day)
            for ensemble, (a, b) in ENSEMBLES.items():
                if a in calls and b in calls and ensemble not in calls:
                    engine.add_pending(state, ticker, day, ensemble, (calls[a] + calls[b]) / 2)
            summary[ticker]["prediction"] = engine.pending_for(state, ticker, day)

    # 4. Real fills from the Alpaca paper account, if one is connected.
    broker = getattr(sources, "broker", None)
    if broker is not None:
        from . import alpaca

        try:
            alpaca.sync(broker, state.root, now)
        except Exception as exc:  # noqa: BLE001 - the broker being down must not stop the predictions
            sources.health["alpaca"]["failed"] += 1
            sources.health["alpaca"]["last_error"] = f"{type(exc).__name__}: {exc}"[:200]
        else:
            sources.health["alpaca"]["ok"] += 1

    state.save()
    build_report(state, config, reports_dir, readme_path, now, sources.health, summary, notes)
    return summary
