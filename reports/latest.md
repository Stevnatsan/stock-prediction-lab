# Stock prediction lab: latest report

Generated 2026-10-02 01:42 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **54.5%** | **Buy at open** | 65.4% | **Outperform** | 17 | positive (+0.14) | positive (+0.24) |
| 2 | AMZN | **51.7%** | Stay out | 52.5% | – | 49 | positive (+0.23) | positive (+0.08) |
| 3 | UNH | **51.6%** | Stay out | 49.6% | – | 4 | positive (+0.19) | negative (-0.17) |
| 4 | JPM | **51.3%** | Stay out | 57.9% | **Outperform** | 27 | positive (+0.09) | negative (-0.06) |
| 5 | GOOGL | **50.4%** | Stay out | 48.3% | – | 39 | positive (+0.21) | neutral (+0.04) |
| 6 | AAPL | **50.0%** | Stay out | 53.9% | **Outperform** | 34 | positive (+0.12) | negative (-0.06) |
| 7 | TSLA | **46.2%** | Stay out | 45.5% | – | 21 | positive (+0.15) | negative (-0.16) |
| 8 | META | **45.5%** | Stay out | 47.0% | – | 47 | positive (+0.14) | positive (+0.11) |
| 9 | MSFT | **45.0%** | Stay out | 48.7% | – | 29 | positive (+0.18) | neutral (+0.04) |
| 10 | NVDA | **42.9%** | Stay out | 41.5% | – | 67 | positive (+0.17) | positive (+0.07) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 50.6% | 50.5% | 50.5% | 53.9% | 49.4% | 50.9% | 50.0% | 52.4% |
| AMZN | 56.4% | 50.5% | 50.2% | 52.5% | 52.8% | 50.9% | 51.7% | 51.7% |
| GOOGL | 59.2% | 50.9% | 51.6% | 48.3% | 49.8% | 50.3% | 50.4% | 49.3% |
| JPM | 54.2% | 49.8% | 48.7% | 57.9% | 52.7% | 50.7% | 51.3% | 54.3% |
| META | 48.0% | 40.5% | 40.4% | 47.0% | 50.5% | 50.8% | 45.5% | 48.9% |
| MSFT | 51.6% | 40.5% | 40.2% | 48.7% | 49.6% | 51.2% | 45.0% | 50.0% |
| NVDA | 47.0% | 40.2% | 39.9% | 41.5% | 45.6% | 49.6% | 42.9% | 45.6% |
| TSLA | 48.4% | 42.8% | 41.5% | 45.5% | 49.6% | 50.8% | 46.2% | 48.1% |
| UNH | 54.1% | 51.1% | 50.7% | 49.6% | 52.1% | 51.7% | 51.6% | 50.7% |
| XOM | 51.8% | 59.1% | 59.1% | 65.4% | 49.9% | 50.9% | 54.5% | 58.1% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 50 | **48.0%** | 34.2%–61.8% | 46.0% | 56.0% | no | 0.2557 |
| Live, logistic, all sources (VADER) | 50 | **52.0%** | 38.2%–65.8% | 46.0% | 56.0% | no | 0.2553 |
| Live, logistic, all sources (FinBERT) | 50 | **52.0%** | 38.2%–65.8% | 46.0% | 56.0% | no | 0.2555 |
| Live, gradient boosting | 50 | **52.0%** | 38.2%–65.8% | 46.0% | 56.0% | no | 0.2497 |
| Live, ensemble | 50 | **56.0%** | 42.2%–69.8% | 46.0% | 56.0% | no | 0.2506 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 50 | **58.0%** | 44.3%–71.7% | 54.0% | 56.0% | within noise | 0.2479 |
| Live, gradient boosting | 50 | **60.0%** | 46.4%–73.6% | 54.0% | 56.0% | within noise | 0.2489 |
| Live, ensemble | 50 | **56.0%** | 42.2%–69.8% | 54.0% | 56.0% | no | 0.2471 |
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
| under 40% | 53.0% (n=247) | 50.7% (n=615) | 50.7% (n=615) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=793) | 52.0% (n=1,091) | 52.0% (n=1,091) | 54.5% (n=1,028) | 52.8% (n=935) |
| 45–48% | 50.7% (n=1,289) | 50.4% (n=1,240) | 50.4% (n=1,242) | 50.5% (n=1,106) | 49.0% (n=1,190) |
| 48–50% | 52.6% (n=1,312) | 55.5% (n=1,143) | 55.5% (n=1,141) | 50.3% (n=977) | 51.2% (n=1,146) |
| 50–52% | 52.5% (n=1,698) | 51.0% (n=1,241) | 51.0% (n=1,241) | 47.4% (n=1,102) | 53.8% (n=1,394) |
| 52–55% | 52.3% (n=2,310) | 52.0% (n=1,745) | 52.0% (n=1,745) | 52.5% (n=1,586) | 52.5% (n=1,983) |
| 55–60% | 52.5% (n=2,110) | 52.3% (n=2,089) | 52.3% (n=2,089) | 52.7% (n=1,538) | 54.6% (n=1,874) |
| 60% or more | 52.3% (n=639) | 53.2% (n=1,234) | 53.2% (n=1,234) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=929) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.0% (n=1,491) | 49.7% (n=1,260) | 47.6% (n=1,278) |
| 45–48% | 50.8% (n=1,435) | 50.1% (n=1,586) | 48.4% (n=1,686) |
| 48–50% | 49.6% (n=1,149) | 50.0% (n=1,407) | 51.4% (n=1,513) |
| 50–52% | 50.0% (n=1,187) | 50.9% (n=1,492) | 51.0% (n=1,459) |
| 52–55% | 52.3% (n=1,530) | 52.3% (n=1,571) | 50.9% (n=1,779) |
| 55–60% | 51.9% (n=1,664) | 50.0% (n=1,105) | 54.0% (n=1,296) |
| 60% or more | 52.8% (n=1,013) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 44 | 43.2% | -0.5% | – | -0.181 |
| FinBERT | 29 | 51.7% | -0.4% | 0.2% | -0.020 |

