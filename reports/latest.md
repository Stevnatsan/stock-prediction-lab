# Stock prediction lab: latest report

Generated 2026-11-18 08:32 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | UNH | **54.3%** | **Buy at open** | 60.1% | **Outperform** | 37 | neutral (+0.02) | negative (-0.27) |
| 2 | XOM | **52.0%** | Stay out | 56.5% | **Outperform** | 24 | neutral (+0.05) | positive (+0.09) |
| 3 | AAPL | **50.7%** | Stay out | 55.8% | – | 32 | positive (+0.12) | negative (-0.08) |
| 4 | META | **50.6%** | Stay out | 45.6% | – | 62 | positive (+0.14) | neutral (+0.02) |
| 5 | JPM | **50.1%** | Stay out | 44.8% | – | 38 | positive (+0.06) | negative (-0.25) |
| 6 | TSLA | **50.1%** | Stay out | 55.8% | **Outperform** | 34 | positive (+0.15) | positive (+0.06) |
| 7 | MSFT | **48.6%** | Stay out | 40.7% | – | 42 | positive (+0.07) | neutral (+0.03) |
| 8 | AMZN | **48.1%** | Stay out | 45.2% | – | 69 | positive (+0.21) | neutral (+0.02) |
| 9 | GOOGL | **37.3%** | Stay out | 43.6% | – | 41 | positive (+0.15) | negative (-0.08) |
| 10 | NVDA | **34.2%** | Stay out | 23.6% | – | 107 | neutral (+0.01) | negative (-0.15) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 52.0% | 50.8% | 52.9% | 55.8% | 50.5% | 49.4% | 50.7% | 52.6% |
| AMZN | 51.0% | 44.5% | 45.6% | 45.2% | 51.7% | 50.4% | 48.1% | 47.8% |
| GOOGL | 38.8% | 24.1% | 22.0% | 43.6% | 50.5% | 50.4% | 37.3% | 47.0% |
| JPM | 59.8% | 44.4% | 41.1% | 44.8% | 55.9% | 50.4% | 50.1% | 47.6% |
| META | 57.2% | 48.7% | 49.0% | 45.6% | 52.5% | 50.3% | 50.6% | 47.9% |
| MSFT | 53.6% | 43.9% | 44.8% | 40.7% | 53.4% | 50.4% | 48.6% | 45.5% |
| NVDA | 41.0% | 21.8% | 22.2% | 23.6% | 46.7% | 48.0% | 34.2% | 35.8% |
| TSLA | 47.6% | 49.3% | 48.6% | 55.8% | 50.9% | 48.2% | 50.1% | 52.0% |
| UNH | 61.2% | 57.1% | 58.1% | 60.1% | 51.5% | 50.4% | 54.3% | 55.2% |
| XOM | 54.1% | 53.7% | 53.7% | 56.5% | 50.2% | 50.4% | 52.0% | 53.5% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 380 | **51.1%** | 46.0%–56.1% | 45.5% | 49.2% | no | 0.2500 |
| Live, logistic, all sources (VADER) | 380 | **52.6%** | 47.6%–57.7% | 45.5% | 49.2% | no | 0.2512 |
| Live, logistic, all sources (FinBERT) | 380 | **53.7%** | 48.7%–58.7% | 45.5% | 49.2% | no | 0.2505 |
| Live, gradient boosting | 380 | **52.1%** | 47.1%–57.1% | 45.5% | 49.2% | no | 0.2475 |
| Live, ensemble | 380 | **53.7%** | 48.7%–58.7% | 45.5% | 49.2% | no | 0.2471 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 380 | **54.5%** | 49.5%–59.5% | 46.8% | 47.4% | within noise | 0.2529 |
| Live, gradient boosting | 380 | **53.4%** | 48.4%–58.4% | 46.8% | 47.4% | within noise | 0.2493 |
| Live, ensemble | 380 | **54.2%** | 49.2%–59.2% | 46.8% | 47.4% | within noise | 0.2493 |
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
| under 40% | 46.2% (n=13) | 41.2% (n=51) | 42.3% (n=52) | 42.9% (n=7) | 42.9% (n=7) |
| 40–45% | 43.1% (n=51) | 43.8% (n=64) | 40.0% (n=65) | 27.7% (n=47) | 29.5% (n=61) |
| 45–48% | 40.7% (n=59) | 45.5% (n=44) | 48.1% (n=52) | 53.3% (n=60) | 48.5% (n=66) |
| 48–50% | 47.8% (n=46) | 42.5% (n=40) | 39.5% (n=38) | 44.4% (n=63) | 47.2% (n=53) |
| 50–52% | 44.9% (n=49) | 51.6% (n=31) | 51.9% (n=27) | 44.8% (n=67) | 44.8% (n=58) |
| 52–55% | 42.4% (n=85) | 33.3% (n=51) | 41.9% (n=43) | 40.6% (n=69) | 50.7% (n=67) |
| 55–60% | 56.1% (n=57) | 50.9% (n=55) | 46.6% (n=58) | 54.7% (n=53) | 51.9% (n=52) |
| 60% or more | 45.0% (n=20) | 59.1% (n=44) | 57.8% (n=45) | 71.4% (n=14) | 50.0% (n=16) |
| **Average gap** | **5.8 pts** | **6.1 pts** | **6.3 pts** | **7.9 pts** | **5.5 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 41.7% (n=48) | – | 57.1% (n=7) |
| 40–45% | 41.9% (n=74) | – | 40.0% (n=50) |
| 45–48% | 42.6% (n=47) | 36.1% (n=36) | 39.3% (n=84) |
| 48–50% | 46.7% (n=30) | 45.3% (n=159) | 49.2% (n=65) |
| 50–52% | 55.9% (n=34) | 50.6% (n=178) | 52.4% (n=63) |
| 52–55% | 57.4% (n=54) | 42.9% (n=7) | 51.7% (n=60) |
| 55–60% | 42.2% (n=45) | – | 50.0% (n=48) |
| 60% or more | 50.0% (n=48) | – | 33.3% (n=3) |
| **Average gap** | **6.3 pts** | **3.0 pts** | **4.0 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 321 | 47.0% | -0.3% | -0.6% | -0.045 |
| FinBERT | 252 | 48.8% | -0.2% | -0.0% | -0.019 |

