# Stock prediction lab: latest report

Generated 2026-10-23 06:03 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | TSLA | **66.8%** | **Buy at open** | 62.6% | **Outperform** | 53 | positive (+0.07) | negative (-0.07) |
| 2 | XOM | **61.9%** | **Buy at open** | 42.1% | – | 19 | positive (+0.07) | negative (-0.17) |
| 3 | META | **55.7%** | **Buy at open** | 63.9% | **Outperform** | 120 | positive (+0.06) | negative (-0.13) |
| 4 | AAPL | **54.7%** | Stay out | 49.7% | – | 33 | neutral (+0.03) | positive (+0.07) |
| 5 | JPM | **53.8%** | Stay out | 54.2% | – | 23 | positive (+0.10) | neutral (+0.01) |
| 6 | AMZN | **53.7%** | Stay out | 62.9% | **Outperform** | 43 | positive (+0.09) | neutral (+0.04) |
| 7 | MSFT | **46.3%** | Stay out | 50.2% | – | 29 | neutral (-0.00) | neutral (+0.03) |
| 8 | UNH | **45.3%** | Stay out | 36.1% | – | 8 | positive (+0.23) | positive (+0.21) |
| 9 | NVDA | **41.0%** | Stay out | 36.5% | – | 71 | positive (+0.13) | neutral (-0.01) |
| 10 | GOOGL | **38.7%** | Stay out | 38.3% | – | 36 | neutral (-0.02) | negative (-0.14) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 51.8% | 57.9% | 54.7% | 49.7% | 42.4% | 48.3% | 50.2% | 49.0% |
| AMZN | 53.4% | 56.1% | 53.7% | 62.9% | 55.3% | 50.3% | 55.7% | 56.6% |
| GOOGL | 49.8% | 41.2% | 38.7% | 38.3% | 49.1% | 50.3% | 45.2% | 44.3% |
| JPM | 53.2% | 53.8% | 53.8% | 54.2% | 55.1% | 50.8% | 54.4% | 52.5% |
| META | 49.0% | 56.5% | 55.7% | 63.9% | 51.2% | 48.4% | 53.9% | 56.1% |
| MSFT | 45.0% | 46.1% | 46.3% | 50.2% | 48.0% | 49.9% | 47.1% | 50.1% |
| NVDA | 39.7% | 41.1% | 41.0% | 36.5% | 50.2% | 48.4% | 45.7% | 42.5% |
| TSLA | 56.9% | 67.0% | 66.8% | 62.6% | 43.7% | 48.4% | 55.4% | 55.5% |
| UNH | 43.8% | 45.2% | 45.3% | 36.1% | 42.7% | 49.0% | 44.0% | 42.5% |
| XOM | 65.8% | 62.6% | 61.9% | 42.1% | 48.2% | 49.8% | 55.4% | 46.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 200 | **53.5%** | 46.6%–60.4% | 50.0% | 48.0% | within noise | 0.2479 |
| Live, logistic, all sources (VADER) | 200 | **56.5%** | 49.6%–63.4% | 50.0% | 48.0% | within noise | 0.2467 |
| Live, logistic, all sources (FinBERT) | 200 | **57.5%** | 50.6%–64.4% | 50.0% | 48.0% | yes | 0.2469 |
| Live, gradient boosting | 200 | **51.5%** | 44.6%–58.4% | 50.0% | 48.0% | within noise | 0.2496 |
| Live, ensemble | 200 | **54.5%** | 47.6%–61.4% | 50.0% | 48.0% | within noise | 0.2461 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 200 | **57.5%** | 50.6%–64.4% | 48.0% | 45.0% | within noise | 0.2459 |
| Live, gradient boosting | 200 | **58.5%** | 51.7%–65.3% | 48.0% | 45.0% | within noise | 0.2482 |
| Live, ensemble | 200 | **57.0%** | 50.1%–63.9% | 48.0% | 45.0% | within noise | 0.2456 |
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
| under 40% | 53.0% (n=253) | 50.7% (n=633) | 50.8% (n=634) | 55.0% (n=1,050) | 52.1% (n=476) |
| 40–45% | 51.7% (n=813) | 51.6% (n=1,127) | 51.6% (n=1,128) | 54.0% (n=1,055) | 52.4% (n=963) |
| 45–48% | 50.8% (n=1,311) | 50.5% (n=1,257) | 50.5% (n=1,260) | 50.9% (n=1,141) | 48.9% (n=1,228) |
| 48–50% | 52.3% (n=1,332) | 55.1% (n=1,158) | 55.1% (n=1,155) | 50.1% (n=1,006) | 51.4% (n=1,170) |
| 50–52% | 52.5% (n=1,720) | 51.1% (n=1,253) | 51.1% (n=1,254) | 47.5% (n=1,130) | 53.6% (n=1,415) |
| 52–55% | 52.2% (n=2,345) | 52.0% (n=1,763) | 52.1% (n=1,759) | 52.4% (n=1,612) | 52.6% (n=2,003) |
| 55–60% | 52.7% (n=2,131) | 52.4% (n=2,110) | 52.3% (n=2,111) | 52.7% (n=1,542) | 54.7% (n=1,887) |
| 60% or more | 52.4% (n=643) | 53.5% (n=1,247) | 53.5% (n=1,247) | 54.9% (n=1,422) | 50.1% (n=816) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.4 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.4% (n=951) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.7% (n=1,520) | 49.7% (n=1,260) | 47.2% (n=1,304) |
| 45–48% | 50.8% (n=1,458) | 49.9% (n=1,607) | 48.2% (n=1,721) |
| 48–50% | 49.6% (n=1,162) | 49.6% (n=1,476) | 51.4% (n=1,542) |
| 50–52% | 49.8% (n=1,200) | 51.1% (n=1,549) | 51.0% (n=1,483) |
| 52–55% | 52.5% (n=1,549) | 52.3% (n=1,574) | 50.9% (n=1,798) |
| 55–60% | 51.9% (n=1,680) | 50.0% (n=1,105) | 54.0% (n=1,312) |
| 60% or more | 52.8% (n=1,028) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 178 | 47.8% | -0.2% | 0.5% | -0.089 |
| FinBERT | 135 | 48.1% | -0.1% | 0.5% | -0.130 |

