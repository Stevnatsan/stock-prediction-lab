# Stock prediction lab: latest report

Generated 2026-11-13 02:38 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **54.9%** | **Buy at open** | 54.3% | **Outperform** | 43 | positive (+0.13) | negative (-0.06) |
| 2 | XOM | **53.9%** | **Buy at open** | 53.1% | – | 36 | positive (+0.08) | positive (+0.16) |
| 3 | MSFT | **53.7%** | **Buy at open** | 53.8% | **Outperform** | 48 | positive (+0.11) | positive (+0.08) |
| 4 | AAPL | **53.4%** | Stay out | 53.5% | – | 38 | positive (+0.09) | neutral (+0.05) |
| 5 | JPM | **50.6%** | Stay out | 47.7% | – | 22 | positive (+0.09) | positive (+0.20) |
| 6 | UNH | **50.3%** | Stay out | 44.3% | – | 15 | positive (+0.25) | neutral (+0.04) |
| 7 | TSLA | **48.1%** | Stay out | 55.5% | **Outperform** | 40 | positive (+0.07) | neutral (+0.04) |
| 8 | AMZN | **44.9%** | Stay out | 44.6% | – | 37 | positive (+0.25) | positive (+0.12) |
| 9 | GOOGL | **44.5%** | Stay out | 51.1% | – | 38 | positive (+0.09) | negative (-0.06) |
| 10 | NVDA | **42.9%** | Stay out | 34.7% | – | 106 | negative (-0.05) | negative (-0.38) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 52.2% | 53.7% | 53.1% | 53.5% | 53.1% | 52.3% | 53.4% | 52.9% |
| AMZN | 46.1% | 39.0% | 38.8% | 44.6% | 50.9% | 51.2% | 44.9% | 47.9% |
| GOOGL | 46.3% | 39.1% | 38.3% | 51.1% | 49.9% | 49.3% | 44.5% | 50.2% |
| JPM | 56.4% | 48.5% | 48.9% | 47.7% | 52.8% | 52.3% | 50.6% | 50.0% |
| META | 62.7% | 56.3% | 57.3% | 54.3% | 53.5% | 51.4% | 54.9% | 52.9% |
| MSFT | 58.4% | 55.9% | 55.9% | 53.8% | 51.4% | 51.2% | 53.7% | 52.5% |
| NVDA | 46.7% | 44.6% | 44.4% | 34.7% | 41.2% | 51.6% | 42.9% | 43.1% |
| TSLA | 40.6% | 46.7% | 47.1% | 55.5% | 49.5% | 48.4% | 48.1% | 51.9% |
| UNH | 44.5% | 47.6% | 46.2% | 44.3% | 53.0% | 51.2% | 50.3% | 47.8% |
| XOM | 53.4% | 57.0% | 56.6% | 53.1% | 50.8% | 48.9% | 53.9% | 51.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 350 | **52.3%** | 47.1%–57.5% | 48.3% | 48.0% | within noise | 0.2494 |
| Live, logistic, all sources (VADER) | 350 | **52.6%** | 47.3%–57.8% | 48.3% | 48.0% | within noise | 0.2517 |
| Live, logistic, all sources (FinBERT) | 350 | **53.1%** | 47.9%–58.4% | 48.3% | 48.0% | within noise | 0.2513 |
| Live, gradient boosting | 350 | **51.7%** | 46.5%–56.9% | 48.3% | 48.0% | no | 0.2475 |
| Live, ensemble | 350 | **54.0%** | 48.8%–59.2% | 48.3% | 48.0% | within noise | 0.2474 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 350 | **54.6%** | 49.4%–59.8% | 47.4% | 47.4% | within noise | 0.2529 |
| Live, gradient boosting | 350 | **53.4%** | 48.2%–58.7% | 47.4% | 47.4% | within noise | 0.2494 |
| Live, ensemble | 350 | **54.3%** | 49.1%–59.5% | 47.4% | 47.4% | within noise | 0.2494 |
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
| 40–45% | 44.7% (n=47) | 44.4% (n=63) | 42.6% (n=61) | 31.0% (n=42) | 32.7% (n=55) |
| 45–48% | 44.4% (n=54) | 51.3% (n=39) | 51.1% (n=47) | 56.4% (n=55) | 50.0% (n=62) |
| 48–50% | 46.7% (n=45) | 44.4% (n=36) | 42.9% (n=35) | 48.3% (n=58) | 50.0% (n=48) |
| 50–52% | 50.0% (n=44) | 53.3% (n=30) | 51.9% (n=27) | 46.0% (n=63) | 51.0% (n=51) |
| 52–55% | 45.6% (n=79) | 37.0% (n=46) | 45.0% (n=40) | 44.1% (n=59) | 52.5% (n=61) |
| 55–60% | 59.6% (n=52) | 55.3% (n=47) | 51.0% (n=49) | 55.8% (n=52) | 54.0% (n=50) |
| 60% or more | 47.1% (n=17) | 59.1% (n=44) | 57.8% (n=45) | 71.4% (n=14) | 50.0% (n=16) |
| **Average gap** | **4.4 pts** | **5.9 pts** | **5.3 pts** | **6.2 pts** | **3.7 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 42.2% (n=45) | – | 66.7% (n=6) |
| 40–45% | 42.9% (n=70) | – | 40.4% (n=47) |
| 45–48% | 41.9% (n=43) | 37.1% (n=35) | 39.5% (n=81) |
| 48–50% | 48.3% (n=29) | 46.1% (n=154) | 50.0% (n=60) |
| 50–52% | 56.7% (n=30) | 51.9% (n=156) | 52.6% (n=57) |
| 52–55% | 55.3% (n=47) | 20.0% (n=5) | 51.0% (n=51) |
| 55–60% | 45.0% (n=40) | – | 53.3% (n=45) |
| 60% or more | 52.2% (n=46) | – | 33.3% (n=3) |
| **Average gap** | **5.3 pts** | **3.4 pts** | **4.0 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 297 | 48.8% | -0.2% | 0.0% | -0.062 |
| FinBERT | 234 | 47.9% | -0.1% | 0.1% | -0.079 |

