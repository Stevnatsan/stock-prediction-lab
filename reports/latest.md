# Stock prediction lab: latest report

Generated 2026-10-15 05:55 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **57.5%** | **Buy at open** | 66.8% | **Outperform** | 27 | positive (+0.11) | positive (+0.22) |
| 2 | JPM | **53.2%** | **Buy at open** | 49.0% | – | 33 | positive (+0.14) | negative (-0.06) |
| 3 | AMZN | **52.5%** | **Buy at open** | 56.9% | **Outperform** | 37 | positive (+0.22) | neutral (+0.03) |
| 4 | GOOGL | **52.4%** | Stay out | 46.5% | – | 35 | positive (+0.13) | positive (+0.08) |
| 5 | AAPL | **50.2%** | Stay out | 51.7% | – | 42 | positive (+0.11) | neutral (+0.04) |
| 6 | NVDA | **46.8%** | Stay out | 44.1% | – | 77 | positive (+0.15) | neutral (-0.05) |
| 7 | TSLA | **46.0%** | Stay out | 39.8% | – | 31 | positive (+0.12) | positive (+0.08) |
| 8 | MSFT | **45.2%** | Stay out | 46.8% | – | 36 | positive (+0.16) | positive (+0.07) |
| 9 | UNH | **43.2%** | Stay out | 28.8% | – | 34 | positive (+0.24) | positive (+0.14) |
| 10 | META | **42.7%** | Stay out | 45.3% | – | 61 | positive (+0.12) | positive (+0.06) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 50.0% | 50.1% | 49.8% | 51.7% | 50.2% | 47.9% | 50.2% | 49.8% |
| AMZN | 52.6% | 54.6% | 54.6% | 56.9% | 50.4% | 49.4% | 52.5% | 53.2% |
| GOOGL | 57.0% | 54.5% | 54.8% | 46.5% | 50.2% | 49.5% | 52.4% | 48.0% |
| JPM | 52.6% | 53.3% | 52.2% | 49.0% | 53.1% | 48.9% | 53.2% | 48.9% |
| META | 42.0% | 35.9% | 35.9% | 45.3% | 49.4% | 49.3% | 42.7% | 47.3% |
| MSFT | 46.8% | 39.5% | 39.5% | 46.8% | 50.9% | 49.6% | 45.2% | 48.2% |
| NVDA | 45.4% | 43.6% | 43.6% | 44.1% | 50.0% | 48.3% | 46.8% | 46.2% |
| TSLA | 48.5% | 44.1% | 44.3% | 39.8% | 47.8% | 49.3% | 46.0% | 44.6% |
| UNH | 39.9% | 39.5% | 39.1% | 28.8% | 46.8% | 47.1% | 43.2% | 38.0% |
| XOM | 54.3% | 69.8% | 70.1% | 66.8% | 45.2% | 46.6% | 57.5% | 56.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 140 | **55.7%** | 47.5%–63.9% | 50.0% | 53.6% | within noise | 0.2463 |
| Live, logistic, all sources (VADER) | 140 | **58.6%** | 50.4%–66.7% | 50.0% | 53.6% | within noise | 0.2417 |
| Live, logistic, all sources (FinBERT) | 140 | **58.6%** | 50.4%–66.7% | 50.0% | 53.6% | within noise | 0.2423 |
| Live, gradient boosting | 140 | **50.7%** | 42.4%–59.0% | 50.0% | 53.6% | no | 0.2474 |
| Live, ensemble | 140 | **57.1%** | 48.9%–65.3% | 50.0% | 53.6% | within noise | 0.2428 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 140 | **60.0%** | 51.9%–68.1% | 49.3% | 48.6% | yes | 0.2434 |
| Live, gradient boosting | 140 | **58.6%** | 50.4%–66.7% | 49.3% | 48.6% | within noise | 0.2479 |
| Live, ensemble | 140 | **58.6%** | 50.4%–66.7% | 49.3% | 48.6% | within noise | 0.2442 |
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
| under 40% | 52.8% (n=248) | 50.6% (n=622) | 50.6% (n=624) | 55.0% (n=1,049) | 52.0% (n=475) |
| 40–45% | 51.8% (n=801) | 51.6% (n=1,115) | 51.6% (n=1,115) | 54.0% (n=1,046) | 52.6% (n=951) |
| 45–48% | 50.7% (n=1,301) | 50.5% (n=1,249) | 50.6% (n=1,252) | 50.9% (n=1,126) | 48.8% (n=1,212) |
| 48–50% | 52.3% (n=1,322) | 55.3% (n=1,150) | 55.3% (n=1,147) | 50.4% (n=997) | 51.4% (n=1,160) |
| 50–52% | 52.6% (n=1,712) | 51.2% (n=1,249) | 51.2% (n=1,249) | 47.4% (n=1,118) | 53.8% (n=1,406) |
| 52–55% | 52.2% (n=2,336) | 52.0% (n=1,757) | 52.0% (n=1,754) | 52.4% (n=1,600) | 52.6% (n=1,996) |
| 55–60% | 52.7% (n=2,128) | 52.4% (n=2,103) | 52.3% (n=2,104) | 52.7% (n=1,540) | 54.7% (n=1,884) |
| 60% or more | 52.3% (n=640) | 53.5% (n=1,243) | 53.5% (n=1,243) | 54.9% (n=1,422) | 50.1% (n=814) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.5% (n=939) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,504) | 49.7% (n=1,260) | 47.5% (n=1,289) |
| 45–48% | 50.7% (n=1,446) | 49.9% (n=1,599) | 48.2% (n=1,704) |
| 48–50% | 49.6% (n=1,160) | 49.9% (n=1,440) | 51.3% (n=1,532) |
| 50–52% | 50.0% (n=1,196) | 51.0% (n=1,533) | 51.1% (n=1,473) |
| 52–55% | 52.4% (n=1,541) | 52.3% (n=1,574) | 50.9% (n=1,794) |
| 55–60% | 51.9% (n=1,677) | 50.0% (n=1,105) | 54.1% (n=1,309) |
| 60% or more | 52.9% (n=1,025) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 124 | 46.0% | -0.2% | 0.5% | -0.046 |
| FinBERT | 93 | 47.3% | -0.1% | 0.7% | -0.065 |

