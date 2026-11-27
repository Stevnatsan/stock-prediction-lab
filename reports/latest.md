# Stock prediction lab: latest report

Generated 2026-11-27 04:14 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | MSFT | **62.2%** | **Buy at open** | 57.7% | **Outperform** | 36 | positive (+0.09) | negative (-0.15) |
| 2 | AAPL | **61.0%** | **Buy at open** | 58.4% | **Outperform** | 38 | positive (+0.10) | negative (-0.05) |
| 3 | META | **58.3%** | **Buy at open** | 47.5% | – | 38 | positive (+0.09) | neutral (-0.03) |
| 4 | JPM | **57.9%** | Stay out | 57.1% | **Outperform** | 31 | positive (+0.08) | negative (-0.08) |
| 5 | AMZN | **54.8%** | Stay out | 51.0% | – | 44 | positive (+0.10) | neutral (-0.04) |
| 6 | UNH | **51.9%** | Stay out | 45.0% | – | 16 | positive (+0.22) | positive (+0.18) |
| 7 | TSLA | **48.3%** | Stay out | 49.5% | – | 40 | positive (+0.13) | negative (-0.22) |
| 8 | XOM | **39.6%** | Stay out | 43.9% | – | 30 | positive (+0.26) | positive (+0.11) |
| 9 | NVDA | **29.7%** | Stay out | 18.3% | – | 89 | negative (-0.06) | negative (-0.26) |
| 10 | GOOGL | **18.1%** | Stay out | 44.6% | – | 50 | positive (+0.10) | negative (-0.20) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 53.5% | 59.3% | 61.0% | 58.4% | 58.8% | 50.0% | 59.1% | 54.2% |
| AMZN | 49.2% | 56.5% | 54.8% | 51.0% | 53.5% | 50.4% | 55.0% | 50.7% |
| GOOGL | 23.6% | 19.8% | 18.1% | 44.6% | 50.6% | 50.4% | 35.2% | 47.5% |
| JPM | 51.4% | 58.0% | 57.9% | 57.1% | 55.6% | 50.4% | 56.8% | 53.7% |
| META | 56.4% | 58.4% | 58.3% | 47.5% | 50.3% | 50.3% | 54.3% | 48.9% |
| MSFT | 52.5% | 62.1% | 62.2% | 57.7% | 55.6% | 50.7% | 58.8% | 54.2% |
| NVDA | 39.0% | 28.9% | 29.7% | 18.3% | 50.8% | 50.4% | 39.8% | 34.4% |
| TSLA | 44.5% | 49.4% | 48.3% | 49.5% | 56.2% | 50.4% | 52.8% | 49.9% |
| UNH | 50.7% | 52.3% | 51.9% | 45.0% | 50.8% | 50.3% | 51.5% | 47.6% |
| XOM | 43.5% | 39.9% | 39.6% | 43.9% | 51.5% | 50.4% | 45.7% | 47.1% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 440 | **51.1%** | 46.5%–55.8% | 44.8% | 52.0% | no | 0.2506 |
| Live, logistic, all sources (VADER) | 440 | **53.9%** | 49.2%–58.5% | 44.8% | 52.0% | no | 0.2505 |
| Live, logistic, all sources (FinBERT) | 440 | **54.5%** | 49.9%–59.2% | 44.8% | 52.0% | no | 0.2496 |
| Live, gradient boosting | 440 | **51.1%** | 46.5%–55.8% | 44.8% | 52.0% | no | 0.2494 |
| Live, ensemble | 440 | **53.2%** | 48.5%–57.8% | 44.8% | 52.0% | no | 0.2469 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 440 | **54.8%** | 50.1%–59.4% | 47.0% | 47.7% | within noise | 0.2535 |
| Live, gradient boosting | 440 | **53.4%** | 48.7%–58.1% | 47.0% | 47.7% | within noise | 0.2492 |
| Live, ensemble | 440 | **54.5%** | 49.9%–59.2% | 47.0% | 47.7% | within noise | 0.2492 |
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
| under 40% | 40.9% (n=22) | 41.5% (n=65) | 40.6% (n=69) | 44.4% (n=9) | 37.5% (n=16) |
| 40–45% | 41.8% (n=55) | 41.9% (n=74) | 40.3% (n=72) | 26.8% (n=56) | 28.4% (n=67) |
| 45–48% | 40.0% (n=65) | 42.9% (n=49) | 47.4% (n=57) | 53.7% (n=67) | 46.4% (n=69) |
| 48–50% | 48.1% (n=52) | 38.6% (n=44) | 34.9% (n=43) | 45.5% (n=66) | 50.8% (n=61) |
| 50–52% | 45.6% (n=57) | 51.4% (n=35) | 50.0% (n=28) | 46.2% (n=78) | 43.5% (n=69) |
| 52–55% | 41.5% (n=94) | 35.7% (n=56) | 44.0% (n=50) | 39.5% (n=76) | 50.6% (n=79) |
| 55–60% | 55.7% (n=70) | 50.0% (n=66) | 46.4% (n=69) | 48.3% (n=60) | 46.7% (n=60) |
| 60% or more | 40.0% (n=25) | 58.8% (n=51) | 57.7% (n=52) | 60.7% (n=28) | 57.9% (n=19) |
| **Average gap** | **6.3 pts** | **6.8 pts** | **6.6 pts** | **8.4 pts** | **5.9 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 41.9% (n=62) | – | 45.5% (n=11) |
| 40–45% | 43.2% (n=81) | – | 41.7% (n=60) |
| 45–48% | 42.3% (n=52) | 36.1% (n=36) | 40.9% (n=93) |
| 48–50% | 42.4% (n=33) | 44.9% (n=176) | 46.5% (n=71) |
| 50–52% | 52.8% (n=36) | 50.7% (n=221) | 52.2% (n=67) |
| 52–55% | 57.1% (n=56) | 42.9% (n=7) | 54.2% (n=72) |
| 55–60% | 49.1% (n=57) | – | 50.0% (n=62) |
| 60% or more | 49.2% (n=63) | – | 25.0% (n=4) |
| **Average gap** | **5.9 pts** | **2.8 pts** | **3.7 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 366 | 47.3% | -0.3% | -1.8% | -0.032 |
| FinBERT | 291 | 49.1% | -0.2% | -0.3% | +0.018 |

