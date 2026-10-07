# Stock prediction lab: latest report

Generated 2026-10-07 07:14 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **56.1%** | **Buy at open** | 65.7% | **Outperform** | 8 | positive (+0.11) | neutral (-0.02) |
| 2 | AAPL | **49.0%** | Stay out | 56.4% | **Outperform** | 23 | positive (+0.19) | neutral (+0.03) |
| 3 | GOOGL | **48.6%** | Stay out | 51.9% | – | 25 | positive (+0.21) | positive (+0.19) |
| 4 | AMZN | **48.1%** | Stay out | 50.6% | – | 23 | positive (+0.14) | positive (+0.09) |
| 5 | JPM | **46.4%** | Stay out | 51.8% | – | 20 | positive (+0.13) | positive (+0.23) |
| 6 | UNH | **46.2%** | Stay out | 43.1% | – | 6 | positive (+0.29) | positive (+0.25) |
| 7 | META | **45.4%** | Stay out | 48.0% | – | 22 | positive (+0.15) | positive (+0.22) |
| 8 | NVDA | **43.2%** | Stay out | 45.2% | – | 45 | positive (+0.16) | positive (+0.11) |
| 9 | MSFT | **43.1%** | Stay out | 49.0% | – | 27 | positive (+0.22) | neutral (-0.01) |
| 10 | TSLA | **42.0%** | Stay out | 44.5% | – | 23 | positive (+0.19) | positive (+0.13) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 54.8% | 55.4% | 56.2% | 56.4% | 42.6% | 49.6% | 49.0% | 53.0% |
| AMZN | 55.0% | 53.2% | 53.3% | 50.6% | 43.0% | 48.6% | 48.1% | 49.6% |
| GOOGL | 55.1% | 54.1% | 55.1% | 51.9% | 43.2% | 47.3% | 48.6% | 49.6% |
| JPM | 50.5% | 47.2% | 47.9% | 51.8% | 45.6% | 50.2% | 46.4% | 51.0% |
| META | 49.8% | 43.4% | 42.9% | 48.0% | 47.4% | 52.4% | 45.4% | 50.2% |
| MSFT | 54.3% | 44.2% | 44.5% | 49.0% | 42.0% | 48.5% | 43.1% | 48.7% |
| NVDA | 50.1% | 43.0% | 42.6% | 45.2% | 43.4% | 47.8% | 43.2% | 46.5% |
| TSLA | 44.5% | 41.2% | 40.1% | 44.5% | 42.8% | 45.6% | 42.0% | 45.1% |
| UNH | 50.4% | 47.1% | 47.7% | 43.1% | 45.3% | 50.2% | 46.2% | 46.6% |
| XOM | 57.6% | 68.5% | 67.8% | 65.7% | 43.6% | 49.2% | 56.1% | 57.4% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 80 | **55.0%** | 44.1%–65.9% | 52.5% | 55.0% | no | 0.2466 |
| Live, logistic, all sources (VADER) | 80 | **58.8%** | 48.0%–69.5% | 52.5% | 55.0% | within noise | 0.2449 |
| Live, logistic, all sources (FinBERT) | 80 | **60.0%** | 49.3%–70.7% | 52.5% | 55.0% | within noise | 0.2450 |
| Live, gradient boosting | 80 | **46.2%** | 35.3%–57.2% | 52.5% | 55.0% | no | 0.2504 |
| Live, ensemble | 80 | **57.5%** | 46.7%–68.3% | 52.5% | 55.0% | within noise | 0.2460 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 80 | **56.2%** | 45.4%–67.1% | 52.5% | 46.2% | within noise | 0.2506 |
| Live, gradient boosting | 80 | **61.3%** | 50.6%–71.9% | 52.5% | 46.2% | within noise | 0.2490 |
| Live, ensemble | 80 | **55.0%** | 44.1%–65.9% | 52.5% | 46.2% | within noise | 0.2485 |
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
| under 40% | 53.0% (n=247) | 50.6% (n=616) | 50.6% (n=618) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=794) | 52.0% (n=1,101) | 51.9% (n=1,100) | 54.4% (n=1,033) | 52.7% (n=941) |
| 45–48% | 50.8% (n=1,294) | 50.4% (n=1,244) | 50.4% (n=1,245) | 50.7% (n=1,116) | 49.0% (n=1,198) |
| 48–50% | 52.5% (n=1,317) | 55.4% (n=1,144) | 55.4% (n=1,143) | 50.5% (n=986) | 51.3% (n=1,151) |
| 50–52% | 52.6% (n=1,703) | 51.1% (n=1,248) | 51.2% (n=1,247) | 47.3% (n=1,105) | 53.9% (n=1,400) |
| 52–55% | 52.4% (n=2,318) | 52.0% (n=1,747) | 52.0% (n=1,747) | 52.5% (n=1,589) | 52.6% (n=1,986) |
| 55–60% | 52.6% (n=2,116) | 52.4% (n=2,092) | 52.4% (n=2,092) | 52.7% (n=1,538) | 54.6% (n=1,876) |
| 60% or more | 52.3% (n=639) | 53.3% (n=1,236) | 53.3% (n=1,236) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=930) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.0% (n=1,495) | 49.7% (n=1,260) | 47.5% (n=1,279) |
| 45–48% | 50.8% (n=1,442) | 50.1% (n=1,586) | 48.4% (n=1,692) |
| 48–50% | 49.7% (n=1,154) | 49.9% (n=1,415) | 51.3% (n=1,521) |
| 50–52% | 50.0% (n=1,187) | 51.0% (n=1,513) | 51.0% (n=1,462) |
| 52–55% | 52.4% (n=1,534) | 52.3% (n=1,572) | 50.8% (n=1,788) |
| 55–60% | 51.8% (n=1,670) | 50.0% (n=1,105) | 54.0% (n=1,299) |
| 60% or more | 52.9% (n=1,016) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 71 | 49.3% | -0.1% | 0.1% | -0.073 |
| FinBERT | 49 | 51.0% | -0.1% | 0.5% | -0.070 |

