# Stock prediction lab: latest report

Generated 2026-11-07 07:08 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | AAPL | **64.4%** | **Buy at open** | 63.2% | **Outperform** | 31 | negative (-0.13) | negative (-0.20) |
| 2 | AMZN | **58.7%** | **Buy at open** | 52.9% | – | 31 | positive (+0.11) | negative (-0.07) |
| 3 | UNH | **56.3%** | **Buy at open** | 50.7% | – | 14 | positive (+0.21) | positive (+0.09) |
| 4 | TSLA | **56.2%** | Stay out | 61.9% | **Outperform** | 39 | neutral (-0.01) | neutral (-0.01) |
| 5 | META | **56.0%** | Stay out | 38.1% | – | 43 | positive (+0.10) | negative (-0.08) |
| 6 | XOM | **51.2%** | Stay out | 42.6% | – | 15 | positive (+0.25) | positive (+0.19) |
| 7 | NVDA | **50.3%** | Stay out | 45.0% | – | 84 | neutral (-0.01) | negative (-0.10) |
| 8 | GOOGL | **49.3%** | Stay out | 68.4% | **Outperform** | 38 | positive (+0.11) | neutral (-0.05) |
| 9 | JPM | **49.0%** | Stay out | 42.8% | – | 22 | positive (+0.09) | positive (+0.13) |
| 10 | MSFT | **46.9%** | Stay out | 49.3% | – | 35 | positive (+0.08) | negative (-0.11) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 54.4% | 70.9% | 65.0% | 63.2% | 58.0% | 50.4% | 64.4% | 56.8% |
| AMZN | 52.1% | 57.4% | 57.0% | 52.9% | 60.0% | 50.1% | 58.7% | 51.5% |
| GOOGL | 42.3% | 38.8% | 38.5% | 68.4% | 59.8% | 51.5% | 49.3% | 59.9% |
| JPM | 53.2% | 40.8% | 40.5% | 42.8% | 57.3% | 50.4% | 49.0% | 46.6% |
| META | 57.8% | 52.2% | 53.0% | 38.1% | 59.8% | 51.5% | 56.0% | 44.8% |
| MSFT | 48.0% | 35.8% | 38.3% | 49.3% | 58.0% | 50.1% | 46.9% | 49.7% |
| NVDA | 44.8% | 40.4% | 41.5% | 45.0% | 60.3% | 50.6% | 50.3% | 47.8% |
| TSLA | 49.0% | 53.0% | 54.9% | 61.9% | 59.3% | 51.5% | 56.2% | 56.7% |
| UNH | 52.8% | 54.6% | 53.3% | 50.7% | 58.0% | 50.8% | 56.3% | 50.8% |
| XOM | 47.7% | 42.3% | 43.9% | 42.6% | 60.0% | 51.5% | 51.2% | 47.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 310 | **52.9%** | 47.3%–58.5% | 46.8% | 47.4% | no | 0.2480 |
| Live, logistic, all sources (VADER) | 310 | **53.5%** | 48.0%–59.1% | 46.8% | 47.4% | within noise | 0.2499 |
| Live, logistic, all sources (FinBERT) | 310 | **53.9%** | 48.3%–59.4% | 46.8% | 47.4% | within noise | 0.2497 |
| Live, gradient boosting | 310 | **50.3%** | 44.8%–55.9% | 46.8% | 47.4% | no | 0.2485 |
| Live, ensemble | 310 | **53.5%** | 48.0%–59.1% | 46.8% | 47.4% | within noise | 0.2471 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 310 | **54.5%** | 49.0%–60.1% | 47.7% | 46.1% | within noise | 0.2532 |
| Live, gradient boosting | 310 | **53.9%** | 48.3%–59.4% | 47.7% | 46.1% | within noise | 0.2494 |
| Live, ensemble | 310 | **54.5%** | 49.0%–60.1% | 47.7% | 46.1% | within noise | 0.2495 |
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
| under 40% | 50.0% (n=12) | 43.6% (n=39) | 43.9% (n=41) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 40.0% (n=40) | 41.8% (n=55) | 41.5% (n=53) | 31.7% (n=41) | 34.0% (n=53) |
| 45–48% | 42.9% (n=42) | 51.4% (n=35) | 50.0% (n=42) | 55.6% (n=54) | 48.2% (n=56) |
| 48–50% | 44.2% (n=43) | 37.5% (n=32) | 36.7% (n=30) | 49.1% (n=57) | 48.8% (n=43) |
| 50–52% | 48.8% (n=43) | 51.9% (n=27) | 50.0% (n=26) | 43.3% (n=60) | 44.2% (n=43) |
| 52–55% | 40.3% (n=67) | 33.3% (n=39) | 38.2% (n=34) | 43.8% (n=48) | 51.9% (n=54) |
| 55–60% | 63.8% (n=47) | 54.8% (n=42) | 52.4% (n=42) | 51.5% (n=33) | 52.4% (n=42) |
| 60% or more | 50.0% (n=16) | 61.0% (n=41) | 59.5% (n=42) | 70.0% (n=10) | 58.3% (n=12) |
| **Average gap** | **6.9 pts** | **6.4 pts** | **6.0 pts** | **6.9 pts** | **4.0 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 42.5% (n=40) | – | 66.7% (n=6) |
| 40–45% | 41.9% (n=62) | – | 37.5% (n=40) |
| 45–48% | 43.6% (n=39) | 39.4% (n=33) | 40.5% (n=74) |
| 48–50% | 50.0% (n=28) | 45.8% (n=142) | 50.9% (n=55) |
| 50–52% | 57.7% (n=26) | 52.7% (n=131) | 56.2% (n=48) |
| 52–55% | 57.5% (n=40) | 25.0% (n=4) | 48.9% (n=45) |
| 55–60% | 44.1% (n=34) | – | 53.8% (n=39) |
| 60% or more | 51.2% (n=41) | – | 33.3% (n=3) |
| **Average gap** | **5.9 pts** | **3.7 pts** | **5.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 264 | 47.7% | -0.3% | -0.2% | -0.051 |
| FinBERT | 208 | 47.1% | -0.2% | -0.0% | -0.086 |

