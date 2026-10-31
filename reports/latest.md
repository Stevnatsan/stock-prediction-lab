# Stock prediction lab: latest report

Generated 2026-10-31 07:00 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **57.9%** | **Buy at open** | 66.9% | **Outperform** | 39 | neutral (-0.02) | negative (-0.21) |
| 2 | GOOGL | **50.8%** | Stay out | 71.8% | **Outperform** | 55 | negative (-0.13) | negative (-0.42) |
| 3 | UNH | **49.8%** | Stay out | 45.0% | – | 10 | positive (+0.17) | positive (+0.22) |
| 4 | JPM | **49.7%** | Stay out | 43.4% | – | 19 | positive (+0.21) | negative (-0.10) |
| 5 | AMZN | **47.5%** | Stay out | 48.3% | – | 94 | neutral (+0.03) | negative (-0.40) |
| 6 | NVDA | **47.2%** | Stay out | 41.8% | – | 68 | neutral (+0.02) | negative (-0.31) |
| 7 | XOM | **46.3%** | Stay out | 34.7% | – | 60 | positive (+0.23) | positive (+0.34) |
| 8 | TSLA | **45.0%** | Stay out | 45.0% | – | 20 | neutral (+0.04) | neutral (+0.00) |
| 9 | MSFT | **42.3%** | Stay out | 43.7% | – | 25 | positive (+0.13) | negative (-0.24) |
| 10 | AAPL | **41.3%** | Stay out | 50.3% | – | 33 | positive (+0.10) | negative (-0.09) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 45.1% | 48.5% | 49.6% | 50.3% | 34.1% | 47.3% | 41.3% | 48.8% |
| AMZN | 46.2% | 52.0% | 57.6% | 48.3% | 43.0% | 50.5% | 47.5% | 49.4% |
| GOOGL | 51.2% | 53.0% | 48.4% | 71.8% | 48.7% | 51.0% | 50.8% | 61.4% |
| JPM | 53.3% | 51.4% | 51.1% | 43.4% | 48.0% | 49.9% | 49.7% | 46.6% |
| META | 60.6% | 66.2% | 64.6% | 66.9% | 49.6% | 51.0% | 57.9% | 58.9% |
| MSFT | 42.0% | 40.0% | 43.7% | 43.7% | 44.6% | 49.9% | 42.3% | 46.8% |
| NVDA | 46.5% | 47.0% | 46.1% | 41.8% | 47.4% | 51.0% | 47.2% | 46.4% |
| TSLA | 43.4% | 47.6% | 48.8% | 45.0% | 42.5% | 49.6% | 45.0% | 47.3% |
| UNH | 53.2% | 52.6% | 51.8% | 45.0% | 47.0% | 50.0% | 49.8% | 47.5% |
| XOM | 42.3% | 47.5% | 47.4% | 34.7% | 45.1% | 47.8% | 46.3% | 41.2% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 260 | **52.3%** | 46.2%–58.4% | 48.1% | 46.9% | within noise | 0.2492 |
| Live, logistic, all sources (VADER) | 260 | **53.8%** | 47.8%–59.9% | 48.1% | 46.9% | within noise | 0.2516 |
| Live, logistic, all sources (FinBERT) | 260 | **53.8%** | 47.8%–59.9% | 48.1% | 46.9% | within noise | 0.2510 |
| Live, gradient boosting | 260 | **50.0%** | 43.9%–56.1% | 48.1% | 46.9% | no | 0.2508 |
| Live, ensemble | 260 | **52.7%** | 46.6%–58.8% | 48.1% | 46.9% | within noise | 0.2492 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 260 | **55.8%** | 49.7%–61.8% | 46.5% | 45.8% | within noise | 0.2500 |
| Live, gradient boosting | 260 | **54.6%** | 48.6%–60.7% | 46.5% | 45.8% | within noise | 0.2490 |
| Live, ensemble | 260 | **55.4%** | 49.3%–61.4% | 46.5% | 45.8% | within noise | 0.2478 |
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
| under 40% | 53.1% (n=256) | 50.5% (n=639) | 50.5% (n=641) | 55.0% (n=1,054) | 51.9% (n=480) |
| 40–45% | 51.7% (n=820) | 51.6% (n=1,129) | 51.6% (n=1,130) | 53.8% (n=1,060) | 52.4% (n=966) |
| 45–48% | 50.6% (n=1,316) | 50.5% (n=1,263) | 50.5% (n=1,268) | 51.0% (n=1,142) | 49.0% (n=1,233) |
| 48–50% | 52.3% (n=1,341) | 55.1% (n=1,164) | 55.2% (n=1,160) | 50.2% (n=1,014) | 51.3% (n=1,173) |
| 50–52% | 52.5% (n=1,733) | 51.2% (n=1,260) | 51.2% (n=1,259) | 47.5% (n=1,140) | 53.5% (n=1,425) |
| 52–55% | 52.0% (n=2,358) | 51.8% (n=1,770) | 51.8% (n=1,770) | 52.3% (n=1,624) | 52.6% (n=2,019) |
| 55–60% | 52.8% (n=2,136) | 52.4% (n=2,124) | 52.4% (n=2,119) | 52.6% (n=1,562) | 54.6% (n=1,904) |
| 60% or more | 52.5% (n=648) | 53.3% (n=1,259) | 53.3% (n=1,261) | 54.9% (n=1,422) | 50.0% (n=818) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=960) | 49.7% (n=768) | 51.2% (n=430) |
| 40–45% | 46.7% (n=1,529) | 49.7% (n=1,260) | 47.3% (n=1,311) |
| 45–48% | 50.7% (n=1,464) | 49.9% (n=1,613) | 48.0% (n=1,732) |
| 48–50% | 49.6% (n=1,169) | 49.6% (n=1,502) | 51.4% (n=1,552) |
| 50–52% | 49.9% (n=1,206) | 50.8% (n=1,576) | 50.9% (n=1,492) |
| 52–55% | 52.4% (n=1,553) | 52.3% (n=1,575) | 50.9% (n=1,806) |
| 55–60% | 51.9% (n=1,687) | 50.0% (n=1,105) | 53.9% (n=1,324) |
| 60% or more | 52.7% (n=1,040) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 226 | 47.8% | -0.1% | 0.0% | -0.054 |
| FinBERT | 175 | 47.4% | -0.1% | 0.4% | -0.115 |

