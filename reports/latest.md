# Stock prediction lab: latest report

Generated 2026-10-20 06:00 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **72.5%** | **Buy at open** | 64.5% | **Outperform** | 24 | positive (+0.06) | positive (+0.19) |
| 2 | GOOGL | **56.3%** | **Buy at open** | 53.1% | **Outperform** | 27 | positive (+0.06) | positive (+0.14) |
| 3 | AMZN | **49.8%** | Stay out | 37.1% | – | 62 | positive (+0.29) | positive (+0.23) |
| 4 | AAPL | **48.4%** | Stay out | 51.8% | – | 39 | positive (+0.13) | neutral (+0.02) |
| 5 | TSLA | **47.7%** | Stay out | 40.5% | – | 37 | positive (+0.10) | positive (+0.06) |
| 6 | UNH | **44.8%** | Stay out | 35.7% | – | 21 | positive (+0.10) | positive (+0.07) |
| 7 | JPM | **42.6%** | Stay out | 47.2% | – | 30 | positive (+0.08) | positive (+0.07) |
| 8 | NVDA | **37.6%** | Stay out | 43.6% | – | 58 | neutral (+0.02) | neutral (+0.01) |
| 9 | META | **37.3%** | Stay out | 40.1% | – | 38 | positive (+0.14) | neutral (+0.02) |
| 10 | MSFT | **28.0%** | Stay out | 40.1% | – | 36 | positive (+0.10) | positive (+0.19) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 49.5% | 48.0% | 48.4% | 51.8% | 43.9% | 51.3% | 45.9% | 51.5% |
| AMZN | 48.1% | 52.8% | 49.8% | 37.1% | 43.1% | 50.8% | 47.9% | 43.9% |
| GOOGL | 52.5% | 55.4% | 56.3% | 53.1% | 43.2% | 49.6% | 49.3% | 51.4% |
| JPM | 51.6% | 42.1% | 42.6% | 47.2% | 57.0% | 51.7% | 49.5% | 49.5% |
| META | 42.9% | 36.7% | 37.3% | 40.1% | 53.4% | 49.7% | 45.1% | 44.9% |
| MSFT | 41.1% | 29.6% | 28.0% | 40.1% | 53.5% | 46.9% | 41.5% | 43.5% |
| NVDA | 38.3% | 36.3% | 37.6% | 43.6% | 44.6% | 48.6% | 40.4% | 46.1% |
| TSLA | 49.5% | 47.3% | 47.7% | 40.5% | 42.6% | 51.5% | 45.0% | 46.0% |
| UNH | 41.3% | 44.1% | 44.8% | 35.7% | 52.4% | 47.0% | 48.3% | 41.3% |
| XOM | 66.7% | 73.1% | 72.5% | 64.5% | 54.7% | 49.6% | 63.9% | 57.1% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 170 | **54.1%** | 46.6%–61.6% | 49.4% | 48.2% | within noise | 0.2458 |
| Live, logistic, all sources (VADER) | 170 | **58.2%** | 50.8%–65.6% | 49.4% | 48.2% | yes | 0.2440 |
| Live, logistic, all sources (FinBERT) | 170 | **58.8%** | 51.4%–66.2% | 49.4% | 48.2% | yes | 0.2446 |
| Live, gradient boosting | 170 | **50.0%** | 42.5%–57.5% | 49.4% | 48.2% | no | 0.2489 |
| Live, ensemble | 170 | **55.3%** | 47.8%–62.8% | 49.4% | 48.2% | within noise | 0.2445 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 170 | **57.1%** | 49.6%–64.5% | 50.0% | 43.5% | within noise | 0.2475 |
| Live, gradient boosting | 170 | **58.2%** | 50.8%–65.6% | 50.0% | 43.5% | yes | 0.2480 |
| Live, ensemble | 170 | **56.5%** | 49.0%–63.9% | 50.0% | 43.5% | within noise | 0.2462 |
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
| under 40% | 53.0% (n=251) | 50.7% (n=629) | 50.8% (n=630) | 55.0% (n=1,049) | 52.1% (n=476) |
| 40–45% | 51.6% (n=808) | 51.6% (n=1,120) | 51.6% (n=1,121) | 54.1% (n=1,047) | 52.6% (n=957) |
| 45–48% | 50.8% (n=1,303) | 50.4% (n=1,251) | 50.5% (n=1,254) | 50.9% (n=1,133) | 48.9% (n=1,218) |
| 48–50% | 52.3% (n=1,326) | 55.2% (n=1,153) | 55.1% (n=1,151) | 50.2% (n=1,003) | 51.3% (n=1,161) |
| 50–52% | 52.5% (n=1,717) | 51.1% (n=1,252) | 51.2% (n=1,251) | 47.4% (n=1,127) | 53.6% (n=1,412) |
| 52–55% | 52.2% (n=2,342) | 52.0% (n=1,761) | 52.0% (n=1,757) | 52.4% (n=1,606) | 52.5% (n=2,002) |
| 55–60% | 52.7% (n=2,129) | 52.4% (n=2,106) | 52.3% (n=2,108) | 52.7% (n=1,541) | 54.7% (n=1,887) |
| 60% or more | 52.5% (n=642) | 53.5% (n=1,246) | 53.5% (n=1,246) | 54.9% (n=1,422) | 50.2% (n=815) |
| **Average gap** | **4.0 pts** | **5.4 pts** | **5.4 pts** | **7.1 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.5% (n=945) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.9% (n=1,510) | 49.7% (n=1,260) | 47.5% (n=1,293) |
| 45–48% | 50.8% (n=1,453) | 49.9% (n=1,602) | 48.2% (n=1,714) |
| 48–50% | 49.6% (n=1,162) | 49.9% (n=1,456) | 51.3% (n=1,539) |
| 50–52% | 49.9% (n=1,198) | 51.1% (n=1,544) | 51.0% (n=1,475) |
| 52–55% | 52.4% (n=1,543) | 52.3% (n=1,574) | 50.9% (n=1,798) |
| 55–60% | 51.9% (n=1,680) | 50.0% (n=1,105) | 54.1% (n=1,311) |
| 60% or more | 52.9% (n=1,027) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 150 | 47.3% | -0.1% | 0.5% | -0.046 |
| FinBERT | 114 | 50.0% | -0.1% | 0.4% | -0.074 |

