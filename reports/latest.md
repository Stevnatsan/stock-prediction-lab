# Stock prediction lab: latest report

Generated 2026-10-10 01:46 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **60.5%** | **Buy at open** | 61.8% | **Outperform** | 21 | negative (-0.06) | negative (-0.12) |
| 2 | GOOGL | **56.2%** | **Buy at open** | 51.1% | – | 31 | positive (+0.16) | positive (+0.11) |
| 3 | JPM | **56.1%** | **Buy at open** | 62.0% | **Outperform** | 29 | positive (+0.19) | positive (+0.18) |
| 4 | AMZN | **54.6%** | Stay out | 48.5% | – | 48 | positive (+0.16) | neutral (+0.01) |
| 5 | UNH | **51.1%** | Stay out | 35.4% | – | 23 | positive (+0.20) | positive (+0.10) |
| 6 | NVDA | **51.0%** | Stay out | 52.9% | – | 87 | positive (+0.07) | neutral (-0.03) |
| 7 | MSFT | **49.3%** | Stay out | 54.8% | – | 35 | positive (+0.10) | neutral (+0.01) |
| 8 | TSLA | **49.1%** | Stay out | 45.1% | – | 30 | positive (+0.15) | positive (+0.22) |
| 9 | AAPL | **48.5%** | Stay out | 58.2% | **Outperform** | 41 | negative (-0.06) | negative (-0.38) |
| 10 | META | **46.6%** | Stay out | 46.3% | – | 49 | positive (+0.09) | negative (-0.15) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 47.4% | 51.7% | 47.7% | 58.2% | 45.2% | 49.8% | 48.5% | 54.0% |
| AMZN | 53.3% | 56.3% | 56.2% | 48.5% | 53.0% | 46.2% | 54.6% | 47.3% |
| GOOGL | 56.2% | 59.0% | 59.6% | 51.1% | 53.4% | 47.3% | 56.2% | 49.2% |
| JPM | 54.8% | 57.8% | 58.8% | 62.0% | 54.5% | 53.0% | 56.1% | 57.5% |
| META | 46.9% | 42.5% | 43.2% | 46.3% | 50.6% | 49.4% | 46.6% | 47.8% |
| MSFT | 54.3% | 46.7% | 46.9% | 54.8% | 51.9% | 49.0% | 49.3% | 51.9% |
| NVDA | 53.4% | 49.3% | 49.4% | 52.9% | 52.8% | 49.9% | 51.0% | 51.4% |
| TSLA | 48.9% | 48.5% | 49.0% | 45.1% | 49.7% | 46.9% | 49.1% | 46.0% |
| UNH | 47.7% | 48.1% | 47.8% | 35.4% | 54.0% | 45.2% | 51.1% | 40.3% |
| XOM | 59.1% | 68.6% | 65.3% | 61.8% | 52.5% | 50.0% | 60.5% | 55.9% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 110 | **59.1%** | 49.9%–68.3% | 52.7% | 54.5% | within noise | 0.2462 |
| Live, logistic, all sources (VADER) | 110 | **60.9%** | 51.8%–70.0% | 52.7% | 54.5% | within noise | 0.2422 |
| Live, logistic, all sources (FinBERT) | 110 | **61.8%** | 52.7%–70.9% | 52.7% | 54.5% | within noise | 0.2419 |
| Live, gradient boosting | 110 | **49.1%** | 39.7%–58.4% | 52.7% | 54.5% | no | 0.2478 |
| Live, ensemble | 110 | **60.0%** | 50.8%–69.2% | 52.7% | 54.5% | within noise | 0.2433 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 110 | **60.0%** | 50.8%–69.2% | 50.0% | 49.1% | yes | 0.2465 |
| Live, gradient boosting | 110 | **60.0%** | 50.8%–69.2% | 50.0% | 49.1% | yes | 0.2489 |
| Live, ensemble | 110 | **58.2%** | 49.0%–67.4% | 50.0% | 49.1% | within noise | 0.2464 |
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
| under 40% | 53.0% (n=247) | 50.8% (n=618) | 50.8% (n=620) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=797) | 51.6% (n=1,111) | 51.5% (n=1,110) | 54.2% (n=1,040) | 52.6% (n=946) |
| 45–48% | 50.7% (n=1,296) | 50.5% (n=1,246) | 50.5% (n=1,247) | 50.8% (n=1,123) | 48.9% (n=1,206) |
| 48–50% | 52.4% (n=1,321) | 55.4% (n=1,146) | 55.4% (n=1,145) | 50.6% (n=993) | 51.3% (n=1,156) |
| 50–52% | 52.7% (n=1,709) | 51.1% (n=1,248) | 51.2% (n=1,248) | 47.3% (n=1,108) | 53.9% (n=1,403) |
| 52–55% | 52.4% (n=2,327) | 52.1% (n=1,753) | 52.1% (n=1,751) | 52.5% (n=1,593) | 52.7% (n=1,991) |
| 55–60% | 52.6% (n=2,122) | 52.5% (n=2,097) | 52.4% (n=2,098) | 52.7% (n=1,540) | 54.7% (n=1,880) |
| 60% or more | 52.3% (n=639) | 53.3% (n=1,239) | 53.3% (n=1,239) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=932) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,501) | 49.7% (n=1,260) | 47.6% (n=1,282) |
| 45–48% | 50.7% (n=1,444) | 50.1% (n=1,592) | 48.2% (n=1,698) |
| 48–50% | 49.6% (n=1,158) | 49.8% (n=1,427) | 51.3% (n=1,529) |
| 50–52% | 50.0% (n=1,193) | 51.0% (n=1,524) | 51.1% (n=1,469) |
| 52–55% | 52.5% (n=1,538) | 52.3% (n=1,573) | 50.9% (n=1,791) |
| 55–60% | 51.9% (n=1,674) | 50.0% (n=1,105) | 54.1% (n=1,302) |
| 60% or more | 52.8% (n=1,018) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 98 | 51.0% | -0.1% | 0.1% | -0.017 |
| FinBERT | 72 | 54.2% | -0.0% | 0.5% | -0.051 |

