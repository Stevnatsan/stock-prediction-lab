# Stock prediction lab: latest report

Generated 2026-11-06 02:25 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | TSLA | **70.6%** | **Buy at open** | 73.6% | **Outperform** | 42 | neutral (-0.04) | negative (-0.36) |
| 2 | AMZN | **65.4%** | **Buy at open** | 65.5% | **Outperform** | 45 | positive (+0.14) | neutral (-0.04) |
| 3 | UNH | **64.0%** | **Buy at open** | 49.2% | – | 17 | positive (+0.29) | neutral (-0.00) |
| 4 | META | **63.9%** | Stay out | 58.5% | – | 43 | positive (+0.07) | negative (-0.13) |
| 5 | JPM | **62.8%** | Stay out | 51.4% | – | 36 | positive (+0.17) | negative (-0.10) |
| 6 | GOOGL | **60.5%** | Stay out | 69.9% | **Outperform** | 34 | neutral (+0.03) | neutral (+0.04) |
| 7 | MSFT | **57.7%** | Stay out | 55.0% | – | 52 | positive (+0.14) | neutral (-0.04) |
| 8 | XOM | **55.4%** | Stay out | 40.4% | – | 15 | positive (+0.16) | positive (+0.19) |
| 9 | AAPL | **54.4%** | Stay out | 43.3% | – | 38 | neutral (+0.05) | negative (-0.07) |
| 10 | NVDA | **48.7%** | Stay out | 34.6% | – | 75 | neutral (+0.00) | negative (-0.22) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 42.4% | 45.7% | 45.0% | 43.3% | 63.0% | 50.5% | 54.4% | 46.9% |
| AMZN | 57.7% | 68.0% | 67.9% | 65.5% | 62.9% | 49.9% | 65.4% | 57.7% |
| GOOGL | 50.1% | 54.9% | 57.2% | 69.9% | 66.2% | 51.4% | 60.5% | 60.6% |
| JPM | 56.4% | 62.2% | 62.0% | 51.4% | 63.3% | 50.5% | 62.8% | 50.9% |
| META | 57.8% | 61.5% | 62.0% | 58.5% | 66.2% | 51.4% | 63.9% | 54.9% |
| MSFT | 44.4% | 52.4% | 53.7% | 55.0% | 63.0% | 49.9% | 57.7% | 52.4% |
| NVDA | 34.4% | 34.5% | 34.3% | 34.6% | 62.9% | 50.4% | 48.7% | 42.5% |
| TSLA | 68.7% | 78.2% | 79.2% | 73.6% | 62.9% | 50.8% | 70.6% | 62.2% |
| UNH | 62.2% | 64.1% | 62.5% | 49.2% | 63.9% | 49.4% | 64.0% | 49.3% |
| XOM | 49.8% | 45.5% | 45.7% | 40.4% | 65.3% | 50.5% | 55.4% | 45.4% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 300 | **53.0%** | 47.4%–58.6% | 46.0% | 48.0% | no | 0.2489 |
| Live, logistic, all sources (VADER) | 300 | **53.3%** | 47.7%–59.0% | 46.0% | 48.0% | no | 0.2510 |
| Live, logistic, all sources (FinBERT) | 300 | **53.7%** | 48.0%–59.3% | 46.0% | 48.0% | no | 0.2507 |
| Live, gradient boosting | 300 | **49.7%** | 44.0%–55.3% | 46.0% | 48.0% | no | 0.2497 |
| Live, ensemble | 300 | **52.7%** | 47.0%–58.3% | 46.0% | 48.0% | no | 0.2483 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 300 | **54.7%** | 49.0%–60.3% | 47.0% | 46.0% | within noise | 0.2528 |
| Live, gradient boosting | 300 | **53.7%** | 48.0%–59.3% | 47.0% | 46.0% | within noise | 0.2494 |
| Live, ensemble | 300 | **54.7%** | 49.0%–60.3% | 47.0% | 46.0% | within noise | 0.2493 |
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
| under 40% | 54.5% (n=11) | 44.7% (n=38) | 45.0% (n=40) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 36.8% (n=38) | 41.8% (n=55) | 41.5% (n=53) | 31.7% (n=41) | 34.0% (n=53) |
| 45–48% | 42.9% (n=42) | 48.5% (n=33) | 47.5% (n=40) | 55.6% (n=54) | 48.2% (n=56) |
| 48–50% | 42.9% (n=42) | 37.5% (n=32) | 36.7% (n=30) | 49.1% (n=57) | 50.0% (n=42) |
| 50–52% | 50.0% (n=42) | 51.9% (n=27) | 50.0% (n=26) | 43.3% (n=60) | 44.2% (n=43) |
| 52–55% | 40.3% (n=67) | 32.4% (n=37) | 36.4% (n=33) | 43.8% (n=48) | 50.9% (n=53) |
| 55–60% | 63.6% (n=44) | 54.8% (n=42) | 53.7% (n=41) | 51.5% (n=33) | 50.0% (n=40) |
| 60% or more | 42.9% (n=14) | 58.3% (n=36) | 56.8% (n=37) | – | 50.0% (n=6) |
| **Average gap** | **7.8 pts** | **6.5 pts** | **6.2 pts** | **6.9 pts** | **4.8 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 43.6% (n=39) | – | 66.7% (n=6) |
| 40–45% | 40.0% (n=60) | – | 38.5% (n=39) |
| 45–48% | 43.6% (n=39) | 39.4% (n=33) | 38.9% (n=72) |
| 48–50% | 48.1% (n=27) | 45.3% (n=139) | 50.0% (n=54) |
| 50–52% | 56.0% (n=25) | 51.6% (n=124) | 55.3% (n=47) |
| 52–55% | 56.4% (n=39) | 25.0% (n=4) | 46.5% (n=43) |
| 55–60% | 42.4% (n=33) | – | 55.3% (n=38) |
| 60% or more | 52.6% (n=38) | – | 0.0% (n=1) |
| **Average gap** | **6.0 pts** | **3.5 pts** | **5.3 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 257 | 46.7% | -0.3% | -0.2% | -0.058 |
| FinBERT | 202 | 47.5% | -0.2% | -0.0% | -0.084 |