The two scorers agree on the direction of the mood on 62% of 450 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 44 | 40.9% | 54.5% | 54.5% | 40.9% | 52.3% | 56.8% |
| AMZN | 44 | 59.1% | 54.5% | 54.5% | 40.9% | 43.2% | 43.2% |
| GOOGL | 44 | 61.4% | 59.1% | 59.1% | 59.1% | 72.7% | 36.4% |
| JPM | 44 | 45.5% | 50.0% | 59.1% | 34.1% | 38.6% | 36.4% |
| META | 44 | 43.2% | 54.5% | 52.3% | 56.8% | 54.5% | 40.9% |
| MSFT | 44 | 47.7% | 52.3% | 52.3% | 63.6% | 47.7% | 47.7% |
| NVDA | 44 | 56.8% | 59.1% | 59.1% | 54.5% | 61.4% | 27.3% |
| TSLA | 44 | 50.0% | 56.8% | 56.8% | 50.0% | 52.3% | 52.3% |
| UNH | 44 | 50.0% | 43.2% | 40.9% | 59.1% | 52.3% | 50.0% |
| XOM | 44 | 56.8% | 54.5% | 56.8% | 52.3% | 56.8% | 56.8% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 44 | 63.6% | 47.7% | 68.2% | 68.2% |
| AMZN | 44 | 47.7% | 52.3% | 47.7% | 45.5% |
| GOOGL | 44 | 54.5% | 59.1% | 52.3% | 40.9% |
| JPM | 44 | 45.5% | 59.1% | 45.5% | 43.2% |
| META | 44 | 54.5% | 45.5% | 50.0% | 36.4% |
| MSFT | 44 | 54.5% | 52.3% | 54.5% | 47.7% |
| NVDA | 44 | 56.8% | 45.5% | 56.8% | 29.5% |
| TSLA | 44 | 54.5% | 61.4% | 54.5% | 52.3% |
| UNH | 44 | 54.5% | 54.5% | 54.5% | 47.7% |
| XOM | 44 | 61.4% | 56.8% | 61.4% | 59.1% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,079 | +29.3% | +6.2% | 0.39 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,079 | +21.6% | +4.7% | 0.33 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,079 | +22.1% | +4.8% | 0.34 | 50.2% |
| Top 3 by gradient boosting | 1,020 | +49.4% | +10.4% | 0.61 | 36.7% |
| Top 3 by ensemble | 1,020 | +5.6% | +1.3% | 0.17 | 45.9% |
| Buy every stock, every session | 1,079 | -16.1% | -4.0% | -0.14 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,079 | -25.2% | -6.6% | -0.40 | 46.9% |
| Top 3 by gradient boosting | 1,020 | -43.6% | -13.2% | -0.82 | 38.5% |
| Top 3 by ensemble | 1,020 | -15.2% | -4.0% | -0.18 | 46.3% |
| Every stock minus SPY | 1,079 | -57.2% | -18.0% | -2.57 | 41.9% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7828 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 507 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 966 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 999 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 186 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-25 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-25 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-25 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-25 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-25 | 0 | 0 | 0 |
| META | ok | 2026-11-25 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-25 | 0 | 0 | 0 |
| JPM | ok | 2026-11-25 | 0 | 0 | 0 |
| XOM | ok | 2026-11-25 | 0 | 0 | 0 |
| UNH | ok | 2026-11-25 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
