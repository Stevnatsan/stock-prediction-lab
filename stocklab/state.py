"""Everything the bot remembers between runs lives in state/ as plain files committed to git,
so the full history of predictions, headlines and model weights is public and diffable."""
import json
import shutil
from pathlib import Path

import pandas as pd

from .features import ALL_MODELS, ENSEMBLES, LIVE_FEATURES, VARIANTS, signature
from .model import OnlineLogisticRegression

PREDICTION_COLUMNS = ["source", "ticker", "variant", "feature_date", "target_date", "p_up", "outcome_up",
                      "correct", "persist_up", "session_return", "made_at"]
LIVE_COLUMNS = ["feature_date", "ticker"] + LIVE_FEATURES


class State:
    def __init__(self, root, config):
        self.root = Path(root)
        self.config = config
        self.models = {}
        self.pending = []
        self.predictions = pd.DataFrame(columns=PREDICTION_COLUMNS)
        self.live = pd.DataFrame(columns=LIVE_COLUMNS)
        self.signatures = None  # None: written by a version that didn't keep them
        self._new_rows = []
        self._keys = set()
        self._rebuilt = set()

    # ---------- persistence ----------
    @classmethod
    def load(cls, root, config):
        s = cls(root, config)
        csv = s.root / "predictions.csv"
        if csv.exists() and csv.stat().st_size:
            s.predictions = pd.read_csv(csv, parse_dates=["feature_date", "target_date"])
        s._keys = set(zip(s.predictions["ticker"], s.predictions["variant"], s.predictions["feature_date"]))
        live = s.root / "live_features.csv"
        if live.exists() and live.stat().st_size:
            s.live = pd.read_csv(live, parse_dates=["feature_date"])
        pending = s.root / "pending.json"
        if pending.exists():
            s.pending = json.loads(pending.read_text())
        signatures = s.root / "models" / "signatures.json"
        if signatures.exists():
            s.signatures = json.loads(signatures.read_text())
        for path in sorted((s.root / "models").glob("*/*.json")):
            s.models[(path.parent.name, path.stem)] = OnlineLogisticRegression.from_dict(json.loads(path.read_text()))
        return s

    def save(self):
        self.flush()
        self.root.mkdir(parents=True, exist_ok=True)
        out = self.predictions.sort_values(["feature_date", "ticker", "variant"])
        out.to_csv(self.root / "predictions.csv", index=False, date_format="%Y-%m-%d", float_format="%.6g")
        if len(self.live):
            self.live.sort_values(["feature_date", "ticker"]).to_csv(self.root / "live_features.csv", index=False,
                                                                     date_format="%Y-%m-%d", float_format="%.6g")
        (self.root / "pending.json").write_text(json.dumps(self.pending, indent=1))
        for variant in self._rebuilt:
            shutil.rmtree(self.root / "models" / variant, ignore_errors=True)  # no stale weights left behind
        for (variant, ticker), model in self.models.items():
            path = self.root / "models" / variant / f"{ticker}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(model.to_dict(), indent=1))
        (self.root / "models").mkdir(exist_ok=True)
        (self.root / "models" / "signatures.json").write_text(json.dumps({v: signature(v) for v in ALL_MODELS}, indent=1))

    # ---------- models ----------
    def _stored_signature(self, variant):
        if self.signatures is not None:
            return self.signatures.get(variant)
        # older state: logistic models carry their feature list; everything else has to be rebuilt
        features = {tuple(m.features) for (v, _), m in self.models.items() if v == variant}
        return ["logistic", "up", *features.pop()] if variant in VARIANTS and len(features) == 1 else None

    def drop_stale_models(self):
        """Models whose inputs changed (new features, a new question) are rebuilt from history: their
        weights and replayed predictions are dropped here and recreated by the next run. Real live
        predictions are never dropped. Returns the models that were reset."""
        self.flush()
        stale = []
        for variant in ALL_MODELS:
            has_history = (self.predictions["variant"] == variant).any() or any(v == variant for v, _ in self.models)
            stored = self._stored_signature(variant)
            members = ENSEMBLES.get(variant, ())
            if has_history and (stored != json.loads(json.dumps(signature(variant))) or any(m in stale for m in members)):
                stale.append(variant)
        if stale:
            self.models = {k: m for k, m in self.models.items() if k[0] not in stale}
            p = self.predictions
            self.predictions = p[~(p["variant"].isin(stale) & (p["source"] != "live"))].reset_index(drop=True)
            self._keys = set(zip(self.predictions["ticker"], self.predictions["variant"], self.predictions["feature_date"]))
            self._rebuilt.update(stale)
        return stale

    def missing_models(self, ticker):
        """Online models this stock doesn't have yet (e.g. a newly added stock or a rebuilt model)."""
        return [v for v in VARIANTS if (v, ticker) not in self.models]

    def model(self, variant, ticker):
        key = (variant, ticker)
        if key not in self.models:
            self.models[key] = OnlineLogisticRegression(VARIANTS[variant], self.config.learning_rate, self.config.l2)
        return self.models[key]

    # ---------- predictions ----------
    def add_prediction(self, **row):
        """Log one scored prediction; a day already logged for this stock and model is ignored. Returns 1 if added."""
        key = (row["ticker"], row["variant"], pd.Timestamp(row["feature_date"]))
        if key in self._keys:
            return 0
        self._keys.add(key)
        self._new_rows.append({c: row.get(c) for c in PREDICTION_COLUMNS})
        return 1

    def flush(self):
        if self._new_rows:
            new = pd.DataFrame(self._new_rows, columns=PREDICTION_COLUMNS)
            for col in ("feature_date", "target_date"):
                new[col] = pd.to_datetime(new[col])
            self.predictions = new if self.predictions.empty else pd.concat([self.predictions, new], ignore_index=True)
            self._new_rows = []

    def last_feature_date(self, ticker, variant):
        """Latest day this model already predicted (resolved or pending) for this ticker."""
        self.flush()
        p = self.predictions
        dates = list(p.loc[(p["ticker"] == ticker) & (p["variant"] == variant), "feature_date"])
        dates += [pd.Timestamp(x["feature_date"]) for x in self.pending if x["ticker"] == ticker and x["variant"] == variant]
        return max(dates) if dates else None

    def resume_after(self, ticker, variant):
        """Where a model's history replay should continue from: None (from the start) if it has never
        replayed this stock's history, otherwise the last day it predicted."""
        self.flush()
        p = self.predictions
        replayed = ((p["ticker"] == ticker) & (p["variant"] == variant) & (p["source"] != "live")).any()
        return self.last_feature_date(ticker, variant) if replayed else None

    # ---------- live-only features ----------
    def record_live(self, ticker, date, features):
        """Keep tonight's live-only inputs (sentiment by both scorers, options, social), so VADER and
        FinBERT can be compared and these features gain a history of their own."""
        row = {"feature_date": pd.Timestamp(date), "ticker": ticker, **{c: features.get(c) for c in LIVE_FEATURES}}
        live = self.live[~((self.live["ticker"] == ticker) & (self.live["feature_date"] == row["feature_date"]))]
        self.live = pd.concat([live, pd.DataFrame([row], columns=LIVE_COLUMNS)], ignore_index=True) if len(live) \
            else pd.DataFrame([row], columns=LIVE_COLUMNS)

    # ---------- headlines ----------
    def store_headlines(self, ticker, items, now, finbert=None, fresh_hours=72, keep_days=30):
        """Add headlines not seen before (only recent ones matter for features), drop anything older
        than `keep_days`, score any not yet scored by FinBERT (if `finbert` is given and works), and
        return what is stored for this ticker."""
        path = self.root / "news" / f"{ticker}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        stored = [json.loads(line) for line in path.read_text().splitlines() if line] if path.exists() else []
        seen = {h["id"] for h in stored}
        for h in items:
            age_hours = (now - pd.Timestamp(h["published"]).to_pydatetime()).total_seconds() / 3600
            if h["id"] in seen or not (0 <= age_hours <= fresh_hours):
                continue
            seen.add(h["id"])
            stored.append(dict(h, collected=now.isoformat(timespec="seconds")))
        cutoff = now - pd.Timedelta(days=keep_days)
        stored = [h for h in stored if pd.Timestamp(h["published"]).to_pydatetime() >= cutoff]
        stored.sort(key=lambda h: h["published"])
        unscored = [h for h in stored if h.get("finbert") is None]
        if finbert and unscored:
            scores = finbert([h["title"] for h in unscored])
            for h, s in zip(unscored, scores or []):
                h["finbert"] = s
        path.write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in stored))
        return stored
