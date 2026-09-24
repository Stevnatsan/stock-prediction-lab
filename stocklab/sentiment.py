"""Headline sentiment with VADER, plus a small finance vocabulary VADER doesn't know by default."""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

FINANCE_WORDS = {
    "beat": 1.5, "beats": 1.5, "tops": 1.2, "upgrade": 2.0, "upgrades": 2.0, "upgraded": 2.0, "outperform": 1.8,
    "surge": 2.0, "surges": 2.0, "soar": 2.2, "soars": 2.2, "rally": 1.6, "rallies": 1.6, "record": 1.0,
    "bullish": 2.0, "buyback": 1.2, "raises": 1.0, "profit": 1.0, "growth": 1.0,
    "miss": -1.5, "misses": -1.5, "missed": -1.5, "downgrade": -2.0, "downgrades": -2.0, "downgraded": -2.0,
    "underperform": -1.8, "plunge": -2.4, "plunges": -2.4, "tumble": -2.0, "tumbles": -2.0, "slump": -1.8,
    "bearish": -2.0, "lawsuit": -1.6, "probe": -1.4, "recall": -1.6, "layoffs": -1.4, "bankruptcy": -3.0,
    "cuts": -1.0, "warns": -1.6, "fraud": -3.0, "investigation": -1.4, "loss": -1.2, "losses": -1.2,
}

_analyzer = SentimentIntensityAnalyzer()
_analyzer.lexicon.update(FINANCE_WORDS)


def score(text):
    """VADER compound score in [-1, 1]; above 0 reads positive."""
    return _analyzer.polarity_scores(text)["compound"]