The two scorers agree on the direction of the mood on 72% of 150 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,049 | 51.4% | 49.6% | 49.5% | 48.4% | 50.4% | 54.5% |
| AMZN | 1,049 | 49.6% | 50.0% | 50.0% | 49.1% | 48.9% | 50.8% |
| GOOGL | 1,049 | 51.5% | 49.4% | 49.4% | 51.1% | 52.2% | 54.3% |
| JPM | 1,049 | 50.6% | 50.6% | 50.7% | 50.9% | 51.0% | 53.9% |
| META | 1,049 | 52.9% | 52.8% | 52.8% | 49.2% | 51.2% | 50.5% |
| MSFT | 1,049 | 51.7% | 52.0% | 52.0% | 50.1% | 52.2% | 51.9% |
| NVDA | 1,049 | 49.6% | 50.0% | 50.0% | 51.7% | 51.9% | 52.6% |
| TSLA | 1,049 | 53.0% | 53.2% | 53.2% | 49.8% | 52.6% | 49.8% |
| UNH | 1,048 | 50.3% | 48.7% | 48.7% | 49.9% | 52.2% | 51.4% |
| XOM | 1,048 | 49.8% | 48.8% | 48.8% | 51.2% | 53.3% | 52.3% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,049 | 51.2% | 50.8% | 51.6% | 53.2% |
| AMZN | 1,049 | 49.2% | 52.8% | 50.7% | 48.0% |
| GOOGL | 1,049 | 50.0% | 51.6% | 50.6% | 53.5% |
| JPM | 1,049 | 52.5% | 49.1% | 49.8% | 53.4% |
| META | 1,049 | 51.4% | 48.2% | 50.1% | 48.9% |
| MSFT | 1,049 | 51.0% | 50.3% | 50.3% | 48.8% |
| NVDA | 1,049 | 52.0% | 52.6% | 52.9% | 52.0% |
| TSLA | 1,049 | 52.6% | 51.6% | 53.6% | 48.7% |
| UNH | 1,048 | 53.4% | 50.5% | 51.6% | 47.6% |
| XOM | 1,048 | 51.4% | 49.3% | 51.5% | 49.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,049 | +40.3% | +8.5% | 0.50 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,049 | +36.4% | +7.7% | 0.49 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,049 | +36.4% | +7.7% | 0.49 | 50.2% |
| Top 3 by gradient boosting | 990 | +68.9% | +14.3% | 0.79 | 36.9% |
| Top 3 by ensemble | 990 | +38.7% | +8.7% | 0.55 | 46.1% |
| Buy every stock, every session | 1,049 | -1.5% | -0.4% | 0.07 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,049 | -22.0% | -5.8% | -0.35 | 47.0% |
| Top 3 by gradient boosting | 990 | -43.3% | -13.5% | -0.83 | 39.6% |
| Top 3 by ensemble | 990 | -12.5% | -3.3% | -0.14 | 46.5% |
| Every stock minus SPY | 1,049 | -53.7% | -16.9% | -2.41 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7764 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 192 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 998 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 168 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-14 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-14 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-14 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-14 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-14 | 0 | 0 | 0 |
| META | ok | 2026-10-14 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-14 | 0 | 0 | 0 |
| JPM | ok | 2026-10-14 | 0 | 0 | 0 |
| XOM | ok | 2026-10-14 | 0 | 0 | 0 |
| UNH | ok | 2026-10-14 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
