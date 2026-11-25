# Stock prediction lab: latest report

Generated 2026-11-25 09:51 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **58.5%** | **Buy at open** | 54.1% | – | 20 | neutral (+0.04) | neutral (-0.04) |
| 2 | TSLA | **57.8%** | **Buy at open** | 56.7% | **Outperform** | 54 | neutral (+0.03) | neutral (-0.02) |
| 3 | UNH | **57.6%** | **Buy at open** | 55.8% | – | 15 | positive (+0.20) | negative (-0.10) |
| 4 | AAPL | **57.4%** | Stay out | 60.6% | **Outperform** | 43 | positive (+0.17) | positive (+0.12) |
| 5 | JPM | **53.8%** | Stay out | 56.0% | **Outperform** | 28 | positive (+0.17) | neutral (-0.00) |
| 6 | META | **53.5%** | Stay out | 47.0% | – | 67 | positive (+0.05) | negative (-0.11) |
| 7 | AMZN | **53.0%** | Stay out | 55.7% | – | 67 | positive (+0.15) | negative (-0.06) |
| 8 | MSFT | **47.4%** | Stay out | 51.1% | – | 41 | positive (+0.13) | negative (-0.11) |
| 9 | GOOGL | **26.0%** | Stay out | 35.0% | – | 33 | positive (+0.10) | neutral (+0.03) |
| 10 | NVDA | **18.1%** | Stay out | 13.9% | – | 97 | positive (+0.05) | negative (-0.18) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 53.5% | 56.4% | 57.4% | 60.6% | 51.9% | 49.7% | 54.1% | 55.1% |
| AMZN | 50.4% | 52.6% | 53.0% | 55.7% | 50.0% | 50.5% | 51.3% | 53.1% |
| GOOGL | 30.4% | 24.4% | 26.0% | 35.0% | 48.6% | 50.5% | 36.5% | 42.7% |
| JPM | 48.9% | 52.7% | 53.8% | 56.0% | 50.8% | 50.4% | 51.8% | 53.2% |
| META | 55.5% | 53.6% | 53.5% | 47.0% | 46.3% | 50.5% | 50.0% | 48.7% |
| MSFT | 51.3% | 47.9% | 47.4% | 51.1% | 50.7% | 50.5% | 49.3% | 50.8% |
| NVDA | 35.0% | 18.7% | 18.1% | 13.9% | 41.9% | 50.4% | 30.3% | 32.2% |
| TSLA | 48.3% | 57.0% | 57.8% | 56.7% | 51.7% | 49.9% | 54.4% | 53.3% |
| UNH | 57.5% | 58.9% | 57.6% | 55.8% | 47.7% | 50.0% | 53.3% | 52.9% |
| XOM | 58.0% | 58.0% | 58.5% | 54.1% | 49.7% | 50.5% | 53.8% | 52.3% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 430 | **51.2%** | 46.4%–55.9% | 43.7% | 51.9% | no | 0.2498 |
| Live, logistic, all sources (VADER) | 430 | **53.7%** | 49.0%–58.4% | 43.7% | 51.9% | no | 0.2492 |
| Live, logistic, all sources (FinBERT) | 430 | **54.4%** | 49.7%–59.1% | 43.7% | 51.9% | no | 0.2484 |
| Live, gradient boosting | 430 | **51.2%** | 46.4%–55.9% | 43.7% | 51.9% | no | 0.2491 |
| Live, ensemble | 430 | **53.3%** | 48.5%–58.0% | 43.7% | 51.9% | no | 0.2462 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 430 | **55.3%** | 50.6%–60.0% | 46.7% | 48.1% | within noise | 0.2518 |
| Live, gradient boosting | 430 | **53.5%** | 48.8%–58.2% | 46.7% | 48.1% | within noise | 0.2492 |
| Live, ensemble | 430 | **55.1%** | 50.4%–59.8% | 46.7% | 48.1% | within noise | 0.2485 |
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
| under 40% | 35.0% (n=20) | 39.7% (n=63) | 38.8% (n=67) | 44.4% (n=9) | 28.6% (n=14) |
| 40–45% | 41.8% (n=55) | 41.9% (n=74) | 40.3% (n=72) | 25.5% (n=55) | 28.4% (n=67) |
| 45–48% | 40.0% (n=65) | 41.7% (n=48) | 46.4% (n=56) | 52.3% (n=65) | 46.4% (n=69) |
| 48–50% | 46.0% (n=50) | 38.6% (n=44) | 34.9% (n=43) | 44.4% (n=63) | 49.2% (n=59) |
| 50–52% | 43.6% (n=55) | 51.4% (n=35) | 50.0% (n=28) | 43.2% (n=74) | 41.8% (n=67) |
| 52–55% | 40.9% (n=93) | 32.1% (n=53) | 40.4% (n=47) | 39.5% (n=76) | 49.3% (n=75) |
| 55–60% | 55.2% (n=67) | 48.4% (n=62) | 44.6% (n=65) | 48.3% (n=60) | 46.7% (n=60) |
| 60% or more | 40.0% (n=25) | 58.8% (n=51) | 57.7% (n=52) | 60.7% (n=28) | 57.9% (n=19) |
| **Average gap** | **6.8 pts** | **7.3 pts** | **6.8 pts** | **9.1 pts** | **6.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 40.0% (n=60) | – | 40.0% (n=10) |
| 40–45% | 43.2% (n=81) | – | 40.7% (n=59) |
| 45–48% | 41.2% (n=51) | 36.1% (n=36) | 40.9% (n=93) |
| 48–50% | 42.4% (n=33) | 44.5% (n=173) | 45.7% (n=70) |
| 50–52% | 54.3% (n=35) | 50.5% (n=214) | 53.0% (n=66) |
| 52–55% | 58.2% (n=55) | 42.9% (n=7) | 53.7% (n=67) |
| 55–60% | 47.2% (n=53) | – | 50.8% (n=61) |
| 60% or more | 50.0% (n=62) | – | 25.0% (n=4) |
| **Average gap** | **6.1 pts** | **3.1 pts** | **3.8 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 358 | 46.1% | -0.4% | -1.8% | -0.027 |
| FinBERT | 285 | 49.8% | -0.2% | -0.5% | +0.035 |

