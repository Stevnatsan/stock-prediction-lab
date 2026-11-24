# Stock prediction lab: latest report

Generated 2026-11-24 06:01 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | AAPL | **68.0%** | **Buy at open** | 61.2% | **Outperform** | 28 | positive (+0.05) | neutral (+0.02) |
| 2 | TSLA | **63.2%** | **Buy at open** | 63.7% | **Outperform** | 41 | positive (+0.18) | positive (+0.30) |
| 3 | XOM | **61.7%** | **Buy at open** | 64.1% | **Outperform** | 30 | positive (+0.07) | neutral (+0.01) |
| 4 | NVDA | **55.6%** | Stay out | 50.8% | – | 97 | positive (+0.15) | neutral (+0.03) |
| 5 | GOOGL | **49.2%** | Stay out | 48.0% | – | 38 | positive (+0.08) | neutral (+0.03) |
| 6 | AMZN | **46.8%** | Stay out | 44.0% | – | 33 | positive (+0.20) | positive (+0.07) |
| 7 | UNH | **44.9%** | Stay out | 58.2% | – | 14 | positive (+0.08) | negative (-0.56) |
| 8 | META | **39.4%** | Stay out | 37.4% | – | 52 | positive (+0.10) | negative (-0.09) |
| 9 | MSFT | **35.4%** | Stay out | 34.5% | – | 18 | neutral (+0.02) | neutral (+0.01) |
| 10 | JPM | **25.0%** | Stay out | 32.7% | – | 27 | neutral (+0.05) | neutral (+0.03) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 61.1% | 70.8% | 68.0% | 61.2% | 46.7% | 49.7% | 58.7% | 55.4% |
| AMZN | 48.8% | 47.2% | 46.8% | 44.0% | 63.4% | 50.1% | 55.3% | 47.0% |
| GOOGL | 47.4% | 47.8% | 49.2% | 48.0% | 59.8% | 50.1% | 53.8% | 49.1% |
| JPM | 39.1% | 23.1% | 25.0% | 32.7% | 44.6% | 50.6% | 33.9% | 41.6% |
| META | 43.2% | 39.0% | 39.4% | 37.4% | 60.8% | 50.0% | 49.9% | 43.7% |
| MSFT | 45.2% | 33.7% | 35.4% | 34.5% | 63.5% | 50.6% | 48.6% | 42.5% |
| NVDA | 62.7% | 56.6% | 55.6% | 50.8% | 61.4% | 50.8% | 59.0% | 50.8% |
| TSLA | 57.9% | 63.7% | 63.2% | 63.7% | 60.0% | 49.7% | 61.9% | 56.7% |
| UNH | 57.1% | 50.3% | 44.9% | 58.2% | 33.2% | 50.0% | 41.7% | 54.1% |
| XOM | 57.8% | 61.5% | 61.7% | 64.1% | 45.2% | 50.6% | 53.3% | 57.3% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 420 | **51.0%** | 46.2%–55.7% | 43.1% | 51.4% | no | 0.2497 |
| Live, logistic, all sources (VADER) | 420 | **53.6%** | 48.8%–58.3% | 43.1% | 51.4% | no | 0.2485 |
| Live, logistic, all sources (FinBERT) | 420 | **54.5%** | 49.8%–59.3% | 43.1% | 51.4% | no | 0.2476 |
| Live, gradient boosting | 420 | **51.7%** | 46.9%–56.4% | 43.1% | 51.4% | no | 0.2481 |
| Live, ensemble | 420 | **53.8%** | 49.0%–58.6% | 43.1% | 51.4% | no | 0.2455 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 420 | **55.2%** | 50.5%–60.0% | 46.7% | 48.1% | within noise | 0.2517 |
| Live, gradient boosting | 420 | **53.6%** | 48.8%–58.3% | 46.7% | 48.1% | within noise | 0.2492 |
| Live, ensemble | 420 | **55.0%** | 50.2%–59.8% | 46.7% | 48.1% | within noise | 0.2484 |
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
| under 40% | 31.6% (n=19) | 36.7% (n=60) | 35.9% (n=64) | 37.5% (n=8) | 23.1% (n=13) |
| 40–45% | 40.7% (n=54) | 41.9% (n=74) | 39.4% (n=71) | 24.1% (n=54) | 27.3% (n=66) |
| 45–48% | 39.7% (n=63) | 43.5% (n=46) | 47.3% (n=55) | 50.8% (n=63) | 46.4% (n=69) |
| 48–50% | 46.9% (n=49) | 38.6% (n=44) | 35.7% (n=42) | 44.4% (n=63) | 47.4% (n=57) |
| 50–52% | 43.6% (n=55) | 50.0% (n=34) | 50.0% (n=28) | 43.2% (n=74) | 41.8% (n=67) |
| 52–55% | 40.9% (n=93) | 32.1% (n=53) | 40.4% (n=47) | 39.5% (n=76) | 49.3% (n=73) |
| 55–60% | 53.1% (n=64) | 49.2% (n=61) | 45.3% (n=64) | 49.2% (n=59) | 47.4% (n=57) |
| 60% or more | 39.1% (n=23) | 56.2% (n=48) | 55.1% (n=49) | 60.9% (n=23) | 55.6% (n=18) |
| **Average gap** | **7.4 pts** | **6.8 pts** | **6.7 pts** | **8.9 pts** | **6.9 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 38.6% (n=57) | – | 40.0% (n=10) |
| 40–45% | 43.8% (n=80) | – | 39.3% (n=56) |
| 45–48% | 41.2% (n=51) | 36.1% (n=36) | 41.3% (n=92) |
| 48–50% | 43.8% (n=32) | 44.4% (n=169) | 46.4% (n=69) |
| 50–52% | 55.9% (n=34) | 50.5% (n=208) | 53.8% (n=65) |
| 52–55% | 58.2% (n=55) | 42.9% (n=7) | 53.0% (n=66) |
| 55–60% | 46.2% (n=52) | – | 50.0% (n=58) |
| 60% or more | 49.2% (n=59) | – | 25.0% (n=4) |
| **Average gap** | **6.3 pts** | **3.2 pts** | **4.0 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 350 | 45.7% | -0.4% | -1.8% | -0.014 |
| FinBERT | 281 | 50.2% | -0.2% | -0.5% | +0.044 |