The two scorers agree on the direction of the mood on 66% of 310 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 30 | 43.3% | 56.7% | 53.3% | 30.0% | 43.3% | 60.0% |
| AMZN | 30 | 60.0% | 56.7% | 56.7% | 50.0% | 50.0% | 50.0% |
| GOOGL | 30 | 60.0% | 53.3% | 53.3% | 66.7% | 73.3% | 43.3% |
| JPM | 30 | 50.0% | 40.0% | 46.7% | 33.3% | 33.3% | 36.7% |
| META | 30 | 46.7% | 56.7% | 53.3% | 60.0% | 60.0% | 36.7% |
| MSFT | 30 | 50.0% | 53.3% | 53.3% | 60.0% | 50.0% | 46.7% |
| NVDA | 30 | 53.3% | 56.7% | 56.7% | 56.7% | 56.7% | 26.7% |
| TSLA | 30 | 53.3% | 53.3% | 53.3% | 33.3% | 43.3% | 50.0% |
| UNH | 30 | 46.7% | 43.3% | 43.3% | 60.0% | 53.3% | 50.0% |
| XOM | 30 | 66.7% | 63.3% | 66.7% | 46.7% | 63.3% | 60.0% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 30 | 60.0% | 40.0% | 66.7% | 63.3% |
| AMZN | 30 | 46.7% | 60.0% | 46.7% | 53.3% |
| GOOGL | 30 | 56.7% | 63.3% | 53.3% | 46.7% |
| JPM | 30 | 46.7% | 60.0% | 46.7% | 43.3% |
| META | 30 | 60.0% | 36.7% | 53.3% | 33.3% |
| MSFT | 30 | 56.7% | 56.7% | 56.7% | 53.3% |
| NVDA | 30 | 53.3% | 46.7% | 53.3% | 30.0% |
| TSLA | 30 | 50.0% | 56.7% | 50.0% | 46.7% |
| UNH | 30 | 53.3% | 56.7% | 56.7% | 43.3% |
| XOM | 30 | 63.3% | 60.0% | 63.3% | 56.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,065 | +36.0% | +7.6% | 0.46 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,065 | +32.0% | +6.8% | 0.44 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,065 | +33.5% | +7.1% | 0.45 | 50.3% |
| Top 3 by gradient boosting | 1,006 | +58.9% | +12.3% | 0.68 | 36.8% |
| Top 3 by ensemble | 1,006 | +29.1% | +6.6% | 0.44 | 45.9% |
| Buy every stock, every session | 1,065 | -8.9% | -2.2% | -0.04 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,065 | -25.0% | -6.6% | -0.41 | 46.8% |
| Top 3 by gradient boosting | 1,006 | -43.4% | -13.3% | -0.82 | 39.0% |
| Top 3 by ensemble | 1,006 | -15.1% | -4.0% | -0.18 | 46.1% |
| Every stock minus SPY | 1,065 | -55.5% | -17.4% | -2.49 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7842 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 734 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 949 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 168 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-05 | 0 | 8 | 38 |
| MSFT | ok | 2026-11-05 | 0 | 8 | 52 |
| NVDA | ok | 2026-11-05 | 0 | 8 | 75 |
| AMZN | ok | 2026-11-05 | 0 | 8 | 45 |
| GOOGL | ok | 2026-11-05 | 0 | 8 | 34 |
| META | ok | 2026-11-05 | 0 | 8 | 43 |
| TSLA | ok | 2026-11-05 | 0 | 8 | 42 |
| JPM | ok | 2026-11-05 | 0 | 8 | 36 |
| XOM | ok | 2026-11-05 | 0 | 8 | 15 |
| UNH | ok | 2026-11-05 | 0 | 8 | 17 |

---

Educational project. Not financial advice.
