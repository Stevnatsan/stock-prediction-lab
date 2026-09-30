# Stock prediction lab: latest report

Generated 2026-09-30 06:43 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **54.9%** | **Buy at open** | 68.1% | **Outperform** | 23 | positive (+0.10) | neutral (+0.04) |
| 2 | UNH | **52.4%** | **Buy at open** | 52.4% | – | 13 | positive (+0.10) | neutral (-0.01) |
| 3 | JPM | **50.5%** | Stay out | 58.4% | **Outperform** | 29 | positive (+0.19) | positive (+0.09) |
| 4 | AMZN | **50.0%** | Stay out | 53.3% | **Outperform** | 37 | positive (+0.12) | neutral (-0.04) |
| 5 | GOOGL | **49.5%** | Stay out | 52.5% | – | 35 | positive (+0.07) | negative (-0.14) |
| 6 | AAPL | **46.9%** | Stay out | 51.3% | – | 42 | positive (+0.08) | negative (-0.20) |
| 7 | NVDA | **44.7%** | Stay out | 41.5% | – | 81 | positive (+0.21) | positive (+0.14) |
| 8 | TSLA | **44.6%** | Stay out | 44.2% | – | 30 | positive (+0.07) | negative (-0.08) |
| 9 | META | **44.2%** | Stay out | 39.3% | – | 62 | positive (+0.09) | neutral (+0.01) |
| 10 | MSFT | **42.6%** | Stay out | 52.7% | – | 29 | positive (+0.13) | neutral (+0.03) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 46.7% | 44.9% | 44.5% | 51.3% | 48.9% | 49.9% | 46.9% | 50.6% |
| AMZN | 57.5% | 48.2% | 47.6% | 53.3% | 51.7% | 49.3% | 50.0% | 51.3% |
| GOOGL | 58.6% | 48.9% | 48.0% | 52.5% | 50.2% | 49.5% | 49.5% | 51.0% |
| JPM | 56.7% | 48.2% | 48.3% | 58.4% | 52.8% | 49.9% | 50.5% | 54.1% |
| META | 45.2% | 38.4% | 38.3% | 39.3% | 49.9% | 49.5% | 44.2% | 44.4% |
| MSFT | 50.9% | 37.2% | 37.1% | 52.7% | 48.0% | 50.8% | 42.6% | 51.7% |
| NVDA | 48.7% | 39.8% | 39.6% | 41.5% | 49.6% | 49.9% | 44.7% | 45.7% |
| TSLA | 48.3% | 40.9% | 40.8% | 44.2% | 48.4% | 49.9% | 44.6% | 47.0% |
| UNH | 51.8% | 53.7% | 53.3% | 52.4% | 51.2% | 50.0% | 52.4% | 51.2% |
| XOM | 58.5% | 61.2% | 60.7% | 68.1% | 48.7% | 50.4% | 54.9% | 59.2% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 30 | **46.7%** | 28.8%–64.5% | 46.7% | 60.0% | no | 0.2583 |
| Live, logistic, all sources (VADER) | 30 | **46.7%** | 28.8%–64.5% | 46.7% | 60.0% | no | 0.2656 |
| Live, logistic, all sources (FinBERT) | 30 | **46.7%** | 28.8%–64.5% | 46.7% | 60.0% | no | 0.2655 |
| Live, gradient boosting | 30 | **56.7%** | 38.9%–74.4% | 46.7% | 60.0% | no | 0.2472 |
| Live, ensemble | 30 | **60.0%** | 42.5%–77.5% | 46.7% | 60.0% | no | 0.2544 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 30 | **60.0%** | 42.5%–77.5% | 50.0% | 60.0% | no | 0.2433 |
| Live, gradient boosting | 30 | **66.7%** | 49.8%–83.5% | 50.0% | 60.0% | within noise | 0.2485 |
| Live, ensemble | 30 | **56.7%** | 38.9%–74.4% | 50.0% | 60.0% | no | 0.2448 |
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
| under 40% | 53.0% (n=247) | 50.8% (n=610) | 50.8% (n=610) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=793) | 52.0% (n=1,085) | 52.0% (n=1,085) | 54.5% (n=1,024) | 53.0% (n=926) |
| 45–48% | 50.8% (n=1,286) | 50.4% (n=1,240) | 50.4% (n=1,240) | 50.5% (n=1,102) | 48.9% (n=1,188) |
| 48–50% | 52.6% (n=1,308) | 55.6% (n=1,139) | 55.6% (n=1,139) | 50.3% (n=969) | 51.2% (n=1,142) |
| 50–52% | 52.6% (n=1,695) | 51.0% (n=1,241) | 51.0% (n=1,241) | 47.4% (n=1,099) | 53.8% (n=1,393) |
| 52–55% | 52.3% (n=2,307) | 52.0% (n=1,743) | 52.0% (n=1,743) | 52.5% (n=1,585) | 52.6% (n=1,979) |
| 55–60% | 52.5% (n=2,103) | 52.3% (n=2,088) | 52.3% (n=2,088) | 52.7% (n=1,538) | 54.6% (n=1,874) |
| 60% or more | 52.3% (n=639) | 53.2% (n=1,232) | 53.2% (n=1,232) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=928) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,487) | 49.7% (n=1,260) | 47.5% (n=1,277) |
| 45–48% | 50.8% (n=1,435) | 50.1% (n=1,586) | 48.3% (n=1,682) |
| 48–50% | 49.7% (n=1,147) | 50.0% (n=1,391) | 51.4% (n=1,511) |
| 50–52% | 49.9% (n=1,186) | 50.8% (n=1,488) | 50.9% (n=1,451) |
| 52–55% | 52.2% (n=1,522) | 52.3% (n=1,571) | 50.9% (n=1,776) |
| 55–60% | 52.0% (n=1,662) | 50.0% (n=1,105) | 53.9% (n=1,294) |
| 60% or more | 52.7% (n=1,011) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 26 | 42.3% | -0.6% | – | -0.058 |
| FinBERT | 18 | 61.1% | -0.4% | 0.0% | +0.158 |

