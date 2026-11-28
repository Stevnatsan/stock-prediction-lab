# Stock prediction lab: latest report

Generated 2026-11-28 03:54 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **63.9%** | **Buy at open** | 43.7% | – | 15 | positive (+0.24) | positive (+0.22) |
| 2 | MSFT | **62.8%** | **Buy at open** | 56.1% | **Outperform** | 41 | positive (+0.11) | positive (+0.09) |
| 3 | JPM | **62.3%** | **Buy at open** | 56.3% | **Outperform** | 16 | positive (+0.12) | positive (+0.06) |
| 4 | AAPL | **60.6%** | Stay out | 56.2% | **Outperform** | 35 | positive (+0.23) | negative (-0.12) |
| 5 | AMZN | **59.1%** | Stay out | 50.0% | – | 46 | positive (+0.20) | positive (+0.21) |
| 6 | META | **56.0%** | Stay out | 43.5% | – | 43 | positive (+0.07) | positive (+0.09) |
| 7 | TSLA | **55.7%** | Stay out | 49.5% | – | 37 | positive (+0.18) | positive (+0.18) |
| 8 | GOOGL | **55.1%** | Stay out | 49.5% | – | 30 | positive (+0.09) | negative (-0.08) |
| 9 | UNH | **54.8%** | Stay out | 42.3% | – | 10 | positive (+0.07) | negative (-0.12) |
| 10 | NVDA | **48.0%** | Stay out | 38.6% | – | 70 | positive (+0.10) | neutral (-0.03) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 54.7% | 57.5% | 65.9% | 56.2% | 63.6% | 51.2% | 60.6% | 53.7% |
| AMZN | 49.2% | 55.7% | 52.1% | 50.0% | 62.5% | 51.2% | 59.1% | 50.6% |
| GOOGL | 53.9% | 52.2% | 49.6% | 49.5% | 57.9% | 50.1% | 55.1% | 49.8% |
| JPM | 53.6% | 61.9% | 62.6% | 56.3% | 62.7% | 51.2% | 62.3% | 53.7% |
| META | 52.5% | 57.2% | 56.0% | 43.5% | 54.8% | 49.5% | 56.0% | 46.5% |
| MSFT | 65.5% | 64.2% | 63.9% | 56.1% | 61.5% | 50.1% | 62.8% | 53.1% |
| NVDA | 54.0% | 44.2% | 44.1% | 38.6% | 51.9% | 50.8% | 48.0% | 44.7% |
| TSLA | 49.1% | 56.6% | 55.7% | 49.5% | 54.8% | 49.5% | 55.7% | 49.5% |
| UNH | 47.0% | 53.4% | 54.1% | 42.3% | 56.3% | 49.5% | 54.8% | 45.9% |
| XOM | 63.0% | 65.9% | 64.8% | 43.7% | 61.8% | 51.2% | 63.9% | 47.5% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 450 | **51.3%** | 46.7%–56.0% | 45.3% | 52.2% | no | 0.2500 |
| Live, logistic, all sources (VADER) | 450 | **54.2%** | 49.6%–58.8% | 45.3% | 52.2% | no | 0.2495 |
| Live, logistic, all sources (FinBERT) | 450 | **54.9%** | 50.3%–59.5% | 45.3% | 52.2% | within noise | 0.2487 |
| Live, gradient boosting | 450 | **51.6%** | 46.9%–56.2% | 45.3% | 52.2% | no | 0.2490 |
| Live, ensemble | 450 | **53.8%** | 49.2%–58.4% | 45.3% | 52.2% | no | 0.2462 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 450 | **54.9%** | 50.3%–59.5% | 46.4% | 47.6% | within noise | 0.2531 |
| Live, gradient boosting | 450 | **52.7%** | 48.1%–57.3% | 46.4% | 47.6% | no | 0.2493 |
| Live, ensemble | 450 | **54.7%** | 50.1%–59.3% | 46.4% | 47.6% | within noise | 0.2490 |
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
| under 40% | 37.5% (n=24) | 41.2% (n=68) | 40.3% (n=72) | 44.4% (n=9) | 33.3% (n=18) |
| 40–45% | 43.9% (n=57) | 41.9% (n=74) | 40.3% (n=72) | 26.8% (n=56) | 28.4% (n=67) |
| 45–48% | 40.0% (n=65) | 42.9% (n=49) | 47.4% (n=57) | 53.7% (n=67) | 47.1% (n=70) |
| 48–50% | 49.1% (n=53) | 40.0% (n=45) | 36.4% (n=44) | 45.5% (n=66) | 50.8% (n=61) |
| 50–52% | 47.5% (n=59) | 51.4% (n=35) | 51.7% (n=29) | 47.0% (n=83) | 44.3% (n=70) |
| 52–55% | 41.7% (n=96) | 36.8% (n=57) | 45.1% (n=51) | 40.3% (n=77) | 52.4% (n=82) |
| 55–60% | 56.3% (n=71) | 52.9% (n=70) | 47.9% (n=71) | 50.0% (n=64) | 47.6% (n=63) |
| 60% or more | 40.0% (n=25) | 57.7% (n=52) | 57.4% (n=54) | 60.7% (n=28) | 57.9% (n=19) |
| **Average gap** | **5.7 pts** | **6.3 pts** | **6.1 pts** | **7.9 pts** | **5.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 41.3% (n=63) | – | 41.7% (n=12) |
| 40–45% | 41.7% (n=84) | – | 41.7% (n=60) |
| 45–48% | 41.5% (n=53) | 36.1% (n=36) | 39.6% (n=96) |
| 48–50% | 44.1% (n=34) | 44.9% (n=176) | 46.6% (n=73) |
| 50–52% | 54.1% (n=37) | 49.4% (n=231) | 52.9% (n=68) |
| 52–55% | 57.1% (n=56) | 42.9% (n=7) | 52.0% (n=75) |
| 55–60% | 46.7% (n=60) | – | 50.0% (n=62) |
| 60% or more | 49.2% (n=63) | – | 25.0% (n=4) |
| **Average gap** | **6.4 pts** | **3.4 pts** | **4.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 376 | 48.1% | -0.3% | -1.7% | -0.027 |
| FinBERT | 299 | 49.5% | -0.2% | -0.3% | +0.024 |