The two scorers agree on the direction of the mood on 70% of 210 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 20 | 50.0% | 60.0% | 55.0% | 20.0% | 40.0% | 65.0% |
| AMZN | 20 | 60.0% | 60.0% | 65.0% | 60.0% | 50.0% | 45.0% |
| GOOGL | 20 | 60.0% | 60.0% | 55.0% | 65.0% | 80.0% | 50.0% |
| JPM | 20 | 40.0% | 35.0% | 45.0% | 35.0% | 25.0% | 40.0% |
| META | 20 | 55.0% | 60.0% | 60.0% | 65.0% | 65.0% | 35.0% |
| MSFT | 20 | 45.0% | 50.0% | 50.0% | 65.0% | 50.0% | 50.0% |
| NVDA | 20 | 55.0% | 70.0% | 70.0% | 65.0% | 65.0% | 30.0% |
| TSLA | 20 | 45.0% | 55.0% | 55.0% | 35.0% | 40.0% | 55.0% |
| UNH | 20 | 50.0% | 45.0% | 45.0% | 65.0% | 55.0% | 60.0% |
| XOM | 20 | 75.0% | 70.0% | 75.0% | 40.0% | 75.0% | 70.0% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 20 | 60.0% | 35.0% | 65.0% | 65.0% |
| AMZN | 20 | 60.0% | 60.0% | 60.0% | 50.0% |
| GOOGL | 20 | 55.0% | 75.0% | 50.0% | 45.0% |
| JPM | 20 | 45.0% | 65.0% | 45.0% | 50.0% |
| META | 20 | 65.0% | 45.0% | 55.0% | 30.0% |
| MSFT | 20 | 60.0% | 65.0% | 60.0% | 50.0% |
| NVDA | 20 | 60.0% | 60.0% | 60.0% | 35.0% |
| TSLA | 20 | 55.0% | 55.0% | 55.0% | 45.0% |
| UNH | 20 | 45.0% | 60.0% | 50.0% | 50.0% |
| XOM | 20 | 70.0% | 65.0% | 70.0% | 60.0% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,055 | +42.3% | +8.8% | 0.51 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,055 | +40.1% | +8.4% | 0.52 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,055 | +39.6% | +8.3% | 0.51 | 50.3% |
| Top 3 by gradient boosting | 996 | +65.0% | +13.5% | 0.75 | 36.6% |
| Top 3 by ensemble | 996 | +37.9% | +8.5% | 0.54 | 46.0% |
| Buy every stock, every session | 1,055 | -3.0% | -0.7% | 0.05 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,055 | -22.3% | -5.8% | -0.35 | 47.0% |
| Top 3 by gradient boosting | 996 | -43.3% | -13.4% | -0.82 | 39.4% |
| Top 3 by ensemble | 996 | -13.0% | -3.5% | -0.15 | 46.4% |
| Every stock minus SPY | 1,055 | -54.4% | -17.1% | -2.44 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7835 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 225 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 984 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 167 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-22 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-22 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-22 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-22 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-22 | 0 | 0 | 0 |
| META | ok | 2026-10-22 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-22 | 0 | 0 | 0 |
| JPM | ok | 2026-10-22 | 0 | 0 | 0 |
| XOM | ok | 2026-10-22 | 0 | 0 | 0 |
| UNH | ok | 2026-10-22 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