The two scorers agree on the direction of the mood on 65% of 40 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,038 | 51.3% | 49.4% | 49.4% | 48.7% | 50.6% | 54.3% |
| AMZN | 1,038 | 49.5% | 50.0% | 50.0% | 49.0% | 49.0% | 50.8% |
| GOOGL | 1,038 | 51.4% | 49.2% | 49.2% | 51.3% | 52.1% | 54.3% |
| JPM | 1,038 | 50.8% | 50.8% | 50.8% | 51.1% | 51.2% | 53.9% |
| META | 1,038 | 52.7% | 52.6% | 52.6% | 48.9% | 51.0% | 50.8% |
| MSFT | 1,038 | 51.7% | 51.9% | 51.9% | 49.7% | 52.1% | 52.0% |
| NVDA | 1,038 | 49.4% | 49.7% | 49.7% | 51.6% | 51.8% | 52.9% |
| TSLA | 1,038 | 53.1% | 53.3% | 53.3% | 49.8% | 52.7% | 49.7% |
| UNH | 1,037 | 50.1% | 48.6% | 48.6% | 49.9% | 52.1% | 51.5% |
| XOM | 1,037 | 49.4% | 48.3% | 48.3% | 51.4% | 52.9% | 51.9% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,038 | 51.0% | 51.1% | 51.4% | 53.0% |
| AMZN | 1,038 | 49.2% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,038 | 49.8% | 51.5% | 50.6% | 53.6% |
| JPM | 1,038 | 52.6% | 49.0% | 49.8% | 53.4% |
| META | 1,038 | 51.3% | 48.3% | 50.2% | 49.0% |
| MSFT | 1,038 | 50.9% | 50.2% | 50.2% | 48.9% |
| NVDA | 1,038 | 52.0% | 52.4% | 52.9% | 52.2% |
| TSLA | 1,038 | 52.6% | 51.4% | 53.6% | 48.7% |
| UNH | 1,037 | 53.4% | 50.3% | 51.4% | 47.7% |
| XOM | 1,037 | 51.1% | 49.4% | 51.1% | 49.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,038 | +34.6% | +7.5% | 0.45 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,038 | +32.2% | +7.0% | 0.45 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,038 | +32.2% | +7.0% | 0.45 | 50.0% |
| Top 3 by gradient boosting | 979 | +73.0% | +15.2% | 0.82 | 37.1% |
| Top 3 by ensemble | 979 | +34.2% | +7.9% | 0.51 | 45.8% |
| Buy every stock, every session | 1,038 | -0.8% | -0.2% | 0.08 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,038 | -24.7% | -6.7% | -0.42 | 46.7% |
| Top 3 by gradient boosting | 979 | -41.1% | -12.7% | -0.77 | 40.0% |
| Top 3 by ensemble | 979 | -15.7% | -4.3% | -0.20 | 46.2% |
| Every stock minus SPY | 1,038 | -53.3% | -16.9% | -2.39 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7676 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 100 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 992 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 181 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-29 | 0 | 0 | 0 |
| MSFT | ok | 2026-09-29 | 0 | 0 | 0 |
| NVDA | ok | 2026-09-29 | 0 | 0 | 0 |
| AMZN | ok | 2026-09-29 | 0 | 0 | 0 |
| GOOGL | ok | 2026-09-29 | 0 | 0 | 0 |
| META | ok | 2026-09-29 | 0 | 0 | 0 |
| TSLA | ok | 2026-09-29 | 0 | 0 | 0 |
| JPM | ok | 2026-09-29 | 0 | 0 | 0 |
| XOM | ok | 2026-09-29 | 0 | 0 | 0 |
| UNH | ok | 2026-09-29 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
