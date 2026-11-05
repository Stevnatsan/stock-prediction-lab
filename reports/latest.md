# Stock prediction lab: latest report

Generated 2026-11-05 07:55 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | AAPL | **55.2%** | **Buy at open** | 49.8% | – | 46 | positive (+0.17) | neutral (+0.02) |
| 2 | TSLA | **52.4%** | **Buy at open** | 59.6% | **Outperform** | 44 | positive (+0.12) | negative (-0.23) |
| 3 | GOOGL | **52.3%** | **Buy at open** | 61.5% | **Outperform** | 40 | positive (+0.13) | neutral (-0.05) |
| 4 | AMZN | **51.3%** | Stay out | 30.9% | – | 61 | positive (+0.27) | positive (+0.07) |
| 5 | META | **49.8%** | Stay out | 42.1% | – | 43 | positive (+0.17) | neutral (+0.01) |
| 6 | NVDA | **49.3%** | Stay out | 45.8% | – | 64 | positive (+0.09) | negative (-0.07) |
| 7 | UNH | **46.4%** | Stay out | 35.8% | – | 13 | neutral (-0.04) | negative (-0.22) |
| 8 | XOM | **42.5%** | Stay out | 41.5% | – | 35 | positive (+0.14) | neutral (-0.00) |
| 9 | JPM | **42.1%** | Stay out | 31.8% | – | 14 | positive (+0.15) | positive (+0.23) |
| 10 | MSFT | **41.0%** | Stay out | 29.7% | – | 39 | positive (+0.17) | positive (+0.13) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 64.2% | 67.8% | 70.2% | 49.8% | 42.6% | 48.9% | 55.2% | 49.3% |
| AMZN | 47.2% | 51.0% | 52.2% | 30.9% | 51.5% | 48.9% | 51.3% | 39.9% |
| GOOGL | 51.5% | 53.6% | 53.4% | 61.5% | 51.1% | 50.0% | 52.3% | 55.8% |
| JPM | 41.7% | 33.1% | 34.7% | 31.8% | 51.2% | 48.9% | 42.1% | 40.3% |
| META | 49.8% | 44.1% | 45.1% | 42.1% | 55.4% | 49.4% | 49.8% | 45.7% |
| MSFT | 38.6% | 31.3% | 31.0% | 29.7% | 50.7% | 48.6% | 41.0% | 39.2% |
| NVDA | 46.2% | 44.8% | 44.5% | 45.8% | 53.8% | 51.1% | 49.3% | 48.5% |
| TSLA | 44.8% | 54.2% | 53.5% | 59.6% | 50.6% | 49.4% | 52.4% | 54.5% |
| UNH | 46.6% | 40.8% | 43.3% | 35.8% | 52.0% | 48.9% | 46.4% | 42.3% |
| XOM | 45.4% | 43.0% | 43.5% | 41.5% | 42.1% | 50.0% | 42.5% | 45.8% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 290 | **52.1%** | 46.3%–57.8% | 47.6% | 48.6% | no | 0.2495 |
| Live, logistic, all sources (VADER) | 290 | **53.1%** | 47.4%–58.8% | 47.6% | 48.6% | within noise | 0.2519 |
| Live, logistic, all sources (FinBERT) | 290 | **53.4%** | 47.7%–59.2% | 47.6% | 48.6% | within noise | 0.2513 |
| Live, gradient boosting | 290 | **50.7%** | 44.9%–56.4% | 47.6% | 48.6% | no | 0.2496 |
| Live, ensemble | 290 | **52.4%** | 46.7%–58.2% | 47.6% | 48.6% | within noise | 0.2488 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 290 | **55.2%** | 49.4%–60.9% | 46.6% | 45.5% | within noise | 0.2513 |
| Live, gradient boosting | 290 | **54.1%** | 48.4%–59.9% | 46.6% | 45.5% | within noise | 0.2492 |
| Live, ensemble | 290 | **55.2%** | 49.4%–60.9% | 46.6% | 45.5% | within noise | 0.2486 |
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
| under 40% | 53.1% (n=256) | 50.5% (n=639) | 50.5% (n=641) | 54.9% (n=1,056) | 51.9% (n=480) |
| 40–45% | 51.5% (n=825) | 51.7% (n=1,134) | 51.6% (n=1,133) | 53.7% (n=1,063) | 52.2% (n=969) |
| 45–48% | 50.6% (n=1,322) | 50.4% (n=1,269) | 50.4% (n=1,275) | 50.9% (n=1,147) | 49.0% (n=1,240) |
| 48–50% | 52.3% (n=1,346) | 55.1% (n=1,166) | 55.1% (n=1,164) | 50.2% (n=1,022) | 51.3% (n=1,179) |
| 50–52% | 52.5% (n=1,735) | 51.1% (n=1,262) | 51.0% (n=1,262) | 47.4% (n=1,145) | 53.5% (n=1,427) |
| 52–55% | 52.0% (n=2,366) | 51.7% (n=1,776) | 51.8% (n=1,771) | 52.3% (n=1,629) | 52.6% (n=2,024) |
| 55–60% | 52.8% (n=2,137) | 52.4% (n=2,127) | 52.4% (n=2,126) | 52.6% (n=1,564) | 54.5% (n=1,911) |
| 60% or more | 52.2% (n=651) | 53.4% (n=1,265) | 53.3% (n=1,266) | 54.9% (n=1,422) | 50.0% (n=818) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=962) | 49.7% (n=768) | 51.2% (n=430) |
| 40–45% | 46.7% (n=1,538) | 49.7% (n=1,260) | 47.3% (n=1,313) |
| 45–48% | 50.6% (n=1,467) | 49.8% (n=1,619) | 48.0% (n=1,744) |
| 48–50% | 49.7% (n=1,170) | 49.6% (n=1,513) | 51.4% (n=1,554) |
| 50–52% | 50.0% (n=1,209) | 50.7% (n=1,589) | 51.0% (n=1,497) |
| 52–55% | 52.3% (n=1,558) | 52.3% (n=1,575) | 50.8% (n=1,810) |
| 55–60% | 51.9% (n=1,689) | 50.0% (n=1,105) | 53.9% (n=1,328) |
| 60% or more | 52.6% (n=1,045) | 51.1% (n=619) | 50.5% (n=372) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 248 | 48.4% | -0.1% | -0.2% | -0.040 |
| FinBERT | 196 | 47.4% | -0.1% | 0.3% | -0.107 |

