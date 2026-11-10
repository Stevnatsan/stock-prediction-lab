# Stock prediction lab: latest report

Generated 2026-11-10 08:25 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | AAPL | **60.5%** | **Buy at open** | 62.6% | **Outperform** | 31 | positive (+0.07) | positive (+0.13) |
| 2 | META | **50.9%** | Stay out | 40.5% | – | 49 | positive (+0.10) | neutral (-0.01) |
| 3 | UNH | **50.4%** | Stay out | 50.1% | – | 12 | positive (+0.16) | neutral (+0.02) |
| 4 | TSLA | **49.6%** | Stay out | 57.6% | **Outperform** | 37 | positive (+0.06) | positive (+0.10) |
| 5 | AMZN | **49.5%** | Stay out | 41.1% | – | 52 | positive (+0.21) | positive (+0.08) |
| 6 | XOM | **47.6%** | Stay out | 43.4% | – | 22 | positive (+0.13) | negative (-0.15) |
| 7 | MSFT | **47.3%** | Stay out | 43.0% | – | 31 | neutral (+0.03) | neutral (-0.03) |
| 8 | JPM | **45.9%** | Stay out | 36.5% | – | 29 | positive (+0.17) | neutral (-0.01) |
| 9 | GOOGL | **44.7%** | Stay out | 56.6% | **Outperform** | 49 | positive (+0.12) | positive (+0.16) |
| 10 | NVDA | **41.8%** | Stay out | 36.6% | – | 97 | neutral (-0.04) | negative (-0.36) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 58.8% | 68.8% | 63.8% | 62.6% | 52.3% | 48.9% | 60.5% | 55.8% |
| AMZN | 46.3% | 44.6% | 44.1% | 41.1% | 54.3% | 48.0% | 49.5% | 44.6% |
| GOOGL | 46.2% | 39.8% | 43.0% | 56.6% | 49.6% | 47.6% | 44.7% | 52.1% |
| JPM | 45.7% | 39.5% | 39.3% | 36.5% | 52.3% | 49.6% | 45.9% | 43.1% |
| META | 52.5% | 49.4% | 49.6% | 40.5% | 52.4% | 48.0% | 50.9% | 44.2% |
| MSFT | 47.6% | 40.7% | 42.0% | 43.0% | 53.9% | 48.8% | 47.3% | 45.9% |
| NVDA | 42.2% | 43.3% | 41.6% | 36.6% | 40.3% | 46.5% | 41.8% | 41.6% |
| TSLA | 42.4% | 48.9% | 49.4% | 57.6% | 50.3% | 49.6% | 49.6% | 53.6% |
| UNH | 49.0% | 49.3% | 48.9% | 50.1% | 51.5% | 49.3% | 50.4% | 49.7% |
| XOM | 47.9% | 47.6% | 48.5% | 43.4% | 47.5% | 48.6% | 47.6% | 46.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 320 | **52.5%** | 47.0%–58.0% | 47.5% | 48.4% | no | 0.2479 |
| Live, logistic, all sources (VADER) | 320 | **53.1%** | 47.7%–58.6% | 47.5% | 48.4% | within noise | 0.2507 |
| Live, logistic, all sources (FinBERT) | 320 | **53.4%** | 48.0%–58.9% | 47.5% | 48.4% | within noise | 0.2503 |
| Live, gradient boosting | 320 | **50.9%** | 45.5%–56.4% | 47.5% | 48.4% | no | 0.2477 |
| Live, ensemble | 320 | **53.8%** | 48.3%–59.2% | 47.5% | 48.4% | within noise | 0.2470 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 320 | **54.4%** | 48.9%–59.8% | 47.5% | 46.2% | within noise | 0.2533 |
| Live, gradient boosting | 320 | **53.4%** | 48.0%–58.9% | 47.5% | 46.2% | within noise | 0.2494 |
| Live, ensemble | 320 | **54.4%** | 48.9%–59.8% | 47.5% | 46.2% | within noise | 0.2495 |
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
| under 40% | 50.0% (n=12) | 43.9% (n=41) | 44.2% (n=43) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 40.5% (n=42) | 44.8% (n=58) | 44.6% (n=56) | 31.7% (n=41) | 34.0% (n=53) |
| 45–48% | 45.5% (n=44) | 51.4% (n=35) | 50.0% (n=42) | 55.6% (n=54) | 49.1% (n=57) |
| 48–50% | 45.5% (n=44) | 37.5% (n=32) | 36.7% (n=30) | 49.1% (n=57) | 48.9% (n=45) |
| 50–52% | 48.8% (n=43) | 51.9% (n=27) | 50.0% (n=26) | 43.3% (n=60) | 46.7% (n=45) |
| 52–55% | 40.8% (n=71) | 35.7% (n=42) | 40.5% (n=37) | 43.8% (n=48) | 51.9% (n=54) |
| 55–60% | 64.6% (n=48) | 53.5% (n=43) | 51.2% (n=43) | 53.7% (n=41) | 52.2% (n=46) |
| 60% or more | 50.0% (n=16) | 61.9% (n=42) | 60.5% (n=43) | 75.0% (n=12) | 61.5% (n=13) |
| **Average gap** | **6.4 pts** | **6.5 pts** | **6.0 pts** | **6.8 pts** | **3.7 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 43.9% (n=41) | – | 66.7% (n=6) |
| 40–45% | 41.5% (n=65) | – | 39.0% (n=41) |
| 45–48% | 43.6% (n=39) | 39.4% (n=33) | 40.3% (n=77) |
| 48–50% | 48.3% (n=29) | 45.8% (n=142) | 50.0% (n=56) |
| 50–52% | 55.6% (n=27) | 51.8% (n=141) | 54.0% (n=50) |
| 52–55% | 56.1% (n=41) | 25.0% (n=4) | 48.9% (n=45) |
| 55–60% | 44.1% (n=34) | – | 54.8% (n=42) |
| 60% or more | 52.3% (n=44) | – | 33.3% (n=3) |
| **Average gap** | **5.6 pts** | **3.2 pts** | **4.4 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 272 | 47.8% | -0.3% | 0.0% | -0.061 |
| FinBERT | 216 | 46.8% | -0.2% | 0.1% | -0.100 |

