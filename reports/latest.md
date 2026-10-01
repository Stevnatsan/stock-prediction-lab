# Stock prediction lab: latest report

Generated 2026-10-01 01:18 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **53.9%** | **Buy at open** | 64.2% | **Outperform** | 16 | positive (+0.11) | positive (+0.09) |
| 2 | UNH | **52.9%** | **Buy at open** | 57.4% | **Outperform** | 17 | positive (+0.10) | neutral (-0.02) |
| 3 | AAPL | **49.3%** | Stay out | 54.7% | **Outperform** | 34 | neutral (+0.05) | neutral (-0.02) |
| 4 | AMZN | **49.2%** | Stay out | 52.1% | – | 42 | positive (+0.17) | positive (+0.09) |
| 5 | JPM | **47.0%** | Stay out | 54.2% | – | 22 | positive (+0.13) | positive (+0.23) |
| 6 | META | **44.3%** | Stay out | 49.5% | – | 70 | positive (+0.14) | positive (+0.08) |
| 7 | MSFT | **43.1%** | Stay out | 54.1% | – | 30 | positive (+0.17) | neutral (-0.03) |
| 8 | GOOGL | **42.9%** | Stay out | 50.0% | – | 43 | positive (+0.11) | positive (+0.14) |
| 9 | TSLA | **41.9%** | Stay out | 42.5% | – | 22 | neutral (-0.01) | neutral (-0.03) |
| 10 | NVDA | **41.3%** | Stay out | 41.9% | – | 65 | positive (+0.11) | positive (+0.07) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 54.7% | 54.9% | 53.8% | 54.7% | 43.7% | 49.0% | 49.3% | 51.8% |
| AMZN | 57.4% | 49.7% | 49.4% | 52.1% | 48.7% | 48.6% | 49.2% | 50.4% |
| GOOGL | 54.9% | 41.7% | 42.2% | 50.0% | 44.1% | 48.6% | 42.9% | 49.3% |
| JPM | 54.9% | 44.2% | 44.4% | 54.2% | 49.9% | 49.9% | 47.0% | 52.0% |
| META | 49.0% | 40.9% | 40.9% | 49.5% | 47.8% | 49.5% | 44.3% | 49.5% |
| MSFT | 51.8% | 40.9% | 40.3% | 54.1% | 45.3% | 49.7% | 43.1% | 51.9% |
| NVDA | 48.1% | 37.1% | 36.8% | 41.9% | 45.4% | 50.0% | 41.3% | 46.0% |
| TSLA | 46.2% | 39.1% | 39.7% | 42.5% | 44.8% | 49.7% | 41.9% | 46.1% |
| UNH | 55.5% | 56.0% | 55.7% | 57.4% | 49.9% | 49.9% | 52.9% | 53.6% |
| XOM | 57.8% | 63.4% | 62.9% | 64.2% | 44.5% | 49.3% | 53.9% | 56.8% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 40 | **47.5%** | 32.0%–63.0% | 47.5% | 57.5% | no | 0.2568 |
| Live, logistic, all sources (VADER) | 40 | **47.5%** | 32.0%–63.0% | 47.5% | 57.5% | no | 0.2625 |
| Live, logistic, all sources (FinBERT) | 40 | **47.5%** | 32.0%–63.0% | 47.5% | 57.5% | no | 0.2625 |
| Live, gradient boosting | 40 | **50.0%** | 34.5%–65.5% | 47.5% | 57.5% | no | 0.2500 |
| Live, ensemble | 40 | **55.0%** | 39.6%–70.4% | 47.5% | 57.5% | no | 0.2543 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 40 | **57.5%** | 42.2%–72.8% | 57.5% | 60.0% | no | 0.2486 |
| Live, gradient boosting | 40 | **57.5%** | 42.2%–72.8% | 57.5% | 60.0% | no | 0.2491 |
| Live, ensemble | 40 | **55.0%** | 39.6%–70.4% | 57.5% | 60.0% | no | 0.2476 |
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
| under 40% | 53.0% (n=247) | 50.7% (n=613) | 50.7% (n=613) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=793) | 52.1% (n=1,087) | 52.1% (n=1,087) | 54.5% (n=1,024) | 53.0% (n=930) |
| 45–48% | 50.8% (n=1,288) | 50.4% (n=1,240) | 50.4% (n=1,242) | 50.6% (n=1,103) | 48.9% (n=1,189) |
| 48–50% | 52.6% (n=1,310) | 55.5% (n=1,142) | 55.5% (n=1,140) | 50.3% (n=974) | 51.2% (n=1,144) |
| 50–52% | 52.6% (n=1,697) | 51.0% (n=1,241) | 51.0% (n=1,241) | 47.4% (n=1,102) | 53.8% (n=1,394) |
| 52–55% | 52.3% (n=2,307) | 51.9% (n=1,744) | 51.9% (n=1,744) | 52.5% (n=1,586) | 52.5% (n=1,981) |
| 55–60% | 52.5% (n=2,107) | 52.3% (n=2,088) | 52.3% (n=2,088) | 52.7% (n=1,538) | 54.6% (n=1,874) |
| 60% or more | 52.3% (n=639) | 53.2% (n=1,233) | 53.2% (n=1,233) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=929) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.0% (n=1,489) | 49.7% (n=1,260) | 47.6% (n=1,278) |
| 45–48% | 50.8% (n=1,435) | 50.1% (n=1,586) | 48.4% (n=1,684) |
| 48–50% | 49.7% (n=1,147) | 50.1% (n=1,398) | 51.4% (n=1,511) |
| 50–52% | 50.0% (n=1,187) | 50.8% (n=1,491) | 51.0% (n=1,456) |
| 52–55% | 52.3% (n=1,526) | 52.3% (n=1,571) | 50.9% (n=1,777) |
| 55–60% | 52.0% (n=1,663) | 50.0% (n=1,105) | 54.0% (n=1,295) |
| 60% or more | 52.8% (n=1,012) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 36 | 44.4% | -0.4% | – | -0.203 |
| FinBERT | 23 | 52.2% | -0.5% | 0.2% | -0.048 |

