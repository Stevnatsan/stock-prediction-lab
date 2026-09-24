# Stock prediction lab: latest report

Generated 2026-09-24 16:06 UTC.

> Rebuilt from history because their inputs changed: full, gbm, ensemble.

## Next-session calls

No open calls right now. New ones are made after each US market close.

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Historical replay, logistic, price only | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,338 | **51.2%** | 50.2%–52.1% | 52.2% | 49.8% | no | 0.2532 |
| Historical replay, logistic, all sources (FinBERT) | 10,338 | **51.2%** | 50.2%–52.1% | 52.2% | 49.8% | no | 0.2532 |
| Historical replay, gradient boosting | 9,748 | **50.7%** | 49.7%–51.7% | 52.3% | 49.8% | no | 0.2556 |
| Historical replay, ensemble | 9,748 | **51.3%** | 50.3%–52.3% | 52.3% | 49.8% | no | 0.2518 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Historical replay, logistic, all sources (VADER) | 10,338 | **51.5%** | 50.5%–52.4% | 50.4% | 49.8% | yes | 0.2529 |
| Historical replay, gradient boosting | 9,748 | **50.5%** | 49.5%–51.5% | 50.5% | 49.9% | no | 0.2541 |
| Historical replay, ensemble | 9,748 | **51.0%** | 50.0%–52.0% | 50.5% | 49.9% | within noise | 0.2516 |

*Brier* is the mean squared error of the probabilities (lower is better; always saying 50% scores 0.25).

![Rolling accuracy](rolling_accuracy.png)

## Calibration

Predictions grouped by confidence. For an honest model, the share that happened matches the prediction: of all the "55–60%" calls, about 57% should come true. *Average gap* is the weighted average distance between the two (expected calibration error). Uses live predictions once a model has 300, before that all scored ones.

**Up or down?**

| Predicted | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble |
|---|---|---|---|---|---|
| under 40% | 52.7% (n=245) | 48.8% (n=414) | 48.8% (n=414) | 52.6% (n=699) | 50.8% (n=258) |
| 40–45% | 52.1% (n=789) | 53.5% (n=927) | 53.5% (n=927) | 53.6% (n=720) | 49.6% (n=671) |
| 45–48% | 50.7% (n=1,283) | 49.0% (n=1,224) | 49.0% (n=1,224) | 51.5% (n=786) | 53.3% (n=1,024) |
| 48–50% | 52.6% (n=1,305) | 53.1% (n=1,201) | 53.1% (n=1,201) | 52.6% (n=917) | 51.5% (n=1,065) |
| 50–52% | 52.5% (n=1,692) | 52.9% (n=1,366) | 52.9% (n=1,366) | 50.0% (n=1,261) | 51.5% (n=1,415) |
| 52–55% | 52.3% (n=2,294) | 52.8% (n=2,058) | 52.8% (n=2,058) | 50.9% (n=2,146) | 52.8% (n=2,438) |
| 55–60% | 52.5% (n=2,092) | 52.1% (n=2,128) | 52.1% (n=2,128) | 54.2% (n=1,859) | 52.8% (n=2,185) |
| 60% or more | 52.4% (n=638) | 53.3% (n=1,020) | 53.3% (n=1,020) | 53.7% (n=1,360) | 53.8% (n=692) |
| **Average gap** | **4.1 pts** | **4.7 pts** | **4.7 pts** | **5.7 pts** | **3.6 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 47.8% (n=655) | 49.7% (n=565) | 51.4% (n=255) |
| 40–45% | 47.3% (n=1,291) | 49.5% (n=945) | 46.9% (n=1,036) |
| 45–48% | 49.7% (n=1,595) | 50.2% (n=1,283) | 49.3% (n=1,483) |
| 48–50% | 50.1% (n=1,253) | 50.3% (n=1,239) | 51.0% (n=1,450) |
| 50–52% | 51.1% (n=1,353) | 51.7% (n=1,545) | 51.2% (n=1,665) |
| 52–55% | 51.0% (n=1,729) | 51.1% (n=2,071) | 50.5% (n=2,135) |
| 55–60% | 53.5% (n=1,684) | 50.2% (n=1,518) | 52.4% (n=1,399) |
| 60% or more | 50.5% (n=778) | 49.3% (n=582) | 52.9% (n=325) |
| **Average gap** | **4.0 pts** | **4.6 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