The two scorers agree on the direction of the mood on 65% of 390 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 38 | 39.5% | 52.6% | 52.6% | 36.8% | 47.4% | 55.3% |
| AMZN | 38 | 57.9% | 55.3% | 55.3% | 42.1% | 44.7% | 44.7% |
| GOOGL | 38 | 57.9% | 55.3% | 55.3% | 65.8% | 73.7% | 39.5% |
| JPM | 38 | 50.0% | 44.7% | 55.3% | 36.8% | 36.8% | 36.8% |
| META | 38 | 47.4% | 52.6% | 50.0% | 57.9% | 57.9% | 39.5% |
| MSFT | 38 | 47.4% | 52.6% | 52.6% | 63.2% | 50.0% | 47.4% |
| NVDA | 38 | 55.3% | 57.9% | 57.9% | 57.9% | 60.5% | 28.9% |
| TSLA | 38 | 47.4% | 55.3% | 55.3% | 47.4% | 50.0% | 52.6% |
| UNH | 38 | 50.0% | 44.7% | 44.7% | 60.5% | 55.3% | 50.0% |
| XOM | 38 | 57.9% | 55.3% | 57.9% | 52.6% | 60.5% | 60.5% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 38 | 60.5% | 47.4% | 65.8% | 65.8% |
| AMZN | 38 | 47.4% | 55.3% | 47.4% | 47.4% |
| GOOGL | 38 | 55.3% | 60.5% | 52.6% | 42.1% |
| JPM | 38 | 47.4% | 57.9% | 47.4% | 39.5% |
| META | 38 | 52.6% | 39.5% | 47.4% | 36.8% |
| MSFT | 38 | 57.9% | 52.6% | 57.9% | 47.4% |
| NVDA | 38 | 55.3% | 47.4% | 55.3% | 31.6% |
| TSLA | 38 | 55.3% | 60.5% | 55.3% | 52.6% |
| UNH | 38 | 52.6% | 55.3% | 52.6% | 44.7% |
| XOM | 38 | 60.5% | 57.9% | 60.5% | 60.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,073 | +34.9% | +7.3% | 0.45 | 50.8% |
| Top 3 by logistic, all sources (VADER) | 1,073 | +34.6% | +7.2% | 0.46 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,073 | +32.1% | +6.8% | 0.44 | 50.2% |
| Top 3 by gradient boosting | 1,014 | +59.4% | +12.3% | 0.69 | 36.9% |
| Top 3 by ensemble | 1,014 | +28.0% | +6.3% | 0.43 | 46.0% |
| Buy every stock, every session | 1,073 | -9.8% | -2.4% | -0.05 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,073 | -21.7% | -5.6% | -0.33 | 46.9% |
| Top 3 by gradient boosting | 1,014 | -43.6% | -13.3% | -0.82 | 38.8% |
| Top 3 by ensemble | 1,014 | -11.5% | -3.0% | -0.11 | 46.3% |
| Every stock minus SPY | 1,073 | -56.0% | -17.5% | -2.51 | 41.9% |

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
| google_news | 10 | 0 | 869 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 166 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-17 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-17 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-17 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-17 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-17 | 0 | 0 | 0 |
| META | ok | 2026-11-17 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-17 | 0 | 0 | 0 |
| JPM | ok | 2026-11-17 | 0 | 0 | 0 |
| XOM | ok | 2026-11-17 | 0 | 0 | 0 |
| UNH | ok | 2026-11-17 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
