# Stock prediction lab: latest report

Generated 2026-11-14 02:26 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | **55.3%** | **Buy at open** | 59.9% | **Outperform** | 79 | negative (-0.07) | negative (-0.37) |
| 2 | META | **54.4%** | **Buy at open** | 59.0% | **Outperform** | 43 | positive (+0.13) | neutral (+0.04) |
| 3 | XOM | **53.1%** | **Buy at open** | 56.3% | – | 35 | positive (+0.16) | positive (+0.17) |
| 4 | TSLA | **51.4%** | Stay out | 60.9% | **Outperform** | 44 | positive (+0.19) | neutral (+0.02) |
| 5 | MSFT | **51.4%** | Stay out | 54.3% | – | 48 | neutral (+0.00) | negative (-0.17) |
| 6 | JPM | **49.8%** | Stay out | 51.2% | – | 27 | positive (+0.06) | negative (-0.17) |
| 7 | AAPL | **48.6%** | Stay out | 50.2% | – | 44 | positive (+0.10) | neutral (+0.05) |
| 8 | GOOGL | **47.1%** | Stay out | 47.5% | – | 42 | positive (+0.19) | positive (+0.06) |
| 9 | AMZN | **46.3%** | Stay out | 45.7% | – | 33 | positive (+0.21) | neutral (+0.02) |
| 10 | UNH | **45.6%** | Stay out | 37.4% | – | 9 | positive (+0.17) | neutral (-0.04) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 51.1% | 49.7% | 48.8% | 50.2% | 47.5% | 51.0% | 48.6% | 50.6% |
| AMZN | 46.1% | 39.5% | 39.9% | 45.7% | 53.2% | 50.8% | 46.3% | 48.3% |
| GOOGL | 50.1% | 45.5% | 44.8% | 47.5% | 48.8% | 51.0% | 47.1% | 49.3% |
| JPM | 52.0% | 46.3% | 44.3% | 51.2% | 53.2% | 49.0% | 49.8% | 50.1% |
| META | 59.9% | 54.4% | 54.8% | 59.0% | 54.5% | 49.0% | 54.4% | 54.0% |
| MSFT | 54.8% | 55.5% | 58.0% | 54.3% | 47.2% | 51.0% | 51.4% | 52.7% |
| NVDA | 59.4% | 58.9% | 58.6% | 59.9% | 51.6% | 50.5% | 55.3% | 55.2% |
| TSLA | 53.1% | 58.3% | 57.2% | 60.9% | 44.4% | 51.0% | 51.4% | 55.9% |
| UNH | 43.5% | 38.5% | 37.9% | 37.4% | 52.7% | 50.8% | 45.6% | 44.1% |
| XOM | 56.1% | 58.7% | 58.3% | 56.3% | 47.5% | 50.8% | 53.1% | 53.5% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 360 | **52.8%** | 47.6%–57.9% | 47.5% | 47.8% | within noise | 0.2485 |
| Live, logistic, all sources (VADER) | 360 | **53.3%** | 48.2%–58.5% | 47.5% | 47.8% | within noise | 0.2508 |
| Live, logistic, all sources (FinBERT) | 360 | **53.9%** | 48.7%–59.0% | 47.5% | 47.8% | within noise | 0.2503 |
| Live, gradient boosting | 360 | **51.7%** | 46.5%–56.8% | 47.5% | 47.8% | no | 0.2475 |
| Live, ensemble | 360 | **54.2%** | 49.0%–59.3% | 47.5% | 47.8% | within noise | 0.2469 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 360 | **54.7%** | 49.6%–59.9% | 47.8% | 46.7% | within noise | 0.2524 |
| Live, gradient boosting | 360 | **53.9%** | 48.7%–59.0% | 47.8% | 46.7% | within noise | 0.2493 |
| Live, ensemble | 360 | **54.4%** | 49.3%–59.6% | 47.8% | 46.7% | within noise | 0.2490 |
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
| under 40% | 50.0% (n=12) | 42.6% (n=47) | 43.8% (n=48) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 42.9% (n=49) | 43.8% (n=64) | 41.9% (n=62) | 30.2% (n=43) | 31.0% (n=58) |
| 45–48% | 42.1% (n=57) | 48.8% (n=41) | 49.0% (n=49) | 56.4% (n=55) | 50.0% (n=62) |
| 48–50% | 46.7% (n=45) | 43.2% (n=37) | 41.7% (n=36) | 46.7% (n=60) | 49.0% (n=49) |
| 50–52% | 50.0% (n=44) | 53.3% (n=30) | 51.9% (n=27) | 45.5% (n=66) | 49.1% (n=53) |
| 52–55% | 44.4% (n=81) | 36.2% (n=47) | 43.9% (n=41) | 42.9% (n=63) | 52.3% (n=65) |
| 55–60% | 59.3% (n=54) | 56.0% (n=50) | 51.9% (n=52) | 55.8% (n=52) | 54.0% (n=50) |
| 60% or more | 50.0% (n=18) | 59.1% (n=44) | 57.8% (n=45) | 71.4% (n=14) | 50.0% (n=16) |
| **Average gap** | **4.6 pts** | **5.3 pts** | **5.0 pts** | **6.9 pts** | **4.1 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 41.3% (n=46) | – | 66.7% (n=6) |
| 40–45% | 43.1% (n=72) | – | 39.6% (n=48) |
| 45–48% | 43.2% (n=44) | 37.1% (n=35) | 39.8% (n=83) |
| 48–50% | 48.3% (n=29) | 45.9% (n=157) | 50.8% (n=61) |
| 50–52% | 54.8% (n=31) | 52.2% (n=161) | 51.7% (n=60) |
| 52–55% | 58.8% (n=51) | 42.9% (n=7) | 53.7% (n=54) |
| 55–60% | 43.9% (n=41) | – | 53.3% (n=45) |
| 60% or more | 52.2% (n=46) | – | 33.3% (n=3) |
| **Average gap** | **5.5 pts** | **3.3 pts** | **3.7 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 307 | 48.2% | -0.2% | -0.4% | -0.044 |
| FinBERT | 241 | 47.7% | -0.1% | 0.1% | -0.069 |

