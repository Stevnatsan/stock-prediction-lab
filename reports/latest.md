# Stock prediction lab: latest report

Generated 2026-10-17 05:36 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | TSLA | **62.6%** | **Buy at open** | 46.3% | – | 54 | positive (+0.08) | positive (+0.07) |
| 2 | GOOGL | **58.7%** | **Buy at open** | 53.6% | **Outperform** | 27 | positive (+0.09) | neutral (+0.01) |
| 3 | AMZN | **58.2%** | **Buy at open** | 57.7% | **Outperform** | 31 | positive (+0.21) | negative (-0.10) |
| 4 | XOM | **54.3%** | Stay out | 52.3% | **Outperform** | 29 | positive (+0.24) | positive (+0.46) |
| 5 | JPM | **50.5%** | Stay out | 46.8% | – | 23 | neutral (+0.03) | negative (-0.19) |
| 6 | UNH | **50.4%** | Stay out | 40.8% | – | 14 | positive (+0.08) | negative (-0.15) |
| 7 | AAPL | **41.5%** | Stay out | 44.7% | – | 36 | positive (+0.19) | positive (+0.17) |
| 8 | META | **40.3%** | Stay out | 51.6% | – | 47 | positive (+0.14) | positive (+0.07) |
| 9 | NVDA | **38.9%** | Stay out | 43.2% | – | 79 | positive (+0.11) | negative (-0.05) |
| 10 | MSFT | **29.9%** | Stay out | 34.3% | – | 42 | positive (+0.12) | neutral (+0.01) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 44.8% | 41.5% | 42.5% | 44.7% | 44.4% | 48.0% | 43.0% | 46.4% |
| AMZN | 53.6% | 58.2% | 58.9% | 57.7% | 54.6% | 51.3% | 56.4% | 54.5% |
| GOOGL | 54.3% | 58.7% | 58.1% | 53.6% | 52.8% | 50.7% | 55.7% | 52.2% |
| JPM | 51.0% | 50.5% | 49.3% | 46.8% | 59.3% | 49.4% | 54.9% | 48.1% |
| META | 40.9% | 40.3% | 40.9% | 51.6% | 51.0% | 50.9% | 45.6% | 51.2% |
| MSFT | 35.9% | 29.9% | 30.0% | 34.3% | 47.8% | 50.0% | 38.8% | 42.2% |
| NVDA | 37.4% | 38.9% | 39.3% | 43.2% | 47.5% | 49.3% | 43.2% | 46.2% |
| TSLA | 63.6% | 62.6% | 63.1% | 46.3% | 45.4% | 50.7% | 54.0% | 48.5% |
| UNH | 48.3% | 50.4% | 50.7% | 40.8% | 52.8% | 49.4% | 51.6% | 45.1% |
| XOM | 48.2% | 54.3% | 58.3% | 52.3% | 45.8% | 49.7% | 50.1% | 51.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 160 | **53.8%** | 46.0%–61.5% | 48.8% | 49.4% | within noise | 0.2465 |
| Live, logistic, all sources (VADER) | 160 | **58.1%** | 50.5%–65.8% | 48.8% | 49.4% | within noise | 0.2440 |
| Live, logistic, all sources (FinBERT) | 160 | **58.1%** | 50.5%–65.8% | 48.8% | 49.4% | within noise | 0.2445 |
| Live, gradient boosting | 160 | **50.0%** | 42.3%–57.7% | 48.8% | 49.4% | no | 0.2484 |
| Live, ensemble | 160 | **55.0%** | 47.3%–62.7% | 48.8% | 49.4% | within noise | 0.2443 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 160 | **58.1%** | 50.5%–65.8% | 49.4% | 45.0% | within noise | 0.2460 |
| Live, gradient boosting | 160 | **57.5%** | 49.8%–65.2% | 49.4% | 45.0% | within noise | 0.2479 |
| Live, ensemble | 160 | **57.5%** | 49.8%–65.2% | 49.4% | 45.0% | within noise | 0.2454 |
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
| under 40% | 53.0% (n=249) | 50.7% (n=627) | 50.8% (n=628) | 55.0% (n=1,049) | 52.0% (n=475) |
| 40–45% | 51.6% (n=806) | 51.6% (n=1,118) | 51.6% (n=1,119) | 54.0% (n=1,046) | 52.6% (n=955) |
| 45–48% | 50.8% (n=1,303) | 50.4% (n=1,251) | 50.5% (n=1,254) | 50.9% (n=1,129) | 48.9% (n=1,217) |
| 48–50% | 52.3% (n=1,324) | 55.2% (n=1,153) | 55.1% (n=1,150) | 50.2% (n=1,003) | 51.3% (n=1,161) |
| 50–52% | 52.5% (n=1,716) | 51.1% (n=1,250) | 51.1% (n=1,250) | 47.4% (n=1,126) | 53.6% (n=1,410) |
| 52–55% | 52.2% (n=2,340) | 52.0% (n=1,760) | 52.0% (n=1,757) | 52.3% (n=1,603) | 52.5% (n=2,000) |
| 55–60% | 52.7% (n=2,129) | 52.3% (n=2,104) | 52.3% (n=2,105) | 52.7% (n=1,540) | 54.7% (n=1,885) |
| 60% or more | 52.4% (n=641) | 53.5% (n=1,245) | 53.5% (n=1,245) | 54.9% (n=1,422) | 50.2% (n=815) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.4% (n=944) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.8% (n=1,507) | 49.7% (n=1,260) | 47.4% (n=1,292) |
| 45–48% | 50.8% (n=1,451) | 49.9% (n=1,602) | 48.2% (n=1,711) |
| 48–50% | 49.6% (n=1,162) | 49.9% (n=1,451) | 51.3% (n=1,537) |
| 50–52% | 50.0% (n=1,197) | 51.0% (n=1,539) | 51.1% (n=1,473) |
| 52–55% | 52.4% (n=1,541) | 52.3% (n=1,574) | 50.9% (n=1,796) |
| 55–60% | 51.9% (n=1,679) | 50.0% (n=1,105) | 54.1% (n=1,311) |
| 60% or more | 52.9% (n=1,027) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 141 | 46.1% | -0.2% | 0.5% | -0.028 |
| FinBERT | 106 | 50.0% | -0.1% | 0.4% | -0.056 |