The two scorers agree on the direction of the mood on 63% of 430 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 42 | 38.1% | 52.4% | 52.4% | 40.5% | 50.0% | 54.8% |
| AMZN | 42 | 57.1% | 52.4% | 52.4% | 42.9% | 42.9% | 42.9% |
| GOOGL | 42 | 61.9% | 59.5% | 59.5% | 61.9% | 76.2% | 35.7% |
| JPM | 42 | 47.6% | 50.0% | 59.5% | 33.3% | 38.1% | 33.3% |
| META | 42 | 42.9% | 54.8% | 52.4% | 57.1% | 57.1% | 38.1% |
| MSFT | 42 | 47.6% | 54.8% | 54.8% | 61.9% | 50.0% | 45.2% |
| NVDA | 42 | 59.5% | 61.9% | 61.9% | 57.1% | 64.3% | 26.2% |
| TSLA | 42 | 50.0% | 54.8% | 54.8% | 47.6% | 50.0% | 50.0% |
| UNH | 42 | 47.6% | 40.5% | 40.5% | 61.9% | 52.4% | 47.6% |
| XOM | 42 | 57.1% | 54.8% | 57.1% | 52.4% | 57.1% | 57.1% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 42 | 64.3% | 47.6% | 69.0% | 69.0% |
| AMZN | 42 | 47.6% | 54.8% | 47.6% | 47.6% |
| GOOGL | 42 | 54.8% | 59.5% | 52.4% | 40.5% |
| JPM | 42 | 45.2% | 57.1% | 45.2% | 40.5% |
| META | 42 | 54.8% | 42.9% | 50.0% | 35.7% |
| MSFT | 42 | 57.1% | 52.4% | 57.1% | 47.6% |
| NVDA | 42 | 59.5% | 45.2% | 59.5% | 28.6% |
| TSLA | 42 | 54.8% | 61.9% | 54.8% | 52.4% |
| UNH | 42 | 52.4% | 57.1% | 52.4% | 45.2% |
| XOM | 42 | 61.9% | 57.1% | 61.9% | 59.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,077 | +26.1% | +5.6% | 0.37 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,077 | +18.8% | +4.1% | 0.30 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,077 | +19.3% | +4.2% | 0.31 | 50.1% |
| Top 3 by gradient boosting | 1,018 | +47.4% | +10.1% | 0.59 | 36.8% |
| Top 3 by ensemble | 1,018 | +4.7% | +1.1% | 0.16 | 45.9% |
| Buy every stock, every session | 1,077 | -18.1% | -4.6% | -0.17 | 51.7% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,077 | -25.2% | -6.6% | -0.40 | 46.9% |
| Top 3 by gradient boosting | 1,018 | -43.6% | -13.2% | -0.82 | 38.6% |
| Top 3 by ensemble | 1,018 | -15.2% | -4.0% | -0.18 | 46.3% |
| Every stock minus SPY | 1,077 | -57.2% | -18.0% | -2.57 | 41.9% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7828 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 802 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 9 | 1 | 853 | HTTPError: 429 Client Error: Too Many Requests for url: https://news.google.com/rss/search?q=MSFT+stock&hl=en-US&gl=US&ceid=US:en |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 7 | 3 | 700 | HTTPError: 429 Client Error: Too Many Requests for url: https://news.google.com/rss/search?q=%28tesla+OR+tsla%29+%28site%3Areuters.com+OR+site%3Abloomberg.com+OR+site%3Acnbc.com+OR+site%3Awsj.com+OR+s |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 175 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-23 | 0 | 8 | 28 |
| MSFT | ok | 2026-11-23 | 0 | 8 | 18 |
| NVDA | ok | 2026-11-23 | 0 | 8 | 97 |
| AMZN | ok | 2026-11-23 | 0 | 8 | 33 |
| GOOGL | ok | 2026-11-23 | 0 | 8 | 38 |
| META | ok | 2026-11-23 | 0 | 8 | 52 |
| TSLA | ok | 2026-11-23 | 0 | 8 | 41 |
| JPM | ok | 2026-11-23 | 0 | 8 | 27 |
| XOM | ok | 2026-11-23 | 0 | 8 | 30 |
| UNH | ok | 2026-11-23 | 0 | 8 | 14 |

---

Educational project. Not financial advice.
