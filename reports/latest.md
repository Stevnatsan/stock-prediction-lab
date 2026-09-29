# Stock prediction lab: latest report

Generated 2026-09-29 01:58 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | JPM | **52.6%** | **Buy at open** | 58.1% | **Outperform** | 20 | positive (+0.23) | negative (-0.25) |
| 2 | XOM | **51.3%** | Stay out | 54.2% | **Outperform** | 17 | positive (+0.18) | positive (+0.30) |
| 3 | AMZN | **51.2%** | Stay out | 51.0% | – | 37 | positive (+0.23) | negative (-0.06) |
| 4 | UNH | **50.2%** | Stay out | 44.0% | – | 9 | positive (+0.10) | positive (+0.05) |
| 5 | GOOGL | **49.1%** | Stay out | 49.1% | – | 25 | positive (+0.15) | neutral (+0.05) |
| 6 | AAPL | **47.7%** | Stay out | 49.5% | – | 22 | positive (+0.15) | neutral (+0.01) |
| 7 | TSLA | **47.0%** | Stay out | 47.2% | – | 34 | neutral (+0.02) | negative (-0.16) |
| 8 | NVDA | **43.0%** | Stay out | 37.3% | – | 96 | positive (+0.25) | positive (+0.13) |
| 9 | META | **41.1%** | Stay out | 45.5% | – | 75 | neutral (+0.04) | negative (-0.35) |
| 10 | MSFT | **40.6%** | Stay out | 53.1% | **Outperform** | 28 | positive (+0.09) | neutral (+0.01) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 48.7% | 45.7% | 46.0% | 49.5% | 49.7% | 50.4% | 47.7% | 50.0% |
| AMZN | 55.4% | 50.4% | 50.1% | 51.0% | 52.0% | 50.4% | 51.2% | 50.7% |
| GOOGL | 57.5% | 50.5% | 51.3% | 49.1% | 47.7% | 50.4% | 49.1% | 49.8% |
| JPM | 56.4% | 52.9% | 52.4% | 58.1% | 52.3% | 50.4% | 52.6% | 54.3% |
| META | 36.1% | 31.4% | 31.4% | 45.5% | 50.8% | 50.8% | 41.1% | 48.1% |
| MSFT | 46.8% | 34.6% | 34.2% | 53.1% | 46.6% | 51.3% | 40.6% | 52.2% |
| NVDA | 44.7% | 39.0% | 38.5% | 37.3% | 47.1% | 49.6% | 43.0% | 43.4% |
| TSLA | 53.2% | 47.3% | 47.1% | 47.2% | 46.6% | 50.2% | 47.0% | 48.7% |
| UNH | 51.3% | 49.1% | 48.6% | 44.0% | 51.2% | 50.4% | 50.2% | 47.2% |
| XOM | 53.6% | 55.9% | 56.9% | 54.2% | 46.6% | 50.3% | 51.3% | 52.2% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 20 | **50.0%** | 28.1%–71.9% | 50.0% | 55.0% | no | 0.2466 |
| Live, logistic, all sources (VADER) | 20 | **50.0%** | 28.1%–71.9% | 50.0% | 55.0% | no | 0.2620 |
| Live, logistic, all sources (FinBERT) | 20 | **50.0%** | 28.1%–71.9% | 50.0% | 55.0% | no | 0.2620 |
| Live, gradient boosting | 20 | **55.0%** | 33.2%–76.8% | 50.0% | 55.0% | no | 0.2455 |
| Live, ensemble | 20 | **60.0%** | 38.5%–81.5% | 50.0% | 55.0% | within noise | 0.2516 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 20 | **60.0%** | 38.5%–81.5% | 45.0% | 45.0% | within noise | 0.2408 |
| Live, gradient boosting | 20 | **65.0%** | 44.1%–85.9% | 45.0% | 45.0% | within noise | 0.2493 |
| Live, ensemble | 20 | **55.0%** | 33.2%–76.8% | 45.0% | 45.0% | no | 0.2436 |
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
| under 40% | 52.8% (n=246) | 50.7% (n=607) | 50.7% (n=607) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.9% (n=792) | 52.0% (n=1,085) | 52.0% (n=1,085) | 54.5% (n=1,024) | 53.0% (n=923) |
| 45–48% | 50.7% (n=1,285) | 50.5% (n=1,238) | 50.5% (n=1,238) | 50.6% (n=1,097) | 49.0% (n=1,186) |
| 48–50% | 52.6% (n=1,307) | 55.5% (n=1,138) | 55.5% (n=1,138) | 50.3% (n=968) | 51.3% (n=1,141) |
| 50–52% | 52.5% (n=1,694) | 51.1% (n=1,239) | 51.1% (n=1,239) | 47.4% (n=1,096) | 53.8% (n=1,390) |
| 52–55% | 52.3% (n=2,305) | 52.0% (n=1,742) | 52.0% (n=1,742) | 52.5% (n=1,584) | 52.6% (n=1,978) |
| 55–60% | 52.6% (n=2,100) | 52.3% (n=2,087) | 52.3% (n=2,087) | 52.7% (n=1,538) | 54.6% (n=1,874) |
| 60% or more | 52.3% (n=639) | 53.2% (n=1,232) | 53.2% (n=1,232) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.6 pts** | **5.6 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=927) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,486) | 49.7% (n=1,260) | 47.6% (n=1,276) |
| 45–48% | 50.8% (n=1,433) | 50.1% (n=1,586) | 48.3% (n=1,681) |
| 48–50% | 49.7% (n=1,145) | 50.0% (n=1,390) | 51.4% (n=1,507) |
| 50–52% | 49.9% (n=1,185) | 50.7% (n=1,479) | 50.9% (n=1,450) |
| 52–55% | 52.2% (n=1,520) | 52.3% (n=1,571) | 50.9% (n=1,773) |
| 55–60% | 52.0% (n=1,661) | 50.0% (n=1,105) | 53.9% (n=1,294) |
| 60% or more | 52.7% (n=1,011) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 18 | 44.4% | -0.6% | – | +0.098 |
| FinBERT | 11 | 54.5% | -0.4% | 0.2% | +0.227 |

