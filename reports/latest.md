# Stock prediction lab: latest report

Generated 2026-10-21 00:38 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **51.0%** | Stay out | 47.8% | – | 36 | positive (+0.18) | positive (+0.06) |
| 2 | AAPL | **50.6%** | Stay out | 53.3% | **Outperform** | 41 | neutral (-0.04) | negative (-0.24) |
| 3 | JPM | **50.4%** | Stay out | 46.3% | – | 24 | positive (+0.17) | positive (+0.12) |
| 4 | GOOGL | **49.9%** | Stay out | 51.8% | – | 40 | positive (+0.15) | positive (+0.07) |
| 5 | TSLA | **48.7%** | Stay out | 46.1% | – | 38 | positive (+0.15) | positive (+0.07) |
| 6 | AMZN | **47.4%** | Stay out | 43.6% | – | 57 | positive (+0.25) | positive (+0.20) |
| 7 | META | **47.2%** | Stay out | 44.2% | – | 64 | positive (+0.09) | neutral (+0.00) |
| 8 | MSFT | **46.5%** | Stay out | 52.6% | **Outperform** | 31 | positive (+0.11) | positive (+0.14) |
| 9 | UNH | **46.4%** | Stay out | 35.4% | – | 13 | positive (+0.36) | positive (+0.07) |
| 10 | NVDA | **46.2%** | Stay out | 40.0% | – | 72 | positive (+0.12) | neutral (+0.03) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 49.1% | 55.8% | 53.4% | 53.3% | 45.4% | 48.6% | 50.6% | 51.0% |
| AMZN | 47.4% | 49.1% | 47.5% | 43.6% | 45.7% | 48.5% | 47.4% | 46.0% |
| GOOGL | 54.8% | 49.9% | 50.2% | 51.8% | 49.9% | 49.9% | 49.9% | 50.9% |
| JPM | 49.2% | 45.9% | 46.9% | 46.3% | 54.8% | 49.4% | 50.4% | 47.9% |
| META | 45.3% | 46.8% | 46.3% | 44.2% | 47.5% | 50.1% | 47.2% | 47.1% |
| MSFT | 47.0% | 42.6% | 41.3% | 52.6% | 50.4% | 50.0% | 46.5% | 51.3% |
| NVDA | 41.0% | 42.1% | 42.1% | 40.0% | 50.2% | 48.6% | 46.2% | 44.3% |
| TSLA | 53.9% | 53.0% | 52.6% | 46.1% | 44.3% | 46.9% | 48.7% | 46.5% |
| UNH | 39.7% | 45.4% | 43.9% | 35.4% | 47.4% | 46.8% | 46.4% | 41.1% |
| XOM | 47.6% | 49.7% | 50.5% | 47.8% | 52.3% | 49.6% | 51.0% | 48.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 180 | **52.8%** | 45.5%–60.1% | 50.0% | 47.8% | within noise | 0.2483 |
| Live, logistic, all sources (VADER) | 180 | **55.6%** | 48.3%–62.8% | 50.0% | 47.8% | within noise | 0.2483 |
| Live, logistic, all sources (FinBERT) | 180 | **56.7%** | 49.4%–63.9% | 50.0% | 47.8% | within noise | 0.2483 |
| Live, gradient boosting | 180 | **50.0%** | 42.7%–57.3% | 50.0% | 47.8% | no | 0.2492 |
| Live, ensemble | 180 | **53.9%** | 46.6%–61.2% | 50.0% | 47.8% | within noise | 0.2466 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 180 | **56.1%** | 48.9%–63.4% | 48.9% | 43.9% | within noise | 0.2485 |
| Live, gradient boosting | 180 | **58.9%** | 51.7%–66.1% | 48.9% | 43.9% | yes | 0.2479 |
| Live, ensemble | 180 | **55.6%** | 48.3%–62.8% | 48.9% | 43.9% | within noise | 0.2467 |
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
| under 40% | 53.2% (n=252) | 50.8% (n=632) | 50.9% (n=633) | 55.0% (n=1,049) | 52.1% (n=476) |
| 40–45% | 51.7% (n=811) | 51.7% (n=1,122) | 51.6% (n=1,123) | 54.1% (n=1,052) | 52.6% (n=960) |
| 45–48% | 50.8% (n=1,303) | 50.5% (n=1,253) | 50.5% (n=1,255) | 50.9% (n=1,133) | 48.9% (n=1,221) |
| 48–50% | 52.4% (n=1,329) | 55.2% (n=1,153) | 55.1% (n=1,153) | 50.2% (n=1,003) | 51.4% (n=1,164) |
| 50–52% | 52.5% (n=1,718) | 51.1% (n=1,252) | 51.2% (n=1,251) | 47.4% (n=1,127) | 53.6% (n=1,412) |
| 52–55% | 52.2% (n=2,343) | 51.9% (n=1,762) | 52.0% (n=1,757) | 52.4% (n=1,610) | 52.5% (n=2,002) |
| 55–60% | 52.7% (n=2,129) | 52.3% (n=2,107) | 52.3% (n=2,109) | 52.7% (n=1,542) | 54.7% (n=1,887) |
| 60% or more | 52.4% (n=643) | 53.5% (n=1,247) | 53.5% (n=1,247) | 54.9% (n=1,422) | 50.1% (n=816) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.5% (n=947) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.8% (n=1,514) | 49.7% (n=1,260) | 47.4% (n=1,297) |
| 45–48% | 50.8% (n=1,454) | 49.9% (n=1,604) | 48.2% (n=1,716) |
| 48–50% | 49.6% (n=1,162) | 49.7% (n=1,460) | 51.4% (n=1,540) |
| 50–52% | 49.9% (n=1,199) | 51.1% (n=1,548) | 50.9% (n=1,477) |
| 52–55% | 52.4% (n=1,544) | 52.3% (n=1,574) | 50.9% (n=1,798) |
| 55–60% | 51.9% (n=1,680) | 50.0% (n=1,105) | 54.0% (n=1,312) |
| 60% or more | 52.8% (n=1,028) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 159 | 47.8% | -0.1% | 0.5% | -0.055 |
| FinBERT | 121 | 49.6% | -0.1% | 0.4% | -0.100 |

