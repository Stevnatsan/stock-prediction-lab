from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Config:
    tickers: list
    market: str = "SPY"
    history_years: int = 4
    decision_threshold: float = 0.55
    cost_bps: float = 5.0
    learning_rate: float = 0.01
    l2: float = 1e-4
    sources: dict = field(default_factory=dict)
    paper_orders: dict = field(default_factory=dict)

    def source_on(self, name):
        return bool(self.sources.get(name, False))


def load_config(path=ROOT / "config.yaml"):
    raw = yaml.safe_load(Path(path).read_text())
    model = raw.get("model", {})
    return Config(
        tickers=[t.upper() for t in raw["tickers"]],
        market=raw.get("market", "SPY").upper(),
        history_years=int(raw.get("history_years", 4)),
        decision_threshold=float(raw.get("decision_threshold", 0.55)),
        cost_bps=float(raw.get("cost_bps", 5)),
        learning_rate=float(model.get("learning_rate", 0.01)),
        l2=float(model.get("l2", 1e-4)),
        sources=raw.get("sources", {}),
        paper_orders=raw.get("paper_orders") or {},
    )
