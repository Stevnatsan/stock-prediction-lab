# Stock prediction lab: latest report

Generated 2026-11-11 01:56 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **60.6%** | **Buy at open** | 59.0% | **Outperform** | 48 | positive (+0.13) | neutral (-0.04) |
| 2 | XOM | **55.3%** | **Buy at open** | 52.3% | – | 27 | positive (+0.12) | neutral (-0.04) |
| 3 | JPM | **54.8%** | **Buy at open** | 50.5% | – | 28 | positive (+0.06) | neutral (+0.03) |
| 4 | MSFT | **53.0%** | Stay out | 52.3% | – | 40 | positive (+0.17) | negative (-0.19) |
| 5 | AAPL | **52.6%** | Stay out | 52.9% | **Outperform** | 33 | positive (+0.18) | positive (+0.14) |
| 6 | TSLA | **51.4%** | Stay out | 55.2% | **Outperform** | 33 | positive (+0.14) | neutral (+0.02) |
| 7 | AMZN | **50.0%** | Stay out | 47.7% | – | 58 | positive (+0.29) | positive (+0.10) |
| 8 | UNH | **48.4%** | Stay out | 38.4% | – | 4 | neutral (+0.04) | negative (-0.43) |
| 9 | NVDA | **47.6%** | Stay out | 38.4% | – | 115 | neutral (-0.01) | negative (-0.27) |
| 10 | GOOGL | **45.3%** | Stay out | 50.5% | – | 38 | positive (+0.09) | positive (+0.10) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 52.6% | 51.6% | 51.3% | 52.9% | 53.7% | 48.7% | 52.6% | 50.8% |
| AMZN | 46.8% | 46.7% | 47.0% | 47.7% | 53.3% | 49.0% | 50.0% | 48.3% |
| GOOGL | 40.1% | 34.7% | 37.2% | 50.5% | 56.0% | 50.2% | 45.3% | 50.3% |
| JPM | 54.4% | 54.6% | 53.6% | 50.5% | 55.1% | 50.5% | 54.8% | 50.5% |
| META | 60.5% | 64.2% | 65.0% | 59.0% | 57.0% | 50.2% | 60.6% | 54.6% |
| MSFT | 55.2% | 52.2% | 57.8% | 52.3% | 53.7% | 49.8% | 53.0% | 51.1% |
| NVDA | 40.3% | 35.9% | 35.0% | 38.4% | 59.4% | 50.4% | 47.6% | 44.4% |
| TSLA | 41.4% | 48.1% | 47.6% | 55.2% | 54.7% | 50.5% | 51.4% | 52.8% |
| UNH | 46.0% | 42.0% | 43.4% | 38.4% | 54.8% | 49.7% | 48.4% | 44.0% |
| XOM | 53.4% | 53.4% | 54.4% | 52.3% | 57.2% | 50.5% | 55.3% | 51.4% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 330 | **52.4%** | 47.0%–57.8% | 47.6% | 48.2% | within noise | 0.2481 |
| Live, logistic, all sources (VADER) | 330 | **52.7%** | 47.3%–58.1% | 47.6% | 48.2% | within noise | 0.2507 |
| Live, logistic, all sources (FinBERT) | 330 | **53.0%** | 47.6%–58.4% | 47.6% | 48.2% | within noise | 0.2501 |
| Live, gradient boosting | 330 | **51.2%** | 45.8%–56.6% | 47.6% | 48.2% | no | 0.2476 |
| Live, ensemble | 330 | **53.9%** | 48.6%–59.3% | 47.6% | 48.2% | within noise | 0.2469 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 330 | **54.2%** | 48.9%–59.6% | 47.6% | 46.4% | within noise | 0.2536 |
| Live, gradient boosting | 330 | **53.3%** | 48.0%–58.7% | 47.6% | 46.4% | within noise | 0.2494 |
| Live, ensemble | 330 | **53.9%** | 48.6%–59.3% | 47.6% | 46.4% | within noise | 0.2496 |
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
| under 40% | 50.0% (n=12) | 41.9% (n=43) | 43.2% (n=44) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 40.9% (n=44) | 44.3% (n=61) | 43.3% (n=60) | 31.0% (n=42) | 32.7% (n=55) |
| 45–48% | 44.9% (n=49) | 52.8% (n=36) | 50.0% (n=42) | 56.4% (n=55) | 48.3% (n=60) |
| 48–50% | 46.7% (n=45) | 42.9% (n=35) | 44.1% (n=34) | 48.3% (n=58) | 51.1% (n=47) |
| 50–52% | 48.8% (n=43) | 51.9% (n=27) | 50.0% (n=26) | 45.2% (n=62) | 48.9% (n=47) |
| 52–55% | 41.7% (n=72) | 35.7% (n=42) | 40.5% (n=37) | 43.4% (n=53) | 51.9% (n=54) |
| 55–60% | 63.3% (n=49) | 53.5% (n=43) | 51.2% (n=43) | 53.7% (n=41) | 52.2% (n=46) |
| 60% or more | 50.0% (n=16) | 60.5% (n=43) | 59.1% (n=44) | 75.0% (n=12) | 57.1% (n=14) |
| **Average gap** | **5.8 pts** | **5.9 pts** | **5.1 pts** | **6.9 pts** | **3.9 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 41.9% (n=43) | – | 66.7% (n=6) |
| 40–45% | 43.5% (n=69) | – | 40.0% (n=45) |
| 45–48% | 43.6% (n=39) | 37.1% (n=35) | 40.5% (n=79) |
| 48–50% | 48.3% (n=29) | 46.7% (n=150) | 50.9% (n=57) |
| 50–52% | 57.1% (n=28) | 51.8% (n=141) | 54.0% (n=50) |
| 52–55% | 56.1% (n=41) | 25.0% (n=4) | 48.9% (n=47) |
| 55–60% | 44.4% (n=36) | – | 53.5% (n=43) |
| 60% or more | 51.1% (n=45) | – | 33.3% (n=3) |
| **Average gap** | **5.5 pts** | **3.1 pts** | **4.5 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 280 | 48.2% | -0.2% | 0.0% | -0.057 |
| FinBERT | 222 | 46.8% | -0.2% | 0.1% | -0.094 |