The two scorers agree on the direction of the mood on 62% of 460 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 45 | 42.2% | 55.6% | 55.6% | 42.2% | 53.3% | 57.8% |
| AMZN | 45 | 57.8% | 55.6% | 55.6% | 42.2% | 44.4% | 44.4% |
| GOOGL | 45 | 62.2% | 60.0% | 60.0% | 57.8% | 73.3% | 35.6% |
| JPM | 45 | 46.7% | 51.1% | 60.0% | 35.6% | 40.0% | 37.8% |
| META | 45 | 44.4% | 55.6% | 53.3% | 57.8% | 55.6% | 42.2% |
| MSFT | 45 | 46.7% | 51.1% | 51.1% | 62.2% | 46.7% | 46.7% |
| NVDA | 45 | 57.8% | 60.0% | 60.0% | 53.3% | 62.2% | 26.7% |
| TSLA | 45 | 48.9% | 55.6% | 55.6% | 51.1% | 53.3% | 53.3% |
| UNH | 45 | 51.1% | 44.4% | 42.2% | 60.0% | 53.3% | 51.1% |
| XOM | 45 | 55.6% | 53.3% | 55.6% | 53.3% | 55.6% | 57.8% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 45 | 62.2% | 46.7% | 66.7% | 66.7% |
| AMZN | 45 | 48.9% | 53.3% | 48.9% | 46.7% |
| GOOGL | 45 | 55.6% | 57.8% | 53.3% | 40.0% |
| JPM | 45 | 44.4% | 57.8% | 44.4% | 42.2% |
| META | 45 | 55.6% | 44.4% | 51.1% | 35.6% |
| MSFT | 45 | 53.3% | 51.1% | 53.3% | 46.7% |
| NVDA | 45 | 57.8% | 44.4% | 57.8% | 28.9% |
| TSLA | 45 | 53.3% | 62.2% | 53.3% | 53.3% |
| UNH | 45 | 55.6% | 53.3% | 55.6% | 46.7% |
| XOM | 45 | 62.2% | 55.6% | 62.2% | 57.8% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,080 | +28.7% | +6.1% | 0.39 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,080 | +21.0% | +4.6% | 0.33 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,080 | +21.5% | +4.7% | 0.33 | 50.2% |
| Top 3 by gradient boosting | 1,021 | +48.1% | +10.2% | 0.59 | 36.7% |
| Top 3 by ensemble | 1,021 | +5.2% | +1.3% | 0.16 | 45.8% |
| Buy every stock, every session | 1,080 | -16.1% | -4.0% | -0.14 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,080 | -25.8% | -6.7% | -0.41 | 46.9% |
| Top 3 by gradient boosting | 1,021 | -43.6% | -13.2% | -0.82 | 38.5% |
| Top 3 by ensemble | 1,021 | -16.0% | -4.2% | -0.19 | 46.2% |
| Every stock minus SPY | 1,080 | -57.3% | -18.0% | -2.58 | 41.9% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7828 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 593 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 918 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 191 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-27 | 0 | 8 | 35 |
| MSFT | ok | 2026-11-27 | 0 | 8 | 41 |
| NVDA | ok | 2026-11-27 | 0 | 8 | 70 |
| AMZN | ok | 2026-11-27 | 0 | 8 | 46 |
| GOOGL | ok | 2026-11-27 | 0 | 8 | 30 |
| META | ok | 2026-11-27 | 0 | 8 | 43 |
| TSLA | ok | 2026-11-27 | 0 | 8 | 37 |
| JPM | ok | 2026-11-27 | 0 | 8 | 16 |
| XOM | ok | 2026-11-27 | 0 | 8 | 15 |
| UNH | ok | 2026-11-27 | 0 | 8 | 10 |

---

Educational project. Not financial advice.
