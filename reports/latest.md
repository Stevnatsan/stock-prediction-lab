# Stock prediction lab: latest report

Generated 2026-10-09 07:23 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | AMZN | **56.8%** | **Buy at open** | 57.8% | **Outperform** | 45 | positive (+0.17) | negative (-0.22) |
| 2 | JPM | **55.8%** | **Buy at open** | 59.7% | **Outperform** | 22 | positive (+0.17) | positive (+0.06) |
| 3 | XOM | **54.9%** | **Buy at open** | 53.1% | **Outperform** | 21 | neutral (+0.02) | positive (+0.24) |
| 4 | GOOGL | **53.8%** | Stay out | 50.1% | – | 32 | positive (+0.05) | positive (+0.12) |
| 5 | UNH | **52.5%** | Stay out | 35.7% | – | 22 | positive (+0.16) | negative (-0.09) |
| 6 | AAPL | **50.1%** | Stay out | 52.3% | – | 36 | positive (+0.14) | positive (+0.15) |
| 7 | NVDA | **48.1%** | Stay out | 43.2% | – | 84 | positive (+0.12) | negative (-0.09) |
| 8 | MSFT | **47.6%** | Stay out | 48.5% | – | 24 | positive (+0.16) | neutral (-0.04) |
| 9 | META | **46.3%** | Stay out | 48.7% | – | 52 | neutral (+0.04) | neutral (-0.04) |
| 10 | TSLA | **44.5%** | Stay out | 41.9% | – | 23 | positive (+0.12) | positive (+0.12) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 53.0% | 52.0% | 51.9% | 52.3% | 48.2% | 49.4% | 50.1% | 50.9% |
| AMZN | 53.4% | 56.6% | 56.5% | 57.8% | 57.1% | 50.0% | 56.8% | 53.9% |
| GOOGL | 55.7% | 57.1% | 57.5% | 50.1% | 50.6% | 49.6% | 53.8% | 49.8% |
| JPM | 53.7% | 57.4% | 57.4% | 59.7% | 54.2% | 51.4% | 55.8% | 55.6% |
| META | 47.1% | 43.1% | 42.5% | 48.7% | 49.4% | 50.1% | 46.3% | 49.4% |
| MSFT | 51.3% | 42.3% | 43.0% | 48.5% | 52.9% | 50.7% | 47.6% | 49.6% |
| NVDA | 47.8% | 44.0% | 44.5% | 43.2% | 52.2% | 49.7% | 48.1% | 46.5% |
| TSLA | 43.9% | 39.9% | 39.9% | 41.9% | 49.1% | 48.2% | 44.5% | 45.1% |
| UNH | 51.9% | 48.6% | 48.3% | 35.7% | 56.5% | 51.7% | 52.5% | 43.7% |
| XOM | 50.8% | 62.1% | 62.6% | 53.1% | 47.8% | 47.6% | 54.9% | 50.4% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 100 | **56.0%** | 46.3%–65.7% | 50.0% | 54.0% | within noise | 0.2476 |
| Live, logistic, all sources (VADER) | 100 | **60.0%** | 50.4%–69.6% | 50.0% | 54.0% | within noise | 0.2438 |
| Live, logistic, all sources (FinBERT) | 100 | **61.0%** | 51.4%–70.6% | 50.0% | 54.0% | within noise | 0.2435 |
| Live, gradient boosting | 100 | **48.0%** | 38.2%–57.8% | 50.0% | 54.0% | no | 0.2489 |
| Live, ensemble | 100 | **58.0%** | 48.3%–67.7% | 50.0% | 54.0% | within noise | 0.2446 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 100 | **59.0%** | 49.4%–68.6% | 49.0% | 48.0% | within noise | 0.2480 |
| Live, gradient boosting | 100 | **59.0%** | 49.4%–68.6% | 49.0% | 48.0% | within noise | 0.2491 |
| Live, ensemble | 100 | **56.0%** | 46.3%–65.7% | 49.0% | 48.0% | within noise | 0.2472 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **51.4%** | 50.4%–52.3% | 50.4% | 49.8% | within noise | 0.2542 |
| Historical replay, gradient boosting | 9,758 | **50.6%** | 49.6%–51.6% | 50.5% | 49.9% | within noise | 0.2544 |
| Historical replay, ensemble | 9,758 | **51.2%** | 50.2%–52.2% | 50.5% | 49.9% | within noise | 0.2520 |

*Brier* is the mean squared error of the probabilities (lower is better; always saying 50% scores 0.25).

![Rolling accuracy](rolling_accuracy.png)

## Calibration

Predictions grouped by confidence. For an honest model, the share that happened matches the prediction: of all the "55–60%" calls, about 57% should come true. *Average gap* is the weighted average distance between the two (expected calibration error). Uses live predictions once a model has 300, before that all scored ones.

**Up or down?**