The two scorers agree on the direction of the mood on 66% of 340 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 33 | 42.4% | 54.5% | 51.5% | 33.3% | 45.5% | 60.6% |
| AMZN | 33 | 54.5% | 51.5% | 51.5% | 48.5% | 45.5% | 48.5% |
| GOOGL | 33 | 60.6% | 54.5% | 54.5% | 63.6% | 72.7% | 39.4% |
| JPM | 33 | 54.5% | 42.4% | 48.5% | 36.4% | 36.4% | 39.4% |
| META | 33 | 51.5% | 57.6% | 54.5% | 63.6% | 63.6% | 42.4% |
| MSFT | 33 | 48.5% | 54.5% | 54.5% | 60.6% | 51.5% | 48.5% |
| NVDA | 33 | 54.5% | 57.6% | 57.6% | 57.6% | 60.6% | 27.3% |
| TSLA | 33 | 51.5% | 54.5% | 54.5% | 39.4% | 45.5% | 54.5% |
| UNH | 33 | 45.5% | 42.4% | 42.4% | 60.6% | 54.5% | 51.5% |
| XOM | 33 | 60.6% | 57.6% | 60.6% | 48.5% | 63.6% | 63.6% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 33 | 57.6% | 45.5% | 63.6% | 63.6% |
| AMZN | 33 | 42.4% | 57.6% | 42.4% | 51.5% |
| GOOGL | 33 | 51.5% | 60.6% | 48.5% | 42.4% |
| JPM | 33 | 51.5% | 60.6% | 51.5% | 42.4% |
| META | 33 | 57.6% | 39.4% | 51.5% | 39.4% |
| MSFT | 33 | 60.6% | 54.5% | 60.6% | 51.5% |
| NVDA | 33 | 54.5% | 48.5% | 54.5% | 30.3% |
| TSLA | 33 | 54.5% | 57.6% | 54.5% | 51.5% |
| UNH | 33 | 51.5% | 51.5% | 51.5% | 45.5% |
| XOM | 33 | 60.6% | 57.6% | 60.6% | 57.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,068 | +39.8% | +8.2% | 0.49 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,068 | +32.8% | +6.9% | 0.45 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,068 | +36.5% | +7.6% | 0.48 | 50.4% |
| Top 3 by gradient boosting | 1,009 | +59.3% | +12.3% | 0.69 | 36.9% |
| Top 3 by ensemble | 1,009 | +29.9% | +6.8% | 0.45 | 46.0% |
| Buy every stock, every session | 1,068 | -7.4% | -1.8% | -0.01 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,068 | -24.4% | -6.4% | -0.39 | 46.8% |
| Top 3 by gradient boosting | 1,009 | -43.4% | -13.2% | -0.82 | 38.9% |
| Top 3 by ensemble | 1,009 | -14.5% | -3.8% | -0.17 | 46.2% |
| Every stock minus SPY | 1,068 | -55.6% | -17.4% | -2.50 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7847 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 738 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 895 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 999 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 171 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-10 | 0 | 8 | 33 |
| MSFT | ok | 2026-11-10 | 0 | 8 | 40 |
| NVDA | ok | 2026-11-10 | 0 | 8 | 115 |
| AMZN | ok | 2026-11-10 | 0 | 8 | 58 |
| GOOGL | ok | 2026-11-10 | 0 | 8 | 38 |
| META | ok | 2026-11-10 | 0 | 8 | 48 |
| TSLA | ok | 2026-11-10 | 0 | 8 | 33 |
| JPM | ok | 2026-11-10 | 0 | 8 | 28 |
| XOM | ok | 2026-11-10 | 0 | 8 | 27 |
| UNH | ok | 2026-11-10 | 0 | 8 | 4 |

---

Educational project. Not financial advice.
