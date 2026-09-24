"""Everything the bot remembers between runs lives in state/ as plain files committed to git,
so the full history of predictions, headlines and model weights is public and diffable."""
import json
from pathlib import Path

import pandas as pd

from .features import VARIANTS
from .model import OnlineLogisticRegression

PREDICTION_COLUMNS = ["source", "ticker", "variant", "feature_date", "target_date", "p_up", "outcome_up",
                      "correct", "persist_up", "session_return", "made_at"]


class State:
    def __init__(self, root, config):
        self.root = Path(root)
        self.config = config
        self.models = {}
        self.pending = []
        self.predictions = pd.DataFrame(columns=PREDICTION_COLUMNS)
        self._new_rows = []

    # ---------- persistence ----------
    @classmethod
    def load(cls, root, config):
        s = cls(root, config)
        csv = s.root / "predictions.csv"
        if csv.exists() and csv.stat().st_size:
            s.predictions = pd.read_csv(csv, parse_dates=["feature_date", "target_date"])
        pending = s.root / "pending.json"
        if pending.exists():
            s.pending = json.loads(pending.read_text())
        for path in sorted((s.root / "models").glob("*/*.json")):
            s.models[(path.parent.name, path.stem)] = OnlineLogisticRegression.from_dict(json.loads(path.read_text()))
        return s

    def save(self):
        self.flush()
        self.root.mkdir(parents=True, exist_ok=True)
        out = self.predictions.sort_values(["feature_date", "ticker", "variant"])
        out.to_csv(self.root / "predictions.csv", index=False, date_format="%Y-%m-%d", float_format="%.6g")
        (self.root / "pending.json").write_text(json.dumps(self.pending, indent=1))
        for (variant, ticker), model in self.models.items():
            path = self.root / "models" / variant / f"{ticker}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(model.to_dict(), indent=1))

    # ---------- models ----------
    def missing_models(self, ticker):
        """Online models this stock doesn't have yet (e.g. a newly added stock)."""
        return [v for v in VARIANTS if (v, ticker) not in self.models]

    def model(self, variant, ticker):
        key = (variant, ticker)
        if key not in self.models:
            self.models[key] = OnlineLogisticRegression(VARIANTS[variant], self.config.learning_rate, self.config.l2)
        return self.models[key]

    # ---------- predictions ----------
    def add_prediction(self, **row):
        self._new_rows.append({c: row.get(c) for c in PREDICTION_COLUMNS})

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

    # ---------- headlines ----------
    def store_headlines(self, ticker, items, now, fresh_hours=72, keep_days=30):
        """Add headlines not seen before (only recent ones matter for features), drop anything older
        than `keep_days`, and return what is stored for this ticker."""
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
        path.write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in stored))
        return stored
