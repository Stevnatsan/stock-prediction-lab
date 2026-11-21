# Stock prediction lab: latest report

Generated 2026-11-21 08:16 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | TSLA | **62.5%** | **Buy at open** | 67.2% | **Outperform** | 40 | neutral (+0.00) | negative (-0.20) |
| 2 | AAPL | **57.2%** | **Buy at open** | 69.3% | **Outperform** | 46 | neutral (+0.02) | negative (-0.05) |
| 3 | AMZN | **56.7%** | **Buy at open** | 64.6% | **Outperform** | 54 | positive (+0.09) | negative (-0.21) |
| 4 | XOM | **49.0%** | Stay out | 49.4% | – | 17 | positive (+0.19) | positive (+0.23) |
| 5 | JPM | **45.4%** | Stay out | 60.4% | – | 29 | neutral (+0.04) | negative (-0.22) |
| 6 | UNH | **44.1%** | Stay out | 58.7% | – | 38 | positive (+0.09) | negative (-0.09) |
| 7 | MSFT | **39.6%** | Stay out | 49.1% | – | 36 | positive (+0.09) | neutral (+0.02) |
| 8 | META | **38.7%** | Stay out | 33.9% | – | 53 | positive (+0.14) | negative (-0.22) |
| 9 | GOOGL | **15.5%** | Stay out | 38.9% | – | 37 | neutral (+0.03) | negative (-0.26) |
| 10 | NVDA | **11.8%** | Stay out | 13.9% | – | 91 | negative (-0.08) | negative (-0.35) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 48.5% | 59.4% | 57.2% | 69.3% | 67.0% | 50.1% | 63.2% | 59.7% |
| AMZN | 51.8% | 55.4% | 56.7% | 64.6% | 61.8% | 50.1% | 58.6% | 57.4% |
| GOOGL | 24.5% | 17.1% | 15.5% | 38.9% | 64.4% | 50.7% | 40.8% | 44.8% |
| JPM | 49.6% | 47.7% | 45.4% | 60.4% | 65.1% | 50.1% | 56.4% | 55.3% |
| META | 46.4% | 37.9% | 38.7% | 33.9% | 62.8% | 50.7% | 50.3% | 42.3% |
| MSFT | 40.7% | 40.5% | 39.6% | 49.1% | 58.0% | 50.1% | 49.2% | 49.6% |
| NVDA | 16.9% | 11.8% | 11.8% | 13.9% | 63.1% | 50.9% | 37.5% | 32.4% |
| TSLA | 59.4% | 62.0% | 62.5% | 67.2% | 64.2% | 50.1% | 63.1% | 58.7% |
| UNH | 54.8% | 44.5% | 44.1% | 58.7% | 61.4% | 50.4% | 53.0% | 54.5% |
| XOM | 47.5% | 49.7% | 49.0% | 49.4% | 64.6% | 50.6% | 57.2% | 50.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 410 | **50.5%** | 45.6%–55.3% | 43.2% | 51.5% | no | 0.2511 |
| Live, logistic, all sources (VADER) | 410 | **53.2%** | 48.3%–58.0% | 43.2% | 51.5% | no | 0.2497 |
| Live, logistic, all sources (FinBERT) | 410 | **54.1%** | 49.3%–59.0% | 43.2% | 51.5% | no | 0.2489 |
| Live, gradient boosting | 410 | **52.0%** | 47.1%–56.8% | 43.2% | 51.5% | no | 0.2471 |
| Live, ensemble | 410 | **53.4%** | 48.6%–58.2% | 43.2% | 51.5% | no | 0.2459 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 410 | **54.9%** | 50.1%–59.7% | 46.8% | 48.3% | within noise | 0.2524 |
| Live, gradient boosting | 410 | **53.9%** | 49.1%–58.7% | 46.8% | 48.3% | within noise | 0.2492 |
| Live, ensemble | 410 | **54.6%** | 49.8%–59.5% | 46.8% | 48.3% | within noise | 0.2489 |
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
| under 40% | 35.3% (n=17) | 36.8% (n=57) | 36.7% (n=60) | 37.5% (n=8) | 25.0% (n=12) |
| 40–45% | 41.5% (n=53) | 41.7% (n=72) | 38.6% (n=70) | 24.1% (n=54) | 27.7% (n=65) |
| 45–48% | 39.3% (n=61) | 44.4% (n=45) | 48.1% (n=54) | 50.8% (n=63) | 46.4% (n=69) |
| 48–50% | 46.8% (n=47) | 39.5% (n=43) | 36.6% (n=41) | 44.4% (n=63) | 48.2% (n=56) |
| 50–52% | 44.4% (n=54) | 50.0% (n=34) | 50.0% (n=28) | 43.2% (n=74) | 40.9% (n=66) |
| 52–55% | 40.2% (n=92) | 32.1% (n=53) | 40.4% (n=47) | 39.5% (n=76) | 48.6% (n=72) |
| 55–60% | 52.4% (n=63) | 49.2% (n=59) | 45.2% (n=62) | 50.0% (n=58) | 50.0% (n=54) |
| 60% or more | 39.1% (n=23) | 55.3% (n=47) | 54.2% (n=48) | 71.4% (n=14) | 50.0% (n=16) |
| **Average gap** | **7.5 pts** | **6.8 pts** | **7.0 pts** | **9.1 pts** | **6.8 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 38.9% (n=54) | – | 44.4% (n=9) |
| 40–45% | 43.8% (n=80) | – | 38.9% (n=54) |
| 45–48% | 41.2% (n=51) | 36.1% (n=36) | 41.3% (n=92) |
| 48–50% | 46.7% (n=30) | 44.4% (n=169) | 47.8% (n=67) |
| 50–52% | 55.9% (n=34) | 51.0% (n=198) | 53.8% (n=65) |
| 52–55% | 58.2% (n=55) | 42.9% (n=7) | 52.3% (n=65) |
| 55–60% | 45.1% (n=51) | – | 50.0% (n=54) |
| 60% or more | 49.1% (n=55) | – | 25.0% (n=4) |
| **Average gap** | **6.1 pts** | **3.3 pts** | **4.0 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 344 | 45.6% | -0.4% | -1.8% | -0.018 |
| FinBERT | 272 | 50.4% | -0.2% | -0.6% | +0.046 |