The two scorers agree on the direction of the mood on 69% of 270 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 26 | 46.2% | 57.7% | 53.8% | 26.9% | 42.3% | 61.5% |
| AMZN | 26 | 57.7% | 53.8% | 53.8% | 53.8% | 50.0% | 46.2% |
| GOOGL | 26 | 69.2% | 61.5% | 57.7% | 69.2% | 84.6% | 46.2% |
| JPM | 26 | 46.2% | 38.5% | 46.2% | 34.6% | 26.9% | 38.5% |
| META | 26 | 46.2% | 57.7% | 53.8% | 61.5% | 61.5% | 38.5% |
| MSFT | 26 | 50.0% | 53.8% | 53.8% | 61.5% | 50.0% | 46.2% |
| NVDA | 26 | 46.2% | 53.8% | 53.8% | 57.7% | 53.8% | 30.8% |
| TSLA | 26 | 46.2% | 53.8% | 53.8% | 34.6% | 42.3% | 53.8% |
| UNH | 26 | 46.2% | 42.3% | 42.3% | 57.7% | 50.0% | 50.0% |
| XOM | 26 | 69.2% | 65.4% | 69.2% | 42.3% | 65.4% | 69.2% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 26 | 61.5% | 38.5% | 65.4% | 61.5% |
| AMZN | 26 | 50.0% | 57.7% | 50.0% | 50.0% |
| GOOGL | 26 | 57.7% | 73.1% | 53.8% | 46.2% |
| JPM | 26 | 46.2% | 61.5% | 46.2% | 42.3% |
| META | 26 | 61.5% | 34.6% | 53.8% | 34.6% |
| MSFT | 26 | 57.7% | 57.7% | 57.7% | 50.0% |
| NVDA | 26 | 50.0% | 50.0% | 50.0% | 34.6% |
| TSLA | 26 | 53.8% | 53.8% | 53.8% | 46.2% |
| UNH | 26 | 57.7% | 61.5% | 61.5% | 38.5% |
| XOM | 26 | 61.5% | 57.7% | 61.5% | 61.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,061 | +41.7% | +8.6% | 0.51 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,061 | +40.6% | +8.4% | 0.52 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,061 | +40.5% | +8.4% | 0.52 | 50.4% |
| Top 3 by gradient boosting | 1,002 | +64.8% | +13.4% | 0.75 | 36.7% |
| Top 3 by ensemble | 1,002 | +37.5% | +8.3% | 0.53 | 46.0% |
| Buy every stock, every session | 1,061 | -4.1% | -1.0% | 0.03 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,061 | -22.9% | -6.0% | -0.36 | 46.9% |
| Top 3 by gradient boosting | 1,002 | -43.4% | -13.3% | -0.82 | 39.1% |
| Top 3 by ensemble | 1,002 | -12.7% | -3.4% | -0.14 | 46.3% |
| Every stock minus SPY | 1,061 | -55.1% | -17.3% | -2.48 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7893 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 209 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 904 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 154 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-30 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-30 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-30 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-30 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-30 | 0 | 0 | 0 |
| META | ok | 2026-10-30 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-30 | 0 | 0 | 0 |
| JPM | ok | 2026-10-30 | 0 | 0 | 0 |
| XOM | ok | 2026-10-30 | 0 | 0 | 0 |
| UNH | ok | 2026-10-30 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