The two scorers agree on the direction of the mood on 66% of 50 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,039 | 51.3% | 49.4% | 49.4% | 48.7% | 50.5% | 54.4% |
| AMZN | 1,039 | 49.6% | 50.0% | 50.0% | 49.1% | 49.0% | 50.8% |
| GOOGL | 1,039 | 51.4% | 49.3% | 49.3% | 51.2% | 52.1% | 54.3% |
| JPM | 1,039 | 50.7% | 50.8% | 50.8% | 51.0% | 51.1% | 53.9% |
| META | 1,039 | 52.7% | 52.6% | 52.6% | 49.0% | 51.0% | 50.7% |
| MSFT | 1,039 | 51.8% | 51.9% | 51.9% | 49.7% | 52.0% | 52.1% |
| NVDA | 1,039 | 49.5% | 49.8% | 49.8% | 51.6% | 51.8% | 52.8% |
| TSLA | 1,039 | 53.0% | 53.2% | 53.2% | 49.8% | 52.7% | 49.8% |
| UNH | 1,038 | 50.1% | 48.6% | 48.6% | 49.8% | 52.1% | 51.4% |
| XOM | 1,038 | 49.4% | 48.4% | 48.4% | 51.4% | 52.9% | 51.9% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,039 | 51.0% | 51.0% | 51.4% | 53.0% |
| AMZN | 1,039 | 49.3% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,039 | 49.9% | 51.4% | 50.6% | 53.6% |
| JPM | 1,039 | 52.6% | 49.1% | 49.8% | 53.3% |
| META | 1,039 | 51.2% | 48.3% | 50.1% | 49.1% |
| MSFT | 1,039 | 50.9% | 50.2% | 50.2% | 49.0% |
| NVDA | 1,039 | 52.0% | 52.3% | 52.9% | 52.3% |
| TSLA | 1,039 | 52.6% | 51.3% | 53.6% | 48.8% |
| UNH | 1,038 | 53.4% | 50.3% | 51.4% | 47.7% |
| XOM | 1,038 | 51.2% | 49.4% | 51.2% | 49.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,039 | +35.2% | +7.6% | 0.46 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,039 | +31.0% | +6.8% | 0.44 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,039 | +31.0% | +6.8% | 0.44 | 50.0% |
| Top 3 by gradient boosting | 980 | +65.2% | +13.8% | 0.76 | 36.9% |
| Top 3 by ensemble | 980 | +33.0% | +7.6% | 0.49 | 45.7% |
| Buy every stock, every session | 1,039 | -0.9% | -0.2% | 0.08 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,039 | -24.4% | -6.5% | -0.41 | 46.8% |
| Top 3 by gradient boosting | 980 | -40.7% | -12.6% | -0.76 | 40.0% |
| Top 3 by ensemble | 980 | -15.7% | -4.3% | -0.20 | 46.2% |
| Every stock minus SPY | 1,039 | -53.1% | -16.8% | -2.38 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7678 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 355 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1002 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 169 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-30 | 0 | 8 | 34 |
| MSFT | ok | 2026-09-30 | 0 | 8 | 30 |
| NVDA | ok | 2026-09-30 | 0 | 8 | 65 |
| AMZN | ok | 2026-09-30 | 0 | 8 | 42 |
| GOOGL | ok | 2026-09-30 | 0 | 8 | 43 |
| META | ok | 2026-09-30 | 0 | 8 | 70 |
| TSLA | ok | 2026-09-30 | 0 | 8 | 22 |
| JPM | ok | 2026-09-30 | 0 | 8 | 22 |
| XOM | ok | 2026-09-30 | 0 | 8 | 16 |
| UNH | ok | 2026-09-30 | 0 | 8 | 17 |

---

Educational project. Not financial advice.