The two scorers agree on the direction of the mood on 70% of 30 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,037 | 51.3% | 49.4% | 49.4% | 48.7% | 50.5% | 54.4% |
| AMZN | 1,037 | 49.6% | 50.0% | 50.0% | 49.1% | 49.1% | 50.8% |
| GOOGL | 1,037 | 51.5% | 49.3% | 49.3% | 51.2% | 52.0% | 54.4% |
| JPM | 1,037 | 50.8% | 50.8% | 50.8% | 51.1% | 51.2% | 54.0% |
| META | 1,037 | 52.7% | 52.7% | 52.7% | 48.9% | 51.0% | 50.7% |
| MSFT | 1,037 | 51.8% | 52.0% | 52.0% | 49.8% | 52.1% | 52.0% |
| NVDA | 1,037 | 49.4% | 49.7% | 49.7% | 51.5% | 51.7% | 52.9% |
| TSLA | 1,037 | 53.1% | 53.2% | 53.2% | 49.8% | 52.7% | 49.8% |
| UNH | 1,036 | 50.1% | 48.6% | 48.6% | 49.8% | 52.1% | 51.4% |
| XOM | 1,036 | 49.3% | 48.3% | 48.3% | 51.5% | 52.8% | 51.8% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,037 | 50.9% | 51.1% | 51.3% | 53.0% |
| AMZN | 1,037 | 49.2% | 52.7% | 50.6% | 47.9% |
| GOOGL | 1,037 | 49.9% | 51.4% | 50.6% | 53.5% |
| JPM | 1,037 | 52.7% | 49.1% | 49.9% | 53.4% |
| META | 1,037 | 51.3% | 48.3% | 50.2% | 49.0% |
| MSFT | 1,037 | 50.8% | 50.1% | 50.1% | 48.9% |
| NVDA | 1,037 | 52.0% | 52.4% | 52.9% | 52.3% |
| TSLA | 1,037 | 52.6% | 51.4% | 53.6% | 48.8% |
| UNH | 1,036 | 53.5% | 50.3% | 51.5% | 47.7% |
| XOM | 1,036 | 51.1% | 49.3% | 51.1% | 49.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,037 | +35.2% | +7.6% | 0.46 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,037 | +32.2% | +7.0% | 0.45 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,037 | +32.2% | +7.0% | 0.45 | 50.0% |
| Top 3 by gradient boosting | 978 | +68.4% | +14.4% | 0.79 | 37.1% |
| Top 3 by ensemble | 978 | +35.1% | +8.1% | 0.52 | 45.8% |
| Buy every stock, every session | 1,037 | -0.4% | -0.1% | 0.08 | 52.1% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,037 | -25.0% | -6.7% | -0.42 | 46.7% |
| Top 3 by gradient boosting | 978 | -40.7% | -12.6% | -0.76 | 40.1% |
| Top 3 by ensemble | 978 | -16.0% | -4.4% | -0.21 | 46.1% |
| Every stock minus SPY | 1,037 | -53.2% | -16.9% | -2.39 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7674 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 467 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 992 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 299 |  |
| yahoo_rss | 10 | 0 | 180 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-28 | 0 | 8 | 22 |
| MSFT | ok | 2026-09-28 | 0 | 8 | 28 |
| NVDA | ok | 2026-09-28 | 0 | 8 | 96 |
| AMZN | ok | 2026-09-28 | 0 | 8 | 37 |
| GOOGL | ok | 2026-09-28 | 0 | 8 | 25 |
| META | ok | 2026-09-28 | 0 | 8 | 75 |
| TSLA | ok | 2026-09-28 | 0 | 8 | 34 |
| JPM | ok | 2026-09-28 | 0 | 8 | 20 |
| XOM | ok | 2026-09-28 | 0 | 8 | 17 |
| UNH | ok | 2026-09-28 | 0 | 8 | 9 |

---

Educational project. Not financial advice.