The two scorers agree on the direction of the mood on 72% of 180 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,052 | 51.3% | 49.5% | 49.4% | 48.2% | 50.3% | 54.5% |
| AMZN | 1,052 | 49.6% | 50.1% | 50.1% | 49.1% | 48.9% | 50.9% |
| GOOGL | 1,052 | 51.6% | 49.5% | 49.5% | 51.3% | 52.4% | 54.4% |
| JPM | 1,052 | 50.5% | 50.6% | 50.8% | 50.8% | 50.9% | 53.7% |
| META | 1,052 | 52.9% | 52.9% | 52.9% | 49.0% | 51.3% | 50.5% |
| MSFT | 1,052 | 51.6% | 52.0% | 52.0% | 50.2% | 52.2% | 51.9% |
| NVDA | 1,052 | 49.6% | 50.0% | 50.0% | 51.8% | 52.0% | 52.6% |
| TSLA | 1,052 | 52.9% | 53.2% | 53.2% | 49.6% | 52.6% | 49.8% |
| UNH | 1,051 | 50.2% | 48.7% | 48.7% | 50.0% | 52.2% | 51.5% |
| XOM | 1,051 | 49.9% | 48.7% | 48.7% | 51.3% | 53.2% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,052 | 51.0% | 50.9% | 51.6% | 53.2% |
| AMZN | 1,052 | 49.2% | 52.8% | 50.8% | 48.0% |
| GOOGL | 1,052 | 50.0% | 51.7% | 50.7% | 53.5% |
| JPM | 1,052 | 52.6% | 49.2% | 49.8% | 53.3% |
| META | 1,052 | 51.3% | 48.0% | 50.1% | 48.9% |
| MSFT | 1,052 | 51.0% | 50.4% | 50.3% | 48.9% |
| NVDA | 1,052 | 52.0% | 52.6% | 52.9% | 52.1% |
| TSLA | 1,052 | 52.7% | 51.7% | 53.7% | 48.7% |
| UNH | 1,051 | 53.4% | 50.4% | 51.5% | 47.7% |
| XOM | 1,051 | 51.4% | 49.5% | 51.4% | 49.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,052 | +42.8% | +8.9% | 0.52 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,052 | +38.8% | +8.2% | 0.51 | 50.3% |
| Top 3 by logistic, all sources (FinBERT) | 1,052 | +38.6% | +8.1% | 0.51 | 50.3% |
| Top 3 by gradient boosting | 993 | +68.0% | +14.1% | 0.78 | 36.8% |
| Top 3 by ensemble | 993 | +38.2% | +8.6% | 0.54 | 46.0% |
| Buy every stock, every session | 1,052 | -2.1% | -0.5% | 0.06 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,052 | -21.5% | -5.6% | -0.34 | 47.1% |
| Top 3 by gradient boosting | 993 | -42.9% | -13.3% | -0.81 | 39.5% |
| Top 3 by ensemble | 993 | -11.5% | -3.1% | -0.12 | 46.5% |
| Every stock minus SPY | 1,052 | -53.8% | -16.9% | -2.40 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7781 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 222 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1002 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 170 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-19 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-19 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-19 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-19 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-19 | 0 | 0 | 0 |
| META | ok | 2026-10-19 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-19 | 0 | 0 | 0 |
| JPM | ok | 2026-10-19 | 0 | 0 | 0 |
| XOM | ok | 2026-10-19 | 0 | 0 | 0 |
| UNH | ok | 2026-10-19 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