The two scorers agree on the direction of the mood on 70% of 170 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,051 | 51.4% | 49.6% | 49.5% | 48.3% | 50.3% | 54.4% |
| AMZN | 1,051 | 49.6% | 50.0% | 50.0% | 49.1% | 48.9% | 50.8% |
| GOOGL | 1,051 | 51.6% | 49.5% | 49.5% | 51.2% | 52.3% | 54.3% |
| JPM | 1,051 | 50.5% | 50.6% | 50.7% | 50.8% | 50.9% | 53.8% |
| META | 1,051 | 52.8% | 52.8% | 52.8% | 49.1% | 51.2% | 50.5% |
| MSFT | 1,051 | 51.7% | 52.0% | 52.0% | 50.2% | 52.2% | 51.9% |
| NVDA | 1,051 | 49.6% | 50.0% | 50.0% | 51.7% | 51.9% | 52.6% |
| TSLA | 1,051 | 52.9% | 53.2% | 53.2% | 49.7% | 52.5% | 49.8% |
| UNH | 1,050 | 50.3% | 48.7% | 48.7% | 49.9% | 52.2% | 51.4% |
| XOM | 1,050 | 49.8% | 48.8% | 48.8% | 51.3% | 53.3% | 52.3% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,051 | 51.1% | 50.9% | 51.6% | 53.2% |
| AMZN | 1,051 | 49.2% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,051 | 50.0% | 51.6% | 50.6% | 53.5% |
| JPM | 1,051 | 52.5% | 49.2% | 49.8% | 53.4% |
| META | 1,051 | 51.4% | 48.1% | 50.1% | 48.9% |
| MSFT | 1,051 | 51.0% | 50.3% | 50.3% | 48.8% |
| NVDA | 1,051 | 52.0% | 52.5% | 52.8% | 52.1% |
| TSLA | 1,051 | 52.7% | 51.6% | 53.7% | 48.6% |
| UNH | 1,050 | 53.4% | 50.5% | 51.6% | 47.6% |
| XOM | 1,050 | 51.4% | 49.4% | 51.5% | 49.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,051 | +40.1% | +8.4% | 0.50 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,051 | +36.2% | +7.7% | 0.48 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,051 | +36.2% | +7.7% | 0.48 | 50.2% |
| Top 3 by gradient boosting | 992 | +68.9% | +14.2% | 0.77 | 36.9% |
| Top 3 by ensemble | 992 | +37.7% | +8.5% | 0.54 | 46.0% |
| Buy every stock, every session | 1,051 | -2.7% | -0.7% | 0.05 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,051 | -22.2% | -5.8% | -0.35 | 47.0% |
| Top 3 by gradient boosting | 992 | -43.3% | -13.4% | -0.83 | 39.5% |
| Top 3 by ensemble | 992 | -12.7% | -3.4% | -0.14 | 46.5% |
| Every stock minus SPY | 1,051 | -54.1% | -17.0% | -2.43 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7777 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 180 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1000 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 163 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-16 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-16 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-16 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-16 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-16 | 0 | 0 | 0 |
| META | ok | 2026-10-16 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-16 | 0 | 0 | 0 |
| JPM | ok | 2026-10-16 | 0 | 0 | 0 |
| XOM | ok | 2026-10-16 | 0 | 0 | 0 |
| UNH | ok | 2026-10-16 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