The two scorers agree on the direction of the mood on 68% of 300 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 29 | 44.8% | 58.6% | 55.2% | 27.6% | 44.8% | 62.1% |
| AMZN | 29 | 58.6% | 58.6% | 58.6% | 51.7% | 51.7% | 51.7% |
| GOOGL | 29 | 62.1% | 55.2% | 55.2% | 69.0% | 75.9% | 44.8% |
| JPM | 29 | 48.3% | 37.9% | 44.8% | 34.5% | 31.0% | 37.9% |
| META | 29 | 44.8% | 55.2% | 51.7% | 62.1% | 58.6% | 37.9% |
| MSFT | 29 | 48.3% | 51.7% | 51.7% | 62.1% | 48.3% | 48.3% |
| NVDA | 29 | 51.7% | 55.2% | 55.2% | 58.6% | 55.2% | 27.6% |
| TSLA | 29 | 51.7% | 55.2% | 55.2% | 34.5% | 44.8% | 51.7% |
| UNH | 29 | 44.8% | 41.4% | 41.4% | 62.1% | 51.7% | 51.7% |
| XOM | 29 | 65.5% | 62.1% | 65.5% | 44.8% | 62.1% | 62.1% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 29 | 62.1% | 41.4% | 69.0% | 62.1% |
| AMZN | 29 | 48.3% | 62.1% | 48.3% | 51.7% |
| GOOGL | 29 | 55.2% | 65.5% | 51.7% | 44.8% |
| JPM | 29 | 44.8% | 58.6% | 44.8% | 44.8% |
| META | 29 | 58.6% | 34.5% | 51.7% | 34.5% |
| MSFT | 29 | 58.6% | 58.6% | 58.6% | 51.7% |
| NVDA | 29 | 51.7% | 48.3% | 51.7% | 31.0% |
| TSLA | 29 | 51.7% | 55.2% | 51.7% | 48.3% |
| UNH | 29 | 55.2% | 58.6% | 58.6% | 41.4% |
| XOM | 29 | 65.5% | 58.6% | 65.5% | 55.2% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,064 | +39.9% | +8.3% | 0.49 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,064 | +38.9% | +8.1% | 0.50 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,064 | +40.5% | +8.4% | 0.52 | 50.4% |
| Top 3 by gradient boosting | 1,005 | +68.7% | +14.0% | 0.78 | 36.7% |
| Top 3 by ensemble | 1,005 | +35.9% | +8.0% | 0.52 | 46.0% |
| Buy every stock, every session | 1,064 | -4.3% | -1.0% | 0.03 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,064 | -23.6% | -6.2% | -0.38 | 46.8% |
| Top 3 by gradient boosting | 1,005 | -43.4% | -13.3% | -0.82 | 39.0% |
| Top 3 by ensemble | 1,005 | -13.5% | -3.6% | -0.16 | 46.2% |
| Every stock minus SPY | 1,064 | -55.2% | -17.3% | -2.48 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7840 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 190 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 888 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 169 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-04 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-04 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-04 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-04 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-04 | 0 | 0 | 0 |
| META | ok | 2026-11-04 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-04 | 0 | 0 | 0 |
| JPM | ok | 2026-11-04 | 0 | 0 | 0 |
| XOM | ok | 2026-11-04 | 0 | 0 | 0 |
| UNH | ok | 2026-11-04 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
