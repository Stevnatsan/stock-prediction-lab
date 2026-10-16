# Stock prediction lab: latest report

Generated 2026-10-16 00:25 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **63.0%** | **Buy at open** | 65.6% | **Outperform** | 19 | positive (+0.10) | positive (+0.16) |
| 2 | AMZN | **54.2%** | **Buy at open** | 55.1% | **Outperform** | 41 | positive (+0.19) | neutral (-0.01) |
| 3 | JPM | **51.2%** | Stay out | 45.6% | – | 35 | neutral (+0.01) | neutral (+0.01) |
| 4 | TSLA | **50.5%** | Stay out | 39.5% | – | 33 | neutral (+0.05) | negative (-0.24) |
| 5 | AAPL | **50.1%** | Stay out | 48.4% | – | 35 | positive (+0.20) | positive (+0.12) |
| 6 | META | **48.9%** | Stay out | 45.4% | – | 47 | positive (+0.18) | neutral (-0.04) |
| 7 | GOOGL | **47.3%** | Stay out | 44.7% | – | 27 | positive (+0.12) | neutral (-0.04) |
| 8 | UNH | **46.5%** | Stay out | 35.9% | – | 19 | positive (+0.16) | positive (+0.14) |
| 9 | NVDA | **44.6%** | Stay out | 34.1% | – | 81 | neutral (+0.01) | negative (-0.20) |
| 10 | MSFT | **41.7%** | Stay out | 42.7% | – | 33 | positive (+0.14) | positive (+0.21) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 50.6% | 49.6% | 50.9% | 48.4% | 50.7% | 50.7% | 50.1% | 49.5% |
| AMZN | 52.9% | 55.7% | 55.8% | 55.1% | 52.7% | 50.4% | 54.2% | 52.8% |
| GOOGL | 44.6% | 46.1% | 45.3% | 44.7% | 48.6% | 48.6% | 47.3% | 46.7% |
| JPM | 51.2% | 49.2% | 47.4% | 45.6% | 53.2% | 51.1% | 51.2% | 48.3% |
| META | 51.6% | 46.2% | 48.1% | 45.4% | 51.6% | 50.4% | 48.9% | 47.9% |
| MSFT | 44.0% | 33.6% | 32.5% | 42.7% | 49.8% | 48.1% | 41.7% | 45.4% |
| NVDA | 41.6% | 39.5% | 40.6% | 34.1% | 49.7% | 48.5% | 44.6% | 41.3% |
| TSLA | 51.3% | 49.1% | 49.3% | 39.5% | 51.9% | 50.7% | 50.5% | 45.1% |
| UNH | 42.0% | 44.3% | 44.6% | 35.9% | 48.6% | 48.6% | 46.5% | 42.3% |
| XOM | 65.6% | 75.0% | 75.1% | 65.6% | 51.0% | 50.4% | 63.0% | 58.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 150 | **54.0%** | 46.0%–62.0% | 51.3% | 51.3% | within noise | 0.2483 |
| Live, logistic, all sources (VADER) | 150 | **56.0%** | 48.1%–63.9% | 51.3% | 51.3% | within noise | 0.2470 |
| Live, logistic, all sources (FinBERT) | 150 | **56.7%** | 48.7%–64.6% | 51.3% | 51.3% | within noise | 0.2475 |
| Live, gradient boosting | 150 | **50.0%** | 42.0%–58.0% | 51.3% | 51.3% | no | 0.2478 |
| Live, ensemble | 150 | **54.7%** | 46.7%–62.6% | 51.3% | 51.3% | within noise | 0.2456 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 150 | **58.0%** | 50.1%–65.9% | 50.0% | 46.7% | yes | 0.2471 |
| Live, gradient boosting | 150 | **57.3%** | 49.4%–65.2% | 50.0% | 46.7% | within noise | 0.2480 |
| Live, ensemble | 150 | **57.3%** | 49.4%–65.2% | 50.0% | 46.7% | within noise | 0.2461 |
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
| under 40% | 53.0% (n=249) | 50.9% (n=625) | 50.9% (n=627) | 55.0% (n=1,049) | 52.0% (n=475) |
| 40–45% | 51.9% (n=802) | 51.7% (n=1,117) | 51.7% (n=1,117) | 54.0% (n=1,046) | 52.7% (n=953) |
| 45–48% | 50.8% (n=1,303) | 50.5% (n=1,249) | 50.6% (n=1,252) | 50.9% (n=1,129) | 49.0% (n=1,215) |
| 48–50% | 52.3% (n=1,324) | 55.3% (n=1,150) | 55.2% (n=1,148) | 50.5% (n=999) | 51.4% (n=1,160) |
| 50–52% | 52.6% (n=1,712) | 51.1% (n=1,250) | 51.2% (n=1,249) | 47.5% (n=1,122) | 53.7% (n=1,407) |
| 52–55% | 52.2% (n=2,339) | 52.0% (n=1,760) | 52.0% (n=1,757) | 52.4% (n=1,601) | 52.6% (n=1,999) |
| 55–60% | 52.7% (n=2,129) | 52.4% (n=2,103) | 52.3% (n=2,104) | 52.7% (n=1,540) | 54.7% (n=1,885) |
| 60% or more | 52.3% (n=640) | 53.5% (n=1,244) | 53.5% (n=1,244) | 54.9% (n=1,422) | 50.1% (n=814) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.5% (n=941) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.9% (n=1,505) | 49.7% (n=1,260) | 47.4% (n=1,290) |
| 45–48% | 50.8% (n=1,449) | 49.9% (n=1,602) | 48.3% (n=1,707) |
| 48–50% | 49.5% (n=1,161) | 50.0% (n=1,447) | 51.3% (n=1,535) |
| 50–52% | 50.0% (n=1,197) | 51.0% (n=1,533) | 51.1% (n=1,473) |
| 52–55% | 52.4% (n=1,541) | 52.3% (n=1,574) | 50.9% (n=1,795) |
| 55–60% | 51.9% (n=1,678) | 50.0% (n=1,105) | 54.0% (n=1,310) |
| 60% or more | 52.8% (n=1,026) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 134 | 47.8% | -0.1% | 0.5% | +0.003 |
| FinBERT | 100 | 50.0% | -0.1% | 0.6% | -0.085 |