The two scorers agree on the direction of the mood on 66% of 360 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 35 | 42.9% | 54.3% | 51.4% | 34.3% | 45.7% | 60.0% |
| AMZN | 35 | 57.1% | 54.3% | 54.3% | 45.7% | 42.9% | 45.7% |
| GOOGL | 35 | 57.1% | 51.4% | 51.4% | 65.7% | 71.4% | 42.9% |
| JPM | 35 | 54.3% | 42.9% | 51.4% | 37.1% | 37.1% | 40.0% |
| META | 35 | 48.6% | 54.3% | 51.4% | 60.0% | 60.0% | 40.0% |
| MSFT | 35 | 48.6% | 54.3% | 54.3% | 60.0% | 51.4% | 48.6% |
| NVDA | 35 | 54.3% | 57.1% | 57.1% | 60.0% | 60.0% | 31.4% |
| TSLA | 35 | 48.6% | 54.3% | 54.3% | 42.9% | 48.6% | 57.1% |
| UNH | 35 | 48.6% | 42.9% | 42.9% | 60.0% | 57.1% | 51.4% |
| XOM | 35 | 62.9% | 60.0% | 62.9% | 51.4% | 65.7% | 65.7% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 35 | 57.1% | 42.9% | 62.9% | 62.9% |
| AMZN | 35 | 45.7% | 57.1% | 45.7% | 48.6% |
| GOOGL | 35 | 54.3% | 62.9% | 51.4% | 45.7% |
| JPM | 35 | 51.4% | 57.1% | 51.4% | 40.0% |
| META | 35 | 54.3% | 37.1% | 48.6% | 37.1% |
| MSFT | 35 | 57.1% | 54.3% | 57.1% | 48.6% |
| NVDA | 35 | 54.3% | 51.4% | 54.3% | 34.3% |
| TSLA | 35 | 57.1% | 60.0% | 57.1% | 54.3% |
| UNH | 35 | 54.3% | 51.4% | 54.3% | 42.9% |
| XOM | 35 | 60.0% | 60.0% | 60.0% | 60.0% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,070 | +37.2% | +7.7% | 0.47 | 50.8% |
| Top 3 by logistic, all sources (VADER) | 1,070 | +36.6% | +7.6% | 0.48 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,070 | +34.4% | +7.2% | 0.46 | 50.3% |
| Top 3 by gradient boosting | 1,011 | +58.8% | +12.2% | 0.69 | 36.9% |
| Top 3 by ensemble | 1,011 | +30.6% | +6.9% | 0.46 | 46.0% |
| Buy every stock, every session | 1,070 | -6.5% | -1.6% | -0.00 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,070 | -22.0% | -5.7% | -0.34 | 46.8% |
| Top 3 by gradient boosting | 1,011 | -43.8% | -13.4% | -0.83 | 38.8% |
| Top 3 by ensemble | 1,011 | -12.4% | -3.2% | -0.13 | 46.2% |
| Every stock minus SPY | 1,070 | -55.6% | -17.4% | -2.49 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7869 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 800 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 876 |  |
| macro_yahoo | 1 | 0 | 1090 |  |
| major_news | 10 | 0 | 999 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11968 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 178 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-12 | 0 | 8 | 38 |
| MSFT | ok | 2026-11-12 | 0 | 8 | 48 |
| NVDA | ok | 2026-11-12 | 0 | 8 | 106 |
| AMZN | ok | 2026-11-12 | 0 | 8 | 37 |
| GOOGL | ok | 2026-11-12 | 0 | 8 | 38 |
| META | ok | 2026-11-12 | 0 | 8 | 43 |
| TSLA | ok | 2026-11-12 | 0 | 8 | 40 |
| JPM | ok | 2026-11-12 | 0 | 8 | 22 |
| XOM | ok | 2026-11-12 | 0 | 8 | 36 |
| UNH | ok | 2026-11-12 | 0 | 8 | 15 |

---

Educational project. Not financial advice.