The two scorers agree on the direction of the mood on 66% of 370 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 36 | 41.7% | 52.8% | 50.0% | 33.3% | 44.4% | 58.3% |
| AMZN | 36 | 58.3% | 55.6% | 55.6% | 44.4% | 44.4% | 44.4% |
| GOOGL | 36 | 58.3% | 52.8% | 52.8% | 66.7% | 72.2% | 41.7% |
| JPM | 36 | 52.8% | 44.4% | 52.8% | 36.1% | 36.1% | 38.9% |
| META | 36 | 50.0% | 55.6% | 52.8% | 61.1% | 61.1% | 41.7% |
| MSFT | 36 | 50.0% | 55.6% | 55.6% | 61.1% | 52.8% | 50.0% |
| NVDA | 36 | 55.6% | 58.3% | 58.3% | 61.1% | 61.1% | 30.6% |
| TSLA | 36 | 50.0% | 55.6% | 55.6% | 44.4% | 50.0% | 55.6% |
| UNH | 36 | 50.0% | 44.4% | 44.4% | 58.3% | 55.6% | 50.0% |
| XOM | 36 | 61.1% | 58.3% | 61.1% | 50.0% | 63.9% | 63.9% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 36 | 58.3% | 44.4% | 63.9% | 63.9% |
| AMZN | 36 | 47.2% | 55.6% | 47.2% | 47.2% |
| GOOGL | 36 | 52.8% | 63.9% | 50.0% | 44.4% |
| JPM | 36 | 50.0% | 58.3% | 50.0% | 41.7% |
| META | 36 | 55.6% | 38.9% | 50.0% | 38.9% |
| MSFT | 36 | 58.3% | 55.6% | 58.3% | 50.0% |
| NVDA | 36 | 55.6% | 50.0% | 55.6% | 33.3% |
| TSLA | 36 | 55.6% | 61.1% | 55.6% | 52.8% |
| UNH | 36 | 52.8% | 52.8% | 52.8% | 44.4% |
| XOM | 36 | 61.1% | 58.3% | 61.1% | 61.1% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,071 | +38.5% | +8.0% | 0.48 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,071 | +37.7% | +7.8% | 0.49 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,071 | +35.5% | +7.4% | 0.47 | 50.3% |
| Top 3 by gradient boosting | 1,012 | +62.0% | +12.8% | 0.71 | 37.0% |
| Top 3 by ensemble | 1,012 | +31.6% | +7.1% | 0.47 | 46.0% |
| Buy every stock, every session | 1,071 | -7.3% | -1.8% | -0.01 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,071 | -21.4% | -5.5% | -0.32 | 46.9% |
| Top 3 by gradient boosting | 1,012 | -43.6% | -13.3% | -0.82 | 38.8% |
| Top 3 by ensemble | 1,012 | -11.0% | -2.9% | -0.11 | 46.2% |
| Every stock minus SPY | 1,071 | -55.7% | -17.4% | -2.49 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7869 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 726 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 921 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 999 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 174 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-13 | 0 | 8 | 44 |
| MSFT | ok | 2026-11-13 | 0 | 8 | 48 |
| NVDA | ok | 2026-11-13 | 0 | 8 | 79 |
| AMZN | ok | 2026-11-13 | 0 | 8 | 33 |
| GOOGL | ok | 2026-11-13 | 0 | 8 | 42 |
| META | ok | 2026-11-13 | 0 | 8 | 43 |
| TSLA | ok | 2026-11-13 | 0 | 8 | 44 |
| JPM | ok | 2026-11-13 | 0 | 8 | 27 |
| XOM | ok | 2026-11-13 | 0 | 8 | 35 |
| UNH | ok | 2026-11-13 | 0 | 8 | 9 |

---

Educational project. Not financial advice.