The two scorers agree on the direction of the mood on 68% of 90 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,043 | 51.5% | 49.6% | 49.6% | 48.5% | 50.4% | 54.6% |
| AMZN | 1,043 | 49.7% | 50.1% | 50.1% | 49.1% | 49.1% | 50.9% |
| GOOGL | 1,043 | 51.5% | 49.4% | 49.4% | 51.1% | 52.2% | 54.4% |
| JPM | 1,043 | 50.6% | 50.7% | 50.8% | 50.9% | 51.0% | 53.8% |
| META | 1,043 | 52.8% | 52.7% | 52.7% | 49.1% | 51.1% | 50.6% |
| MSFT | 1,043 | 51.7% | 52.0% | 52.0% | 49.8% | 52.1% | 52.0% |
| NVDA | 1,043 | 49.5% | 49.8% | 49.8% | 51.6% | 51.8% | 52.8% |
| TSLA | 1,043 | 53.0% | 53.2% | 53.2% | 49.8% | 52.6% | 49.8% |
| UNH | 1,042 | 50.1% | 48.6% | 48.6% | 49.9% | 52.1% | 51.4% |
| XOM | 1,042 | 49.6% | 48.6% | 48.6% | 51.2% | 53.1% | 52.1% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,043 | 51.1% | 51.0% | 51.5% | 53.1% |
| AMZN | 1,043 | 49.2% | 52.7% | 50.6% | 48.0% |
| GOOGL | 1,043 | 50.0% | 51.6% | 50.7% | 53.6% |
| JPM | 1,043 | 52.4% | 48.9% | 49.7% | 53.2% |
| META | 1,043 | 51.3% | 48.3% | 50.1% | 49.0% |
| MSFT | 1,043 | 51.0% | 50.3% | 50.3% | 48.9% |
| NVDA | 1,043 | 52.0% | 52.4% | 52.8% | 52.3% |
| TSLA | 1,043 | 52.5% | 51.4% | 53.6% | 48.8% |
| UNH | 1,042 | 53.3% | 50.5% | 51.4% | 47.7% |
| XOM | 1,042 | 51.2% | 49.4% | 51.3% | 49.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,043 | +36.1% | +7.7% | 0.47 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,043 | +34.3% | +7.4% | 0.47 | 50.1% |
| Top 3 by logistic, all sources (FinBERT) | 1,043 | +34.3% | +7.4% | 0.47 | 50.1% |
| Top 3 by gradient boosting | 984 | +65.8% | +13.8% | 0.77 | 36.9% |
| Top 3 by ensemble | 984 | +36.8% | +8.4% | 0.53 | 45.9% |
| Buy every stock, every session | 1,043 | -0.3% | -0.1% | 0.08 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,043 | -24.4% | -6.5% | -0.41 | 46.9% |
| Top 3 by gradient boosting | 984 | -41.4% | -12.8% | -0.78 | 39.8% |
| Top 3 by ensemble | 984 | -15.5% | -4.2% | -0.20 | 46.3% |
| Every stock minus SPY | 1,043 | -53.2% | -16.8% | -2.38 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7676 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 263 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1000 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 168 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-06 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-06 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-06 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-06 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-06 | 0 | 0 | 0 |
| META | ok | 2026-10-06 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-06 | 0 | 0 | 0 |
| JPM | ok | 2026-10-06 | 0 | 0 | 0 |
| XOM | ok | 2026-10-06 | 0 | 0 | 0 |
| UNH | ok | 2026-10-06 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