The two scorers agree on the direction of the mood on 62% of 440 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 43 | 39.5% | 53.5% | 53.5% | 39.5% | 51.2% | 55.8% |
| AMZN | 43 | 58.1% | 53.5% | 53.5% | 41.9% | 41.9% | 41.9% |
| GOOGL | 43 | 62.8% | 60.5% | 60.5% | 60.5% | 74.4% | 34.9% |
| JPM | 43 | 46.5% | 48.8% | 58.1% | 32.6% | 37.2% | 34.9% |
| META | 43 | 41.9% | 53.5% | 51.2% | 58.1% | 55.8% | 39.5% |
| MSFT | 43 | 46.5% | 53.5% | 53.5% | 62.8% | 48.8% | 46.5% |
| NVDA | 43 | 58.1% | 60.5% | 60.5% | 55.8% | 62.8% | 25.6% |
| TSLA | 43 | 51.2% | 55.8% | 55.8% | 48.8% | 51.2% | 51.2% |
| UNH | 43 | 48.8% | 41.9% | 39.5% | 60.5% | 51.2% | 48.8% |
| XOM | 43 | 58.1% | 55.8% | 58.1% | 51.2% | 58.1% | 58.1% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 43 | 65.1% | 46.5% | 69.8% | 69.8% |
| AMZN | 43 | 48.8% | 53.5% | 48.8% | 46.5% |
| GOOGL | 43 | 55.8% | 58.1% | 53.5% | 39.5% |
| JPM | 43 | 44.2% | 58.1% | 44.2% | 41.9% |
| META | 43 | 55.8% | 44.2% | 51.2% | 34.9% |
| MSFT | 43 | 55.8% | 53.5% | 55.8% | 48.8% |
| NVDA | 43 | 58.1% | 44.2% | 58.1% | 27.9% |
| TSLA | 43 | 53.5% | 62.8% | 53.5% | 51.2% |
| UNH | 43 | 53.5% | 55.8% | 53.5% | 46.5% |
| XOM | 43 | 62.8% | 58.1% | 62.8% | 60.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,078 | +25.9% | +5.5% | 0.36 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,078 | +19.7% | +4.3% | 0.31 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,078 | +20.2% | +4.4% | 0.32 | 50.2% |
| Top 3 by gradient boosting | 1,019 | +49.6% | +10.5% | 0.61 | 36.8% |
| Top 3 by ensemble | 1,019 | +4.5% | +1.1% | 0.15 | 45.8% |
| Buy every stock, every session | 1,078 | -17.8% | -4.5% | -0.17 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,078 | -25.0% | -6.5% | -0.39 | 46.9% |
| Top 3 by gradient boosting | 1,019 | -43.6% | -13.2% | -0.82 | 38.6% |
| Top 3 by ensemble | 1,019 | -15.1% | -4.0% | -0.18 | 46.3% |
| Every stock minus SPY | 1,078 | -57.3% | -18.0% | -2.58 | 41.8% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7828 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 288 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 952 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 183 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-24 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-24 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-24 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-24 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-24 | 0 | 0 | 0 |
| META | ok | 2026-11-24 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-24 | 0 | 0 | 0 |
| JPM | ok | 2026-11-24 | 0 | 0 | 0 |
| XOM | ok | 2026-11-24 | 0 | 0 | 0 |
| UNH | ok | 2026-11-24 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