The two scorers agree on the direction of the mood on 65% of 60 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,040 | 51.3% | 49.4% | 49.4% | 48.6% | 50.5% | 54.4% |
| AMZN | 1,040 | 49.5% | 50.0% | 50.0% | 49.1% | 49.0% | 50.8% |
| GOOGL | 1,040 | 51.3% | 49.3% | 49.3% | 51.3% | 52.2% | 54.2% |
| JPM | 1,040 | 50.8% | 50.8% | 50.8% | 51.0% | 51.1% | 53.9% |
| META | 1,040 | 52.8% | 52.7% | 52.7% | 49.0% | 51.1% | 50.7% |
| MSFT | 1,040 | 51.7% | 51.9% | 51.9% | 49.7% | 52.1% | 52.0% |
| NVDA | 1,040 | 49.4% | 49.7% | 49.7% | 51.6% | 51.8% | 52.9% |
| TSLA | 1,040 | 53.1% | 53.3% | 53.3% | 49.8% | 52.7% | 49.7% |
| UNH | 1,039 | 50.0% | 48.5% | 48.5% | 49.9% | 52.0% | 51.4% |
| XOM | 1,039 | 49.5% | 48.4% | 48.4% | 51.3% | 53.0% | 52.0% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,040 | 51.1% | 51.0% | 51.5% | 53.1% |
| AMZN | 1,040 | 49.2% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,040 | 49.9% | 51.5% | 50.7% | 53.6% |
| JPM | 1,040 | 52.6% | 49.0% | 49.8% | 53.4% |
| META | 1,040 | 51.2% | 48.3% | 50.2% | 49.0% |
| MSFT | 1,040 | 50.9% | 50.3% | 50.2% | 48.9% |
| NVDA | 1,040 | 51.9% | 52.4% | 52.8% | 52.3% |
| TSLA | 1,040 | 52.6% | 51.4% | 53.6% | 48.8% |
| UNH | 1,039 | 53.3% | 50.3% | 51.3% | 47.6% |
| XOM | 1,039 | 51.2% | 49.4% | 51.2% | 49.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,040 | +34.8% | +7.5% | 0.45 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,040 | +31.3% | +6.8% | 0.44 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,040 | +31.3% | +6.8% | 0.44 | 50.0% |
| Top 3 by gradient boosting | 981 | +67.1% | +14.1% | 0.77 | 36.9% |
| Top 3 by ensemble | 981 | +33.4% | +7.7% | 0.50 | 45.8% |
| Buy every stock, every session | 1,040 | -1.5% | -0.4% | 0.07 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,040 | -24.2% | -6.5% | -0.40 | 46.8% |
| Top 3 by gradient boosting | 981 | -41.1% | -12.7% | -0.77 | 40.0% |
| Top 3 by ensemble | 981 | -15.2% | -4.1% | -0.19 | 46.3% |
| Every stock minus SPY | 1,040 | -53.4% | -16.9% | -2.40 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7671 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 328 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 997 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 176 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-01 | 0 | 8 | 34 |
| MSFT | ok | 2026-10-01 | 0 | 8 | 29 |
| NVDA | ok | 2026-10-01 | 0 | 8 | 67 |
| AMZN | ok | 2026-10-01 | 0 | 8 | 49 |
| GOOGL | ok | 2026-10-01 | 0 | 8 | 39 |
| META | ok | 2026-10-01 | 0 | 8 | 47 |
| TSLA | ok | 2026-10-01 | 0 | 8 | 21 |
| JPM | ok | 2026-10-01 | 0 | 8 | 27 |
| XOM | ok | 2026-10-01 | 0 | 8 | 17 |
| UNH | ok | 2026-10-01 | 0 | 8 | 4 |

---

Educational project. Not financial advice.