The two scorers agree on the direction of the mood on 70% of 120 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,046 | 51.5% | 49.6% | 49.6% | 48.4% | 50.6% | 54.6% |
| AMZN | 1,046 | 49.7% | 50.2% | 50.2% | 49.1% | 49.0% | 51.0% |
| GOOGL | 1,046 | 51.5% | 49.4% | 49.4% | 51.1% | 52.2% | 54.4% |
| JPM | 1,046 | 50.8% | 50.8% | 50.9% | 51.0% | 51.1% | 53.9% |
| META | 1,046 | 53.0% | 52.9% | 52.9% | 49.2% | 51.3% | 50.5% |
| MSFT | 1,046 | 51.6% | 52.0% | 52.0% | 49.9% | 52.2% | 51.9% |
| NVDA | 1,046 | 49.5% | 49.9% | 49.9% | 51.7% | 52.0% | 52.7% |
| TSLA | 1,046 | 53.0% | 53.2% | 53.2% | 49.7% | 52.6% | 49.8% |
| UNH | 1,045 | 50.2% | 48.5% | 48.5% | 49.9% | 52.1% | 51.5% |
| XOM | 1,045 | 49.7% | 48.6% | 48.6% | 51.1% | 53.1% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,046 | 51.1% | 51.0% | 51.6% | 53.2% |
| AMZN | 1,046 | 49.2% | 52.8% | 50.7% | 48.1% |
| GOOGL | 1,046 | 49.9% | 51.7% | 50.7% | 53.5% |
| JPM | 1,046 | 52.6% | 49.0% | 49.8% | 53.3% |
| META | 1,046 | 51.4% | 48.2% | 50.2% | 48.9% |
| MSFT | 1,046 | 51.0% | 50.4% | 50.3% | 48.9% |
| NVDA | 1,046 | 52.1% | 52.5% | 53.0% | 52.1% |
| TSLA | 1,046 | 52.6% | 51.5% | 53.6% | 48.8% |
| UNH | 1,045 | 53.3% | 50.4% | 51.4% | 47.7% |
| XOM | 1,045 | 51.3% | 49.4% | 51.3% | 49.8% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,046 | +38.6% | +8.2% | 0.49 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,046 | +34.9% | +7.5% | 0.47 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,046 | +34.9% | +7.5% | 0.47 | 50.2% |
| Top 3 by gradient boosting | 987 | +71.4% | +14.7% | 0.81 | 37.0% |
| Top 3 by ensemble | 987 | +37.2% | +8.4% | 0.53 | 46.0% |
| Buy every stock, every session | 1,046 | -0.5% | -0.1% | 0.08 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,046 | -23.6% | -6.3% | -0.39 | 46.9% |
| Top 3 by gradient boosting | 987 | -42.9% | -13.3% | -0.82 | 39.7% |
| Top 3 by ensemble | 987 | -14.4% | -3.9% | -0.18 | 46.4% |
| Every stock minus SPY | 1,046 | -53.5% | -16.9% | -2.40 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7681 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 679 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 999 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 157 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-09 | 0 | 8 | 41 |
| MSFT | ok | 2026-10-09 | 0 | 8 | 35 |
| NVDA | ok | 2026-10-09 | 0 | 8 | 87 |
| AMZN | ok | 2026-10-09 | 0 | 8 | 48 |
| GOOGL | ok | 2026-10-09 | 0 | 8 | 31 |
| META | ok | 2026-10-09 | 0 | 8 | 49 |
| TSLA | ok | 2026-10-09 | 0 | 8 | 30 |
| JPM | ok | 2026-10-09 | 0 | 8 | 29 |
| XOM | ok | 2026-10-09 | 0 | 8 | 21 |
| UNH | ok | 2026-10-09 | 0 | 8 | 23 |

---

Educational project. Not financial advice.