The two scorers agree on the direction of the mood on 63% of 420 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 41 | 39.0% | 51.2% | 51.2% | 39.0% | 48.8% | 53.7% |
| AMZN | 41 | 58.5% | 53.7% | 53.7% | 43.9% | 43.9% | 43.9% |
| GOOGL | 41 | 61.0% | 58.5% | 58.5% | 63.4% | 75.6% | 36.6% |
| JPM | 41 | 46.3% | 48.8% | 58.5% | 34.1% | 39.0% | 34.1% |
| META | 41 | 43.9% | 56.1% | 53.7% | 56.1% | 56.1% | 36.6% |
| MSFT | 41 | 46.3% | 53.7% | 53.7% | 63.4% | 48.8% | 46.3% |
| NVDA | 41 | 58.5% | 61.0% | 61.0% | 58.5% | 63.4% | 26.8% |
| TSLA | 41 | 48.8% | 53.7% | 53.7% | 46.3% | 48.8% | 48.8% |
| UNH | 41 | 46.3% | 41.5% | 41.5% | 61.0% | 51.2% | 46.3% |
| XOM | 41 | 56.1% | 53.7% | 56.1% | 53.7% | 58.5% | 58.5% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 41 | 63.4% | 46.3% | 68.3% | 68.3% |
| AMZN | 41 | 48.8% | 56.1% | 48.8% | 48.8% |
| GOOGL | 41 | 53.7% | 61.0% | 51.2% | 41.5% |
| JPM | 41 | 46.3% | 58.5% | 46.3% | 41.5% |
| META | 41 | 56.1% | 41.5% | 51.2% | 34.1% |
| MSFT | 41 | 56.1% | 53.7% | 56.1% | 48.8% |
| NVDA | 41 | 58.5% | 46.3% | 58.5% | 29.3% |
| TSLA | 41 | 53.7% | 61.0% | 53.7% | 51.2% |
| UNH | 41 | 51.2% | 56.1% | 51.2% | 43.9% |
| XOM | 41 | 61.0% | 58.5% | 61.0% | 61.0% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,076 | +21.8% | +4.7% | 0.33 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,076 | +18.3% | +4.0% | 0.30 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,076 | +18.8% | +4.1% | 0.31 | 50.1% |
| Top 3 by gradient boosting | 1,017 | +50.7% | +10.7% | 0.62 | 36.8% |
| Top 3 by ensemble | 1,017 | +4.3% | +1.0% | 0.15 | 45.8% |
| Buy every stock, every session | 1,076 | -18.1% | -4.6% | -0.17 | 51.7% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,076 | -25.6% | -6.7% | -0.41 | 46.8% |
| Top 3 by gradient boosting | 1,017 | -43.6% | -13.2% | -0.82 | 38.6% |
| Top 3 by ensemble | 1,017 | -15.7% | -4.1% | -0.19 | 46.2% |
| Every stock minus SPY | 1,076 | -57.3% | -18.0% | -2.58 | 41.8% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7828 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 176 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 951 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 180 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-20 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-20 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-20 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-20 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-20 | 0 | 0 | 0 |
| META | ok | 2026-11-20 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-20 | 0 | 0 | 0 |
| JPM | ok | 2026-11-20 | 0 | 0 | 0 |
| XOM | ok | 2026-11-20 | 0 | 0 | 0 |
| UNH | ok | 2026-11-20 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
