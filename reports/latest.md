# Stock prediction lab: latest report

Generated 2026-09-25 00:23 UTC.

> Rebuilt from history because their inputs changed: full, finbert, beat_full, gbm, beat_gbm, ensemble, beat_ensemble.

## Next-session calls

No open calls right now. New ones are made after each US market close.

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Historical replay, logistic, price only | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,338 | **50.4%** | 49.5%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,338 | **50.4%** | 49.5%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,748 | **50.1%** | 49.1%–51.1% | 52.3% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,748 | **51.5%** | 50.5%–52.5% | 52.3% | 49.8% | no | 0.2532 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Historical replay, logistic, all sources (VADER) | 10,338 | **51.4%** | 50.4%–52.4% | 50.4% | 49.8% | yes | 0.2541 |
| Historical replay, gradient boosting | 9,748 | **50.6%** | 49.6%–51.6% | 50.5% | 49.9% | within noise | 0.2544 |
| Historical replay, ensemble | 9,748 | **51.2%** | 50.2%–52.2% | 50.5% | 49.9% | within noise | 0.2519 |

*Brier* is the mean squared error of the probabilities (lower is better; always saying 50% scores 0.25).

![Rolling accuracy](rolling_accuracy.png)

## Calibration

Predictions grouped by confidence. For an honest model, the share that happened matches the prediction: of all the "55–60%" calls, about 57% should come true. *Average gap* is the weighted average distance between the two (expected calibration error). Uses live predictions once a model has 300, before that all scored ones.

**Up or down?**

| Predicted | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble |
|---|---|---|---|---|---|
| under 40% | 52.7% (n=245) | 50.6% (n=601) | 50.6% (n=601) | 55.0% (n=1,049) | 52.0% (n=473) |
| 40–45% | 52.1% (n=789) | 51.9% (n=1,082) | 51.9% (n=1,082) | 54.5% (n=1,024) | 53.1% (n=918) |
| 45–48% | 50.7% (n=1,283) | 50.4% (n=1,235) | 50.4% (n=1,235) | 50.6% (n=1,090) | 48.9% (n=1,181) |
| 48–50% | 52.6% (n=1,305) | 55.5% (n=1,133) | 55.5% (n=1,133) | 50.3% (n=965) | 51.3% (n=1,139) |
| 50–52% | 52.5% (n=1,692) | 51.1% (n=1,235) | 51.1% (n=1,235) | 47.4% (n=1,089) | 53.8% (n=1,384) |
| 52–55% | 52.3% (n=2,294) | 52.0% (n=1,739) | 52.0% (n=1,739) | 52.4% (n=1,577) | 52.6% (n=1,970) |
| 55–60% | 52.5% (n=2,092) | 52.3% (n=2,083) | 52.3% (n=2,083) | 52.6% (n=1,532) | 54.6% (n=1,871) |
| 60% or more | 52.4% (n=638) | 53.2% (n=1,230) | 53.2% (n=1,230) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=926) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,477) | 49.7% (n=1,260) | 47.5% (n=1,275) |
| 45–48% | 50.8% (n=1,428) | 50.0% (n=1,583) | 48.3% (n=1,671) |
| 48–50% | 49.7% (n=1,144) | 50.1% (n=1,382) | 51.4% (n=1,500) |
| 50–52% | 49.9% (n=1,183) | 50.7% (n=1,461) | 50.9% (n=1,449) |
| 52–55% | 52.2% (n=1,517) | 52.3% (n=1,570) | 50.9% (n=1,767) |
| 55–60% | 52.1% (n=1,656) | 50.0% (n=1,105) | 54.0% (n=1,289) |
| 60% or more | 52.7% (n=1,007) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

Both scorers read every headline from the first live run on; results appear here once those calls are scored.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,034 | 51.4% | 49.4% | 49.4% | 48.7% | 50.6% | 54.4% |
| AMZN | 1,034 | 49.5% | 49.9% | 49.9% | 49.0% | 49.0% | 50.8% |
| GOOGL | 1,034 | 51.4% | 49.3% | 49.3% | 51.1% | 51.9% | 54.3% |
| JPM | 1,034 | 50.8% | 50.8% | 50.8% | 51.1% | 51.2% | 54.0% |
| META | 1,034 | 52.7% | 52.6% | 52.6% | 48.8% | 51.0% | 50.8% |
| MSFT | 1,034 | 51.7% | 52.1% | 52.1% | 49.8% | 52.3% | 51.8% |
| NVDA | 1,034 | 49.4% | 49.6% | 49.6% | 51.6% | 51.7% | 53.0% |
| TSLA | 1,034 | 53.2% | 53.3% | 53.3% | 49.8% | 52.7% | 49.8% |
| UNH | 1,033 | 50.1% | 48.8% | 48.8% | 49.7% | 52.2% | 51.3% |
| XOM | 1,033 | 49.4% | 48.3% | 48.3% | 51.6% | 52.9% | 51.9% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,034 | 51.0% | 51.1% | 51.4% | 53.1% |
| AMZN | 1,034 | 49.1% | 52.6% | 50.7% | 47.8% |
| GOOGL | 1,034 | 49.9% | 51.3% | 50.7% | 53.5% |
| JPM | 1,034 | 52.7% | 49.0% | 49.9% | 53.5% |
| META | 1,034 | 51.3% | 48.2% | 50.2% | 49.0% |
| MSFT | 1,034 | 50.9% | 50.1% | 50.2% | 48.7% |
| NVDA | 1,034 | 51.9% | 52.5% | 52.8% | 52.3% |
| TSLA | 1,034 | 52.6% | 51.5% | 53.5% | 48.9% |
| UNH | 1,033 | 53.5% | 50.1% | 51.5% | 47.6% |
| XOM | 1,033 | 51.1% | 49.4% | 51.1% | 49.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,034 | +33.7% | +7.3% | 0.45 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,034 | +33.1% | +7.2% | 0.46 | 49.9% |
| Top 3 by logistic, all sources (FinBERT) | 1,034 | +33.1% | +7.2% | 0.46 | 49.9% |
| Top 3 by gradient boosting | 975 | +65.5% | +13.9% | 0.77 | 36.8% |
| Top 3 by ensemble | 975 | +35.4% | +8.1% | 0.52 | 45.7% |
| Buy every stock, every session | 1,034 | -0.3% | -0.1% | 0.08 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,034 | -24.8% | -6.7% | -0.42 | 46.7% |
| Top 3 by gradient boosting | 975 | -41.0% | -12.8% | -0.77 | 40.1% |
| Top 3 by ensemble | 975 | -15.9% | -4.4% | -0.21 | 46.2% |
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
| finbert | 10 | 0 | 239 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 994 |  |
| macro_yahoo | 1 | 0 | 1086 |  |
| prices | 11 | 0 | 11922 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 175 |  |

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
