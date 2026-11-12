# Stock prediction lab: latest report

Generated 2026-11-12 08:19 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **60.1%** | **Buy at open** | 57.5% | **Outperform** | 45 | positive (+0.12) | neutral (-0.04) |
| 2 | XOM | **57.8%** | **Buy at open** | 46.7% | – | 14 | positive (+0.18) | positive (+0.32) |
| 3 | TSLA | **56.7%** | **Buy at open** | 61.9% | **Outperform** | 39 | positive (+0.11) | neutral (+0.02) |
| 4 | AAPL | **56.7%** | Stay out | 52.8% | – | 37 | positive (+0.16) | neutral (-0.03) |
| 5 | NVDA | **55.0%** | Stay out | 57.3% | **Outperform** | 96 | neutral (+0.00) | negative (-0.28) |
| 6 | JPM | **54.8%** | Stay out | 43.6% | – | 24 | positive (+0.11) | neutral (-0.04) |
| 7 | AMZN | **52.8%** | Stay out | 46.4% | – | 47 | positive (+0.15) | negative (-0.05) |
| 8 | UNH | **52.8%** | Stay out | 45.2% | – | 9 | positive (+0.05) | positive (+0.08) |
| 9 | GOOGL | **51.9%** | Stay out | 54.1% | – | 39 | positive (+0.16) | positive (+0.16) |
| 10 | MSFT | **50.9%** | Stay out | 52.2% | – | 43 | positive (+0.17) | negative (-0.12) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 56.5% | 54.5% | 57.3% | 52.8% | 58.8% | 50.2% | 56.7% | 51.5% |
| AMZN | 45.8% | 46.9% | 47.5% | 46.4% | 58.7% | 50.6% | 52.8% | 48.5% |
| GOOGL | 45.8% | 43.4% | 45.3% | 54.1% | 60.5% | 51.2% | 51.9% | 52.6% |
| JPM | 52.5% | 50.3% | 49.3% | 43.6% | 59.4% | 50.5% | 54.8% | 47.1% |
| META | 56.3% | 56.7% | 57.5% | 57.5% | 63.6% | 52.8% | 60.1% | 55.1% |
| MSFT | 53.1% | 50.3% | 52.5% | 52.2% | 51.4% | 50.1% | 50.9% | 51.1% |
| NVDA | 52.8% | 56.7% | 55.9% | 57.3% | 53.3% | 50.0% | 55.0% | 53.7% |
| TSLA | 46.2% | 55.2% | 55.1% | 61.9% | 58.2% | 50.2% | 56.7% | 56.1% |
| UNH | 51.1% | 46.2% | 47.9% | 45.2% | 59.4% | 50.7% | 52.8% | 47.9% |
| XOM | 54.2% | 56.4% | 56.5% | 46.7% | 59.1% | 51.0% | 57.8% | 48.8% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 340 | **52.4%** | 47.0%–57.7% | 47.9% | 47.6% | within noise | 0.2491 |
| Live, logistic, all sources (VADER) | 340 | **52.6%** | 47.3%–58.0% | 47.9% | 47.6% | within noise | 0.2517 |
| Live, logistic, all sources (FinBERT) | 340 | **52.9%** | 47.6%–58.2% | 47.9% | 47.6% | within noise | 0.2513 |
| Live, gradient boosting | 340 | **51.5%** | 46.2%–56.8% | 47.9% | 47.6% | no | 0.2473 |
| Live, ensemble | 340 | **53.8%** | 48.5%–59.1% | 47.9% | 47.6% | within noise | 0.2472 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 340 | **54.4%** | 49.1%–59.7% | 47.6% | 46.2% | within noise | 0.2536 |
| Live, gradient boosting | 340 | **53.8%** | 48.5%–59.1% | 47.6% | 46.2% | within noise | 0.2494 |
| Live, ensemble | 340 | **54.1%** | 48.8%–59.4% | 47.6% | 46.2% | within noise | 0.2496 |
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
| under 40% | 50.0% (n=12) | 44.4% (n=45) | 45.7% (n=46) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 44.7% (n=47) | 43.5% (n=62) | 42.6% (n=61) | 31.0% (n=42) | 32.7% (n=55) |
| 45–48% | 43.1% (n=51) | 51.4% (n=37) | 50.0% (n=44) | 56.4% (n=55) | 50.0% (n=62) |
| 48–50% | 46.7% (n=45) | 44.4% (n=36) | 44.1% (n=34) | 48.3% (n=58) | 50.0% (n=48) |
| 50–52% | 48.8% (n=43) | 53.6% (n=28) | 51.9% (n=27) | 45.2% (n=62) | 49.0% (n=49) |
| 52–55% | 44.0% (n=75) | 37.8% (n=45) | 43.6% (n=39) | 43.1% (n=58) | 52.6% (n=57) |
| 55–60% | 62.0% (n=50) | 53.5% (n=43) | 50.0% (n=44) | 56.5% (n=46) | 53.2% (n=47) |
| 60% or more | 47.1% (n=17) | 59.1% (n=44) | 57.8% (n=45) | 75.0% (n=12) | 53.3% (n=15) |
| **Average gap** | **5.5 pts** | **5.9 pts** | **5.3 pts** | **6.6 pts** | **3.9 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 42.2% (n=45) | – | 66.7% (n=6) |
| 40–45% | 43.5% (n=69) | – | 40.4% (n=47) |
| 45–48% | 42.5% (n=40) | 37.1% (n=35) | 40.5% (n=79) |
| 48–50% | 48.3% (n=29) | 46.1% (n=154) | 50.0% (n=58) |
| 50–52% | 56.7% (n=30) | 52.4% (n=147) | 54.5% (n=55) |
| 52–55% | 56.8% (n=44) | 25.0% (n=4) | 49.0% (n=49) |
| 55–60% | 44.7% (n=38) | – | 53.5% (n=43) |
| 60% or more | 51.1% (n=45) | – | 33.3% (n=3) |
| **Average gap** | **5.7 pts** | **3.6 pts** | **4.4 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 288 | 48.6% | -0.2% | 0.0% | -0.067 |
| FinBERT | 228 | 47.4% | -0.2% | 0.0% | -0.079 |