| Predicted | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble |
|---|---|---|---|---|---|
| under 40% | 53.0% (n=247) | 50.7% (n=617) | 50.7% (n=619) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=796) | 51.6% (n=1,108) | 51.6% (n=1,107) | 54.2% (n=1,040) | 52.6% (n=945) |
| 45–48% | 50.8% (n=1,294) | 50.5% (n=1,246) | 50.5% (n=1,247) | 50.7% (n=1,122) | 48.9% (n=1,204) |
| 48–50% | 52.4% (n=1,321) | 55.4% (n=1,145) | 55.3% (n=1,144) | 50.5% (n=990) | 51.3% (n=1,155) |
| 50–52% | 52.6% (n=1,706) | 51.1% (n=1,248) | 51.2% (n=1,247) | 47.2% (n=1,107) | 53.9% (n=1,402) |
| 52–55% | 52.3% (n=2,324) | 52.1% (n=1,752) | 52.1% (n=1,751) | 52.5% (n=1,590) | 52.6% (n=1,988) |
| 55–60% | 52.6% (n=2,121) | 52.4% (n=2,094) | 52.4% (n=2,095) | 52.7% (n=1,538) | 54.6% (n=1,878) |
| 60% or more | 52.3% (n=639) | 53.3% (n=1,238) | 53.3% (n=1,238) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.5% (n=931) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.0% (n=1,499) | 49.7% (n=1,260) | 47.5% (n=1,281) |
| 45–48% | 50.7% (n=1,444) | 50.0% (n=1,591) | 48.3% (n=1,696) |
| 48–50% | 49.6% (n=1,156) | 49.8% (n=1,423) | 51.3% (n=1,526) |
| 50–52% | 50.0% (n=1,192) | 51.0% (n=1,519) | 51.0% (n=1,467) |
| 52–55% | 52.4% (n=1,536) | 52.3% (n=1,573) | 50.8% (n=1,790) |
| 55–60% | 51.8% (n=1,672) | 50.0% (n=1,105) | 54.0% (n=1,301) |
| 60% or more | 52.8% (n=1,018) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 90 | 47.8% | -0.2% | 0.1% | -0.046 |
| FinBERT | 64 | 51.6% | -0.1% | 0.4% | -0.044 |

The two scorers agree on the direction of the mood on 69% of 110 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,045 | 51.5% | 49.6% | 49.6% | 48.5% | 50.5% | 54.5% |
| AMZN | 1,045 | 49.7% | 50.1% | 50.1% | 49.1% | 49.0% | 50.9% |
| GOOGL | 1,045 | 51.5% | 49.4% | 49.4% | 51.0% | 52.1% | 54.4% |
| JPM | 1,045 | 50.7% | 50.7% | 50.8% | 50.9% | 51.0% | 53.9% |
| META | 1,045 | 52.9% | 52.8% | 52.8% | 49.2% | 51.2% | 50.5% |
| MSFT | 1,045 | 51.6% | 52.1% | 52.1% | 49.9% | 52.2% | 51.9% |
| NVDA | 1,045 | 49.5% | 49.9% | 49.9% | 51.7% | 51.9% | 52.7% |
| TSLA | 1,045 | 53.0% | 53.2% | 53.2% | 49.8% | 52.6% | 49.8% |
| UNH | 1,044 | 50.2% | 48.6% | 48.6% | 49.8% | 52.1% | 51.4% |
| XOM | 1,044 | 49.6% | 48.6% | 48.6% | 51.2% | 53.1% | 52.1% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,045 | 51.1% | 51.0% | 51.5% | 53.1% |
| AMZN | 1,045 | 49.2% | 52.7% | 50.6% | 48.0% |
| GOOGL | 1,045 | 50.0% | 51.6% | 50.6% | 53.6% |
| JPM | 1,045 | 52.5% | 49.0% | 49.8% | 53.3% |
| META | 1,045 | 51.4% | 48.3% | 50.1% | 48.9% |
| MSFT | 1,045 | 51.0% | 50.3% | 50.3% | 48.8% |
| NVDA | 1,045 | 52.1% | 52.4% | 52.9% | 52.2% |
| TSLA | 1,045 | 52.5% | 51.4% | 53.5% | 48.8% |
| UNH | 1,044 | 53.4% | 50.4% | 51.5% | 47.6% |
| XOM | 1,044 | 51.2% | 49.4% | 51.3% | 49.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,045 | +37.3% | +7.9% | 0.48 | 50.8% |
| Top 3 by logistic, all sources (VADER) | 1,045 | +34.4% | +7.4% | 0.47 | 50.1% |
| Top 3 by logistic, all sources (FinBERT) | 1,045 | +34.4% | +7.4% | 0.47 | 50.1% |
| Top 3 by gradient boosting | 986 | +69.4% | +14.4% | 0.79 | 37.0% |
| Top 3 by ensemble | 986 | +35.7% | +8.1% | 0.52 | 45.9% |
| Buy every stock, every session | 1,045 | -0.9% | -0.2% | 0.08 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,045 | -24.2% | -6.5% | -0.40 | 46.9% |
| Top 3 by gradient boosting | 986 | -43.3% | -13.5% | -0.83 | 39.8% |
| Top 3 by ensemble | 986 | -15.3% | -4.2% | -0.20 | 46.3% |
| Every stock minus SPY | 1,045 | -53.6% | -16.9% | -2.40 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7680 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 311 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1002 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 139 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-08 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-08 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-08 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-08 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-08 | 0 | 0 | 0 |
| META | ok | 2026-10-08 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-08 | 0 | 0 | 0 |
| JPM | ok | 2026-10-08 | 0 | 0 | 0 |
| XOM | ok | 2026-10-08 | 0 | 0 | 0 |
| UNH | ok | 2026-10-08 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