The two scorers agree on the direction of the mood on 73% of 190 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,053 | 51.3% | 49.5% | 49.4% | 48.2% | 50.2% | 54.5% |
| AMZN | 1,053 | 49.7% | 50.0% | 50.1% | 49.2% | 49.0% | 50.8% |
| GOOGL | 1,053 | 51.6% | 49.5% | 49.5% | 51.3% | 52.4% | 54.3% |
| JPM | 1,053 | 50.5% | 50.5% | 50.7% | 50.8% | 50.8% | 53.8% |
| META | 1,053 | 52.8% | 52.8% | 52.8% | 49.1% | 51.2% | 50.5% |
| MSFT | 1,053 | 51.7% | 52.0% | 52.0% | 50.1% | 52.2% | 51.9% |
| NVDA | 1,053 | 49.6% | 50.0% | 50.0% | 51.7% | 51.9% | 52.6% |
| TSLA | 1,053 | 52.9% | 53.2% | 53.2% | 49.6% | 52.5% | 49.9% |
| UNH | 1,052 | 50.2% | 48.7% | 48.7% | 50.1% | 52.2% | 51.5% |
| XOM | 1,052 | 49.8% | 48.7% | 48.7% | 51.3% | 53.2% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,053 | 51.0% | 50.8% | 51.5% | 53.2% |
| AMZN | 1,053 | 49.3% | 52.7% | 50.8% | 48.0% |
| GOOGL | 1,053 | 50.0% | 51.7% | 50.6% | 53.5% |
| JPM | 1,053 | 52.5% | 49.3% | 49.8% | 53.4% |
| META | 1,053 | 51.4% | 48.1% | 50.1% | 48.8% |
| MSFT | 1,053 | 51.0% | 50.4% | 50.3% | 48.8% |
| NVDA | 1,053 | 52.0% | 52.6% | 52.9% | 52.0% |
| TSLA | 1,053 | 52.6% | 51.7% | 53.6% | 48.7% |
| UNH | 1,052 | 53.3% | 50.4% | 51.5% | 47.7% |
| XOM | 1,052 | 51.3% | 49.5% | 51.4% | 49.8% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,053 | +41.2% | +8.6% | 0.51 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,053 | +37.6% | +7.9% | 0.50 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,053 | +37.1% | +7.8% | 0.49 | 50.2% |
| Top 3 by gradient boosting | 994 | +67.9% | +14.0% | 0.78 | 36.8% |
| Top 3 by ensemble | 994 | +36.6% | +8.2% | 0.53 | 46.0% |
| Buy every stock, every session | 1,053 | -2.1% | -0.5% | 0.06 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,053 | -22.7% | -6.0% | -0.36 | 47.0% |
| Top 3 by gradient boosting | 994 | -42.9% | -13.2% | -0.81 | 39.4% |
| Top 3 by ensemble | 994 | -12.9% | -3.4% | -0.15 | 46.5% |
| Every stock minus SPY | 1,053 | -54.0% | -17.0% | -2.42 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7794 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 793 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 923 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 159 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-20 | 0 | 8 | 41 |
| MSFT | ok | 2026-10-20 | 0 | 8 | 31 |
| NVDA | ok | 2026-10-20 | 0 | 8 | 72 |
| AMZN | ok | 2026-10-20 | 0 | 8 | 57 |
| GOOGL | ok | 2026-10-20 | 0 | 8 | 40 |
| META | ok | 2026-10-20 | 0 | 8 | 64 |
| TSLA | ok | 2026-10-20 | 0 | 8 | 38 |
| JPM | ok | 2026-10-20 | 0 | 8 | 24 |
| XOM | ok | 2026-10-20 | 0 | 8 | 36 |
| UNH | ok | 2026-10-20 | 0 | 8 | 13 |

---

Educational project. Not financial advice.