The two scorers agree on the direction of the mood on 66% of 320 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 31 | 41.9% | 54.8% | 51.6% | 32.3% | 45.2% | 61.3% |
| AMZN | 31 | 58.1% | 54.8% | 54.8% | 48.4% | 48.4% | 48.4% |
| GOOGL | 31 | 58.1% | 51.6% | 51.6% | 64.5% | 71.0% | 41.9% |
| JPM | 31 | 51.6% | 41.9% | 48.4% | 35.5% | 35.5% | 38.7% |
| META | 31 | 48.4% | 58.1% | 54.8% | 61.3% | 61.3% | 38.7% |
| MSFT | 31 | 48.4% | 54.8% | 54.8% | 61.3% | 51.6% | 48.4% |
| NVDA | 31 | 54.8% | 58.1% | 58.1% | 54.8% | 58.1% | 25.8% |
| TSLA | 31 | 54.8% | 54.8% | 54.8% | 35.5% | 45.2% | 51.6% |
| UNH | 31 | 48.4% | 45.2% | 45.2% | 61.3% | 54.8% | 51.6% |
| XOM | 31 | 64.5% | 61.3% | 64.5% | 48.4% | 64.5% | 61.3% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 31 | 58.1% | 41.9% | 64.5% | 64.5% |
| AMZN | 31 | 45.2% | 61.3% | 45.2% | 51.6% |
| GOOGL | 31 | 54.8% | 61.3% | 51.6% | 45.2% |
| JPM | 31 | 48.4% | 61.3% | 48.4% | 45.2% |
| META | 31 | 61.3% | 38.7% | 54.8% | 35.5% |
| MSFT | 31 | 58.1% | 54.8% | 58.1% | 54.8% |
| NVDA | 31 | 54.8% | 45.2% | 54.8% | 29.0% |
| TSLA | 31 | 51.6% | 58.1% | 51.6% | 48.4% |
| UNH | 31 | 51.6% | 54.8% | 54.8% | 45.2% |
| XOM | 31 | 61.3% | 61.3% | 61.3% | 58.1% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,066 | +38.1% | +7.9% | 0.47 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,066 | +33.6% | +7.1% | 0.45 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,066 | +35.2% | +7.4% | 0.47 | 50.4% |
| Top 3 by gradient boosting | 1,007 | +58.5% | +12.2% | 0.68 | 36.8% |
| Top 3 by ensemble | 1,007 | +30.8% | +6.9% | 0.46 | 46.0% |
| Buy every stock, every session | 1,066 | -8.4% | -2.1% | -0.03 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,066 | -24.5% | -6.4% | -0.40 | 46.8% |
| Top 3 by gradient boosting | 1,007 | -43.4% | -13.3% | -0.82 | 38.9% |
| Top 3 by ensemble | 1,007 | -14.5% | -3.9% | -0.17 | 46.2% |
| Every stock minus SPY | 1,066 | -55.3% | -17.3% | -2.48 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7843 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 158 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 944 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 999 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 173 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-06 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-06 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-06 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-06 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-06 | 0 | 0 | 0 |
| META | ok | 2026-11-06 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-06 | 0 | 0 | 0 |
| JPM | ok | 2026-11-06 | 0 | 0 | 0 |
| XOM | ok | 2026-11-06 | 0 | 0 | 0 |
| UNH | ok | 2026-11-06 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