Both scorers read every headline from the first live run on; results appear here once those calls are scored.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,034 | 51.4% | 50.5% | 50.5% | 50.5% | 50.5% | 54.4% |
| AMZN | 1,034 | 49.5% | 49.1% | 49.1% | 49.7% | 50.2% | 50.8% |
| GOOGL | 1,034 | 51.4% | 51.1% | 51.1% | 51.3% | 52.0% | 54.3% |
| JPM | 1,034 | 50.8% | 50.8% | 50.8% | 50.3% | 49.5% | 54.0% |
| META | 1,034 | 52.7% | 53.3% | 53.3% | 51.2% | 51.0% | 50.8% |
| MSFT | 1,034 | 51.7% | 50.9% | 50.9% | 50.4% | 51.9% | 51.8% |
| NVDA | 1,034 | 49.4% | 50.6% | 50.6% | 50.5% | 52.8% | 53.0% |
| TSLA | 1,034 | 53.2% | 53.2% | 53.2% | 49.0% | 51.9% | 49.8% |
| UNH | 1,033 | 50.1% | 51.1% | 51.1% | 50.8% | 51.1% | 51.3% |
| XOM | 1,033 | 49.4% | 51.3% | 51.3% | 53.3% | 52.4% | 51.9% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,034 | 51.4% | 50.2% | 51.0% | 53.1% |
| AMZN | 1,034 | 48.8% | 49.0% | 49.3% | 47.8% |
| GOOGL | 1,034 | 52.2% | 52.3% | 50.9% | 53.5% |
| JPM | 1,034 | 53.1% | 50.7% | 50.6% | 53.5% |
| META | 1,034 | 49.9% | 49.5% | 50.5% | 49.0% |
| MSFT | 1,034 | 51.9% | 47.8% | 50.1% | 48.7% |
| NVDA | 1,034 | 51.9% | 51.7% | 53.5% | 52.3% |
| TSLA | 1,034 | 52.1% | 50.7% | 51.9% | 48.9% |
| UNH | 1,033 | 52.2% | 51.4% | 52.1% | 47.6% |
| XOM | 1,033 | 50.9% | 51.7% | 50.4% | 49.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,034 | +43.8% | +9.3% | 0.53 | 49.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,034 | +43.8% | +9.3% | 0.53 | 49.2% |
| Top 3 by gradient boosting | 975 | +19.2% | +4.6% | 0.32 | 45.5% |
| Top 3 by ensemble | 975 | +16.7% | +4.1% | 0.30 | 48.7% |
| Buy every stock, every session | 1,034 | -0.3% | -0.1% | 0.08 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,034 | -32.6% | -9.2% | -0.60 | 46.5% |
| Top 3 by gradient boosting | 975 | -38.7% | -11.9% | -0.74 | 43.3% |
| Top 3 by ensemble | 975 | -13.6% | -3.7% | -0.17 | 47.1% |
| Every stock minus SPY | 1,034 | -52.9% | -16.8% | -2.38 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7669 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 772 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=30) |
| google_news | 10 | 0 | 994 |  |
| prices | 11 | 0 | 11933 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 182 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-23 | 1034 | 0 | 0 |
| MSFT | ok | 2026-09-23 | 1034 | 0 | 0 |
| NVDA | ok | 2026-09-23 | 1034 | 0 | 0 |
| AMZN | ok | 2026-09-23 | 1034 | 0 | 0 |
| GOOGL | ok | 2026-09-23 | 1034 | 0 | 0 |
| META | ok | 2026-09-23 | 1034 | 0 | 0 |
| TSLA | ok | 2026-09-23 | 1034 | 0 | 0 |
| JPM | ok | 2026-09-23 | 1034 | 0 | 0 |
| XOM | ok | 2026-09-23 | 1033 | 0 | 0 |
| UNH | ok | 2026-09-23 | 1033 | 0 | 0 |

---

Educational project. Not financial advice.
