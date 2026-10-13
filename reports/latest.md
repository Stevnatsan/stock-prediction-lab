# Stock prediction lab: latest report

Generated 2026-10-13 07:42 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **69.1%** | **Buy at open** | 61.0% | **Outperform** | 22 | neutral (+0.04) | neutral (-0.02) |
| 2 | AAPL | **59.2%** | **Buy at open** | 60.3% | **Outperform** | 34 | positive (+0.10) | positive (+0.12) |
| 3 | GOOGL | **57.7%** | **Buy at open** | 53.2% | – | 28 | positive (+0.17) | positive (+0.10) |
| 4 | AMZN | **57.4%** | Stay out | 60.1% | – | 45 | positive (+0.19) | positive (+0.06) |
| 5 | JPM | **53.6%** | Stay out | 62.7% | **Outperform** | 28 | positive (+0.11) | positive (+0.05) |
| 6 | NVDA | **46.5%** | Stay out | 49.5% | – | 60 | positive (+0.12) | negative (-0.08) |
| 7 | MSFT | **45.7%** | Stay out | 56.0% | – | 37 | positive (+0.07) | neutral (+0.01) |
| 8 | UNH | **42.5%** | Stay out | 35.1% | – | 27 | positive (+0.10) | positive (+0.05) |
| 9 | META | **41.2%** | Stay out | 44.5% | – | 60 | positive (+0.06) | positive (+0.17) |
| 10 | TSLA | **39.4%** | Stay out | 38.1% | – | 21 | positive (+0.05) | positive (+0.11) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 56.3% | 59.2% | 58.4% | 60.3% | 49.4% | 50.4% | 54.3% | 55.4% |
| AMZN | 55.4% | 57.4% | 57.1% | 60.1% | 50.0% | 50.4% | 53.7% | 55.3% |
| GOOGL | 54.4% | 57.7% | 58.3% | 53.2% | 50.8% | 50.4% | 54.2% | 51.8% |
| JPM | 53.1% | 53.6% | 52.4% | 62.7% | 41.6% | 48.5% | 47.6% | 55.6% |
| META | 43.4% | 41.2% | 39.1% | 44.5% | 46.2% | 50.6% | 43.7% | 47.6% |
| MSFT | 53.2% | 45.7% | 45.7% | 56.0% | 49.2% | 51.0% | 47.4% | 53.5% |
| NVDA | 51.4% | 46.5% | 46.2% | 49.5% | 50.4% | 50.4% | 48.4% | 50.0% |
| TSLA | 43.4% | 39.4% | 40.7% | 38.1% | 50.4% | 50.4% | 44.9% | 44.2% |
| UNH | 52.1% | 42.5% | 42.6% | 35.1% | 41.4% | 47.6% | 42.0% | 41.4% |
| XOM | 58.7% | 69.1% | 67.2% | 61.0% | 52.0% | 50.4% | 60.5% | 55.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 120 | **58.3%** | 49.5%–67.2% | 52.5% | 54.2% | within noise | 0.2462 |
| Live, logistic, all sources (VADER) | 120 | **60.8%** | 52.1%–69.6% | 52.5% | 54.2% | within noise | 0.2427 |
| Live, logistic, all sources (FinBERT) | 120 | **60.8%** | 52.1%–69.6% | 52.5% | 54.2% | within noise | 0.2429 |
| Live, gradient boosting | 120 | **49.2%** | 40.2%–58.1% | 52.5% | 54.2% | no | 0.2489 |
| Live, ensemble | 120 | **57.5%** | 48.7%–66.3% | 52.5% | 54.2% | within noise | 0.2441 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 120 | **61.7%** | 53.0%–70.4% | 50.8% | 50.0% | yes | 0.2429 |
| Live, gradient boosting | 120 | **59.2%** | 50.4%–68.0% | 50.8% | 50.0% | within noise | 0.2482 |
| Live, ensemble | 120 | **59.2%** | 50.4%–68.0% | 50.8% | 50.0% | within noise | 0.2443 |
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
| 40–45% | 51.8% (n=797) | 51.6% (n=1,112) | 51.6% (n=1,111) | 54.2% (n=1,040) | 52.6% (n=946) |
| 45–48% | 50.7% (n=1,299) | 50.5% (n=1,247) | 50.6% (n=1,250) | 50.8% (n=1,124) | 49.0% (n=1,207) |
| 48–50% | 52.3% (n=1,322) | 55.3% (n=1,149) | 55.3% (n=1,147) | 50.5% (n=994) | 51.3% (n=1,159) |
| 50–52% | 52.7% (n=1,709) | 51.2% (n=1,249) | 51.2% (n=1,248) | 47.4% (n=1,110) | 53.8% (n=1,405) |
| 52–55% | 52.3% (n=2,331) | 52.1% (n=1,753) | 52.1% (n=1,751) | 52.5% (n=1,599) | 52.7% (n=1,992) |
| 55–60% | 52.7% (n=2,124) | 52.4% (n=2,100) | 52.4% (n=2,101) | 52.7% (n=1,540) | 54.7% (n=1,882) |
| 60% or more | 52.3% (n=639) | 53.4% (n=1,240) | 53.4% (n=1,240) | 54.9% (n=1,422) | 50.1% (n=813) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=933) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,501) | 49.7% (n=1,260) | 47.5% (n=1,283) |
| 45–48% | 50.7% (n=1,446) | 50.0% (n=1,596) | 48.2% (n=1,701) |
| 48–50% | 49.5% (n=1,159) | 49.9% (n=1,432) | 51.3% (n=1,530) |
| 50–52% | 50.0% (n=1,194) | 51.0% (n=1,524) | 51.1% (n=1,471) |
| 52–55% | 52.5% (n=1,540) | 52.3% (n=1,574) | 50.9% (n=1,792) |
| 55–60% | 51.9% (n=1,675) | 50.0% (n=1,105) | 54.1% (n=1,304) |
| 60% or more | 52.9% (n=1,020) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 108 | 49.1% | -0.1% | 0.5% | -0.072 |
| FinBERT | 79 | 50.6% | -0.1% | 0.6% | -0.119 |

