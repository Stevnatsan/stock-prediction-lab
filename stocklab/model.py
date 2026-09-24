"""A logistic regression that learns one example at a time, small enough to read in a minute.

Every day it first predicts, then (once the session is over) learns from the true outcome.
The update is proportional to the error (p - y): a confident wrong call such as p = 0.9 when the
stock fell moves the weights nine times more than a confident right one. Wrong predictions are
literally the biggest lessons. The constant learning rate means old days slowly fade, which
suits markets whose behaviour drifts.
"""
import numpy as np


class OnlineLogisticRegression:
    def __init__(self, features, learning_rate=0.01, l2=1e-4):
        self.features = list(features)
        n = len(self.features)
        self.learning_rate = learning_rate
        self.l2 = l2
        self.weights = np.zeros(n)
        self.bias = 0.0
        # running mean / variance per feature (Welford), so inputs are standardised on the fly
        self.count = np.zeros(n)
        self.mean = np.zeros(n)
        self.m2 = np.zeros(n)
        self.updates = 0

    def _standardise(self, x):
        x = np.asarray(x, dtype=float)
        std = np.sqrt(np.divide(self.m2, self.count - 1, out=np.ones_like(self.m2), where=self.count > 1))
        std = np.where(std > 1e-12, std, 1.0)
        z = (x - self.mean) / std
        z = np.where(np.isfinite(z) & (self.count > 1), z, 0.0)  # unknown or not-yet-seen feature -> average
        return np.clip(z, -4, 4)  # one freak day shouldn't dominate an update

    def predict_proba(self, x):
        s = float(self._standardise(x) @ self.weights + self.bias)
        return float(1 / (1 + np.exp(-np.clip(s, -30, 30))))

    def update(self, x, y):
        """Learn from one outcome (y = 1 up, 0 down). Returns the size of the mistake |p - y|."""
        x = np.asarray(x, dtype=float)
        finite = np.isfinite(x)
        self.count[finite] += 1
        delta = np.where(finite, x - self.mean, 0.0)
        self.mean = self.mean + np.divide(delta, self.count, out=np.zeros_like(delta), where=finite)
        self.m2 = self.m2 + np.where(finite, delta * (x - self.mean), 0.0)

        z = self._standardise(x)
        p = float(1 / (1 + np.exp(-np.clip(z @ self.weights + self.bias, -30, 30))))
        error = p - y
        self.weights -= self.learning_rate * (error * z + self.l2 * self.weights)
        self.bias -= self.learning_rate * error
        self.updates += 1
        return abs(error)

    def to_dict(self):
        return {"features": self.features, "learning_rate": self.learning_rate, "l2": self.l2, "updates": self.updates,
                "weights": dict(zip(self.features, np.round(self.weights, 6).tolist())), "bias": round(self.bias, 6),
                "count": self.count.tolist(), "mean": self.mean.tolist(), "m2": self.m2.tolist()}

    @classmethod
    def from_dict(cls, d):
        m = cls(d["features"], d["learning_rate"], d["l2"])
        m.weights = np.array([d["weights"][f] for f in m.features], dtype=float)
        m.bias = float(d["bias"])
        m.count, m.mean, m.m2 = (np.array(d[k], dtype=float) for k in ("count", "mean", "m2"))
        m.updates = int(d["updates"])
        return m
