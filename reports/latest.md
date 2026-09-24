# Stock prediction lab: latest report

Generated 2026-09-24 15:30 UTC.

## Next-session calls

No open calls right now. New ones are made after each US market close.

## Accuracy

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? |
|---|---|---|---|---|---|---|
| Historical replay, logistic, price + news | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |
| Historical replay, logistic, price only | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |
| Historical replay, gradient boosting | 9,748 | **51.2%** | 50.2%–52.2% | 52.3% | 49.8% | no |
| Historical replay, ensemble | 9,748 | **51.2%** | 50.2%–52.2% | 52.3% | 49.8% | no |

![Rolling accuracy](rolling_accuracy.png)

## Per stock

Based on all resolved (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price + news | Logistic, price only | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|
| AAPL | 1,034 | 51.4% | 51.4% | 52.3% | 51.6% | 54.4% |
| AMZN | 1,034 | 49.5% | 49.5% | 51.4% | 50.1% | 50.8% |
| GOOGL | 1,034 | 51.4% | 51.4% | 51.5% | 51.7% | 54.3% |
| JPM | 1,034 | 50.8% | 50.8% | 52.5% | 52.0% | 54.0% |
| META | 1,034 | 52.7% | 52.7% | 49.3% | 50.9% | 50.8% |
| MSFT | 1,034 | 51.7% | 51.7% | 49.4% | 50.2% | 51.8% |
| NVDA | 1,034 | 49.4% | 49.4% | 51.6% | 52.2% | 53.0% |
| TSLA | 1,034 | 53.2% | 53.2% | 50.1% | 52.6% | 49.8% |
| UNH | 1,033 | 50.1% | 50.1% | 52.2% | 50.2% | 51.3% |
| XOM | 1,033 | 49.4% | 49.4% | 51.7% | 51.0% | 51.9% |

## Paper trading

Hypothetical only: no real orders are placed. Each session a strategy buys, at the open, the (up to) 3 stocks its model rates most likely to rise with P(up) ≥ 52%, and sells them at the close.

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price + news | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Top 3 by logistic, price only | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Top 3 by gradient boosting | 975 | -3.3% | -0.9% | 0.06 | 44.8% |
| Top 3 by ensemble | 975 | +30.6% | +7.1% | 0.44 | 49.2% |
| Buy every stock, every session | 1,034 | -0.3% | -0.1% | 0.08 | 52.0% |

![Paper trading](paper_trading.png)

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| google_news | 10 | 0 | 994 |  |
| prices | 11 | 0 | 11933 |  |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 182 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-23 | 0 | 0 | 33 |
| MSFT | ok | 2026-09-23 | 0 | 0 | 29 |
| NVDA | ok | 2026-09-23 | 0 | 0 | 72 |
| AMZN | ok | 2026-09-23 | 0 | 0 | 54 |
| GOOGL | ok | 2026-09-23 | 0 | 0 | 50 |
| META | ok | 2026-09-23 | 0 | 0 | 87 |
| TSLA | ok | 2026-09-23 | 0 | 0 | 23 |
| JPM | ok | 2026-09-23 | 0 | 0 | 17 |
| XOM | ok | 2026-09-23 | 0 | 0 | 20 |
| UNH | ok | 2026-09-23 | 0 | 0 | 15 |

---

Educational project. Not financial advice.