The two scorers agree on the direction of the mood on 71% of 130 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,047 | 51.5% | 49.7% | 49.6% | 48.4% | 50.5% | 54.6% |
| AMZN | 1,047 | 49.7% | 50.1% | 50.1% | 49.1% | 49.0% | 50.9% |
| GOOGL | 1,047 | 51.6% | 49.5% | 49.5% | 51.1% | 52.2% | 54.4% |
| JPM | 1,047 | 50.7% | 50.7% | 50.8% | 50.9% | 51.0% | 53.9% |
| META | 1,047 | 52.9% | 52.8% | 52.8% | 49.3% | 51.2% | 50.5% |
| MSFT | 1,047 | 51.7% | 52.0% | 52.0% | 50.0% | 52.1% | 52.0% |
| NVDA | 1,047 | 49.5% | 50.0% | 50.0% | 51.6% | 51.9% | 52.6% |
| TSLA | 1,047 | 53.0% | 53.2% | 53.2% | 49.8% | 52.6% | 49.8% |
| UNH | 1,046 | 50.3% | 48.6% | 48.6% | 49.8% | 52.1% | 51.4% |
| XOM | 1,046 | 49.7% | 48.7% | 48.7% | 51.2% | 53.2% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,047 | 51.2% | 50.9% | 51.6% | 53.2% |
| AMZN | 1,047 | 49.3% | 52.8% | 50.7% | 48.0% |
| GOOGL | 1,047 | 50.0% | 51.6% | 50.6% | 53.6% |
| JPM | 1,047 | 52.6% | 49.1% | 49.9% | 53.4% |
| META | 1,047 | 51.4% | 48.2% | 50.1% | 48.9% |
| MSFT | 1,047 | 51.0% | 50.3% | 50.3% | 48.9% |
| NVDA | 1,047 | 52.1% | 52.5% | 52.9% | 52.1% |
| TSLA | 1,047 | 52.6% | 51.5% | 53.6% | 48.7% |
| UNH | 1,046 | 53.3% | 50.5% | 51.5% | 47.6% |
| XOM | 1,046 | 51.3% | 49.3% | 51.4% | 49.8% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,047 | +38.9% | +8.2% | 0.49 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,047 | +35.3% | +7.5% | 0.48 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,047 | +35.3% | +7.5% | 0.48 | 50.2% |
| Top 3 by gradient boosting | 988 | +72.9% | +15.0% | 0.82 | 36.9% |
| Top 3 by ensemble | 988 | +37.6% | +8.5% | 0.54 | 46.1% |
| Buy every stock, every session | 1,047 | -0.5% | -0.1% | 0.08 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,047 | -23.3% | -6.2% | -0.38 | 47.0% |
| Top 3 by gradient boosting | 988 | -42.9% | -13.3% | -0.82 | 39.7% |
| Top 3 by ensemble | 988 | -13.9% | -3.8% | -0.17 | 46.5% |
| Every stock minus SPY | 1,047 | -53.5% | -16.8% | -2.40 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7686 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 189 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1000 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 173 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-12 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-12 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-12 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-12 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-12 | 0 | 0 | 0 |
| META | ok | 2026-10-12 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-12 | 0 | 0 | 0 |
| JPM | ok | 2026-10-12 | 0 | 0 | 0 |
| XOM | ok | 2026-10-12 | 0 | 0 | 0 |
| UNH | ok | 2026-10-12 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
