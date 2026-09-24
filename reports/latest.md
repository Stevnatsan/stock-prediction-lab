# Stock prediction lab: latest report

Generated 2026-09-24 15:29 UTC.

## Next-session calls

No open calls right now. New ones are made after each US market close.

## Accuracy

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? |
|---|---|---|---|---|---|---|
| Historical replay, logistic, price + news | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |
| Historical replay, logistic, price only | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |

![Rolling accuracy](rolling_accuracy.png)

## Per stock

Based on all resolved (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price + news | Logistic, price only | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|
| AAPL | 1,034 | 51.4% | 51.4% | – | – | 54.4% |
| AMZN | 1,034 | 49.5% | 49.5% | – | – | 50.8% |
| GOOGL | 1,034 | 51.4% | 51.4% | – | – | 54.3% |
| JPM | 1,034 | 50.8% | 50.8% | – | – | 54.0% |
| META | 1,034 | 52.7% | 52.7% | – | – | 50.8% |
| MSFT | 1,034 | 51.7% | 51.7% | – | – | 51.8% |
| NVDA | 1,034 | 49.4% | 49.4% | – | – | 53.0% |
| TSLA | 1,034 | 53.2% | 53.2% | – | – | 49.8% |
| UNH | 1,033 | 50.1% | 50.1% | – | – | 51.3% |
| XOM | 1,033 | 49.4% | 49.4% | – | – | 51.9% |

## Paper trading

Hypothetical only: no real orders are placed. Each session a strategy buys, at the open, the (up to) 3 stocks its model rates most likely to rise with P(up) ≥ 52%, and sells them at the close.

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price + news | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Top 3 by logistic, price only | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Buy every stock, every session | 1,034 | -0.3% | -0.1% | 0.08 | 52.0% |

![Paper trading](paper_trading.png)

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|

---

Educational project. Not financial advice.