The two scorers agree on the direction of the mood on 65% of 350 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 34 | 44.1% | 55.9% | 52.9% | 35.3% | 47.1% | 61.8% |
| AMZN | 34 | 55.9% | 52.9% | 52.9% | 47.1% | 44.1% | 47.1% |
| GOOGL | 34 | 58.8% | 52.9% | 52.9% | 64.7% | 70.6% | 41.2% |
| JPM | 34 | 55.9% | 44.1% | 50.0% | 38.2% | 38.2% | 41.2% |
| META | 34 | 50.0% | 55.9% | 52.9% | 61.8% | 61.8% | 41.2% |
| MSFT | 34 | 47.1% | 52.9% | 52.9% | 58.8% | 50.0% | 47.1% |
| NVDA | 34 | 52.9% | 55.9% | 55.9% | 58.8% | 58.8% | 29.4% |
| TSLA | 34 | 50.0% | 52.9% | 52.9% | 41.2% | 47.1% | 55.9% |
| UNH | 34 | 47.1% | 44.1% | 44.1% | 58.8% | 55.9% | 50.0% |
| XOM | 34 | 61.8% | 58.8% | 61.8% | 50.0% | 64.7% | 64.7% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 34 | 58.8% | 44.1% | 64.7% | 64.7% |
| AMZN | 34 | 44.1% | 58.8% | 44.1% | 50.0% |
| GOOGL | 34 | 52.9% | 61.8% | 50.0% | 44.1% |
| JPM | 34 | 50.0% | 58.8% | 50.0% | 41.2% |
| META | 34 | 55.9% | 38.2% | 50.0% | 38.2% |
| MSFT | 34 | 58.8% | 55.9% | 58.8% | 50.0% |
| NVDA | 34 | 52.9% | 50.0% | 52.9% | 32.4% |
| TSLA | 34 | 55.9% | 58.8% | 55.9% | 52.9% |
| UNH | 34 | 52.9% | 52.9% | 52.9% | 44.1% |
| XOM | 34 | 61.8% | 58.8% | 61.8% | 58.8% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,069 | +37.3% | +7.8% | 0.47 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,069 | +31.9% | +6.8% | 0.44 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,069 | +34.5% | +7.2% | 0.46 | 50.3% |
| Top 3 by gradient boosting | 1,010 | +58.9% | +12.2% | 0.69 | 36.8% |
| Top 3 by ensemble | 1,010 | +29.1% | +6.6% | 0.44 | 45.9% |
| Buy every stock, every session | 1,069 | -7.7% | -1.9% | -0.02 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,069 | -24.8% | -6.5% | -0.40 | 46.8% |
| Top 3 by gradient boosting | 1,010 | -43.4% | -13.2% | -0.82 | 38.8% |
| Top 3 by ensemble | 1,010 | -15.6% | -4.1% | -0.19 | 46.1% |
| Every stock minus SPY | 1,069 | -56.0% | -17.6% | -2.52 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7850 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 221 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 882 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 166 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-11 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-11 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-11 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-11 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-11 | 0 | 0 | 0 |
| META | ok | 2026-11-11 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-11 | 0 | 0 | 0 |
| JPM | ok | 2026-11-11 | 0 | 0 | 0 |
| XOM | ok | 2026-11-11 | 0 | 0 | 0 |
| UNH | ok | 2026-11-11 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