The two scorers agree on the direction of the mood on 71% of 160 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,050 | 51.4% | 49.5% | 49.5% | 48.3% | 50.4% | 54.5% |
| AMZN | 1,050 | 49.6% | 50.1% | 50.1% | 49.1% | 48.9% | 50.9% |
| GOOGL | 1,050 | 51.5% | 49.4% | 49.4% | 51.2% | 52.3% | 54.4% |
| JPM | 1,050 | 50.6% | 50.6% | 50.7% | 50.9% | 51.0% | 53.8% |
| META | 1,050 | 52.9% | 52.8% | 52.8% | 49.1% | 51.2% | 50.6% |
| MSFT | 1,050 | 51.6% | 52.0% | 52.0% | 50.2% | 52.2% | 51.9% |
| NVDA | 1,050 | 49.5% | 49.9% | 49.9% | 51.7% | 51.9% | 52.7% |
| TSLA | 1,050 | 53.0% | 53.1% | 53.1% | 49.7% | 52.6% | 49.8% |
| UNH | 1,049 | 50.2% | 48.6% | 48.6% | 49.9% | 52.1% | 51.5% |
| XOM | 1,049 | 49.8% | 48.7% | 48.7% | 51.2% | 53.2% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,050 | 51.1% | 50.9% | 51.7% | 53.1% |
| AMZN | 1,050 | 49.2% | 52.8% | 50.8% | 48.0% |
| GOOGL | 1,050 | 49.9% | 51.6% | 50.6% | 53.5% |
| JPM | 1,050 | 52.6% | 49.1% | 49.8% | 53.3% |
| META | 1,050 | 51.3% | 48.1% | 50.1% | 49.0% |
| MSFT | 1,050 | 51.0% | 50.3% | 50.3% | 48.9% |
| NVDA | 1,050 | 52.0% | 52.6% | 52.9% | 52.1% |
| TSLA | 1,050 | 52.7% | 51.7% | 53.7% | 48.7% |
| UNH | 1,049 | 53.4% | 50.4% | 51.5% | 47.7% |
| XOM | 1,049 | 51.4% | 49.4% | 51.4% | 49.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,050 | +40.6% | +8.5% | 0.50 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,050 | +36.7% | +7.8% | 0.49 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,050 | +36.7% | +7.8% | 0.49 | 50.3% |
| Top 3 by gradient boosting | 991 | +71.0% | +14.6% | 0.80 | 36.8% |
| Top 3 by ensemble | 991 | +38.2% | +8.6% | 0.54 | 46.0% |
| Buy every stock, every session | 1,050 | -1.0% | -0.2% | 0.07 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,050 | -22.9% | -6.0% | -0.37 | 47.0% |
| Top 3 by gradient boosting | 991 | -43.3% | -13.4% | -0.83 | 39.6% |
| Top 3 by ensemble | 991 | -13.6% | -3.6% | -0.16 | 46.4% |
| Every stock minus SPY | 1,050 | -53.9% | -16.9% | -2.41 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7774 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 732 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 992 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 168 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-15 | 0 | 8 | 35 |
| MSFT | ok | 2026-10-15 | 0 | 8 | 33 |
| NVDA | ok | 2026-10-15 | 0 | 8 | 81 |
| AMZN | ok | 2026-10-15 | 0 | 8 | 41 |
| GOOGL | ok | 2026-10-15 | 0 | 8 | 27 |
| META | ok | 2026-10-15 | 0 | 8 | 47 |
| TSLA | ok | 2026-10-15 | 0 | 8 | 33 |
| JPM | ok | 2026-10-15 | 0 | 8 | 35 |
| XOM | ok | 2026-10-15 | 0 | 8 | 19 |
| UNH | ok | 2026-10-15 | 0 | 8 | 19 |

---

Educational project. Not financial advice.