The two scorers agree on the direction of the mood on 66% of 330 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 32 | 43.8% | 56.2% | 53.1% | 34.4% | 46.9% | 62.5% |
| AMZN | 32 | 56.2% | 53.1% | 53.1% | 46.9% | 46.9% | 46.9% |
| GOOGL | 32 | 59.4% | 53.1% | 53.1% | 62.5% | 71.9% | 40.6% |
| JPM | 32 | 53.1% | 40.6% | 46.9% | 37.5% | 34.4% | 40.6% |
| META | 32 | 50.0% | 59.4% | 56.2% | 62.5% | 62.5% | 40.6% |
| MSFT | 32 | 46.9% | 53.1% | 53.1% | 62.5% | 50.0% | 50.0% |
| NVDA | 32 | 53.1% | 56.2% | 56.2% | 56.2% | 59.4% | 28.1% |
| TSLA | 32 | 53.1% | 56.2% | 56.2% | 37.5% | 46.9% | 53.1% |
| UNH | 32 | 46.9% | 43.8% | 43.8% | 59.4% | 53.1% | 50.0% |
| XOM | 32 | 62.5% | 59.4% | 62.5% | 50.0% | 65.6% | 62.5% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 32 | 59.4% | 43.8% | 65.6% | 65.6% |
| AMZN | 32 | 43.8% | 59.4% | 43.8% | 50.0% |
| GOOGL | 32 | 53.1% | 59.4% | 50.0% | 43.8% |
| JPM | 32 | 50.0% | 59.4% | 50.0% | 43.8% |
| META | 32 | 59.4% | 40.6% | 53.1% | 37.5% |
| MSFT | 32 | 59.4% | 53.1% | 59.4% | 53.1% |
| NVDA | 32 | 53.1% | 46.9% | 53.1% | 31.2% |
| TSLA | 32 | 53.1% | 59.4% | 53.1% | 50.0% |
| UNH | 32 | 50.0% | 53.1% | 53.1% | 43.8% |
| XOM | 32 | 62.5% | 59.4% | 62.5% | 56.2% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,067 | +39.9% | +8.3% | 0.49 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,067 | +33.9% | +7.1% | 0.46 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,067 | +37.7% | +7.9% | 0.49 | 50.4% |
| Top 3 by gradient boosting | 1,008 | +62.5% | +12.9% | 0.72 | 36.8% |
| Top 3 by ensemble | 1,008 | +31.0% | +7.0% | 0.46 | 46.0% |
| Buy every stock, every session | 1,067 | -7.5% | -1.8% | -0.02 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,067 | -24.4% | -6.4% | -0.39 | 46.9% |
| Top 3 by gradient boosting | 1,008 | -43.4% | -13.2% | -0.82 | 38.9% |
| Top 3 by ensemble | 1,008 | -14.4% | -3.8% | -0.17 | 46.2% |
| Every stock minus SPY | 1,067 | -55.5% | -17.4% | -2.49 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7845 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 209 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 897 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 999 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 168 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-09 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-09 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-09 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-09 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-09 | 0 | 0 | 0 |
| META | ok | 2026-11-09 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-09 | 0 | 0 | 0 |
| JPM | ok | 2026-11-09 | 0 | 0 | 0 |
| XOM | ok | 2026-11-09 | 0 | 0 | 0 |
| UNH | ok | 2026-11-09 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
