# Stock prediction lab: latest report

Generated 2026-10-14 06:08 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **59.2%** | **Buy at open** | 63.2% | **Outperform** | 17 | neutral (+0.05) | positive (+0.45) |
| 2 | UNH | **56.5%** | **Buy at open** | 57.2% | **Outperform** | 54 | positive (+0.26) | positive (+0.31) |
| 3 | AAPL | **53.6%** | **Buy at open** | 51.0% | – | 50 | positive (+0.13) | positive (+0.06) |
| 4 | AMZN | **51.6%** | Stay out | 50.2% | – | 38 | positive (+0.15) | neutral (+0.04) |
| 5 | GOOGL | **48.0%** | Stay out | 44.0% | – | 26 | positive (+0.11) | neutral (-0.04) |
| 6 | TSLA | **47.3%** | Stay out | 39.7% | – | 22 | positive (+0.10) | positive (+0.11) |
| 7 | JPM | **46.5%** | Stay out | 38.1% | – | 56 | neutral (-0.02) | negative (-0.28) |
| 8 | META | **42.7%** | Stay out | 41.5% | – | 71 | positive (+0.18) | positive (+0.16) |
| 9 | NVDA | **40.6%** | Stay out | 33.6% | – | 82 | positive (+0.16) | neutral (+0.03) |
| 10 | MSFT | **39.4%** | Stay out | 39.5% | – | 32 | neutral (+0.04) | neutral (-0.01) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 52.2% | 54.7% | 54.9% | 51.0% | 52.6% | 49.3% | 53.6% | 50.2% |
| AMZN | 50.3% | 52.6% | 52.3% | 50.2% | 50.6% | 49.1% | 51.6% | 49.7% |
| GOOGL | 51.0% | 52.5% | 51.8% | 44.0% | 43.4% | 49.0% | 48.0% | 46.5% |
| JPM | 46.9% | 48.2% | 44.2% | 38.1% | 44.8% | 48.7% | 46.5% | 43.4% |
| META | 41.6% | 34.9% | 35.3% | 41.5% | 50.6% | 50.0% | 42.7% | 45.8% |
| MSFT | 39.7% | 34.4% | 34.4% | 39.5% | 44.4% | 47.8% | 39.4% | 43.7% |
| NVDA | 40.5% | 39.3% | 39.3% | 33.6% | 41.9% | 46.7% | 40.6% | 40.2% |
| TSLA | 46.4% | 44.2% | 44.8% | 39.7% | 50.4% | 49.5% | 47.3% | 44.6% |
| UNH | 56.5% | 61.7% | 61.1% | 57.2% | 51.3% | 49.4% | 56.5% | 53.3% |
| XOM | 60.0% | 70.8% | 71.1% | 63.2% | 47.6% | 49.2% | 59.2% | 56.2% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 130 | **55.4%** | 46.8%–63.9% | 51.5% | 53.8% | within noise | 0.2488 |
| Live, logistic, all sources (VADER) | 130 | **58.5%** | 50.0%–66.9% | 51.5% | 53.8% | within noise | 0.2454 |
| Live, logistic, all sources (FinBERT) | 130 | **58.5%** | 50.0%–66.9% | 51.5% | 53.8% | within noise | 0.2457 |
| Live, gradient boosting | 130 | **51.5%** | 42.9%–60.1% | 51.5% | 53.8% | no | 0.2479 |
| Live, ensemble | 130 | **56.2%** | 47.6%–64.7% | 51.5% | 53.8% | within noise | 0.2449 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 130 | **58.5%** | 50.0%–66.9% | 50.0% | 49.2% | within noise | 0.2468 |
| Live, gradient boosting | 130 | **59.2%** | 50.8%–67.7% | 50.0% | 49.2% | yes | 0.2480 |
| Live, ensemble | 130 | **56.2%** | 47.6%–64.7% | 50.0% | 49.2% | within noise | 0.2461 |
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
| under 40% | 53.0% (n=247) | 50.9% (n=619) | 50.9% (n=621) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.9% (n=799) | 51.6% (n=1,114) | 51.6% (n=1,113) | 54.1% (n=1,042) | 52.7% (n=949) |
| 45–48% | 50.7% (n=1,299) | 50.5% (n=1,249) | 50.6% (n=1,252) | 50.8% (n=1,125) | 48.9% (n=1,209) |
| 48–50% | 52.3% (n=1,322) | 55.3% (n=1,149) | 55.3% (n=1,147) | 50.4% (n=997) | 51.4% (n=1,160) |
| 50–52% | 52.7% (n=1,710) | 51.2% (n=1,249) | 51.2% (n=1,248) | 47.5% (n=1,114) | 53.8% (n=1,405) |
| 52–55% | 52.2% (n=2,335) | 52.1% (n=1,754) | 52.1% (n=1,752) | 52.5% (n=1,599) | 52.6% (n=1,995) |
| 55–60% | 52.7% (n=2,127) | 52.4% (n=2,103) | 52.3% (n=2,104) | 52.7% (n=1,540) | 54.7% (n=1,882) |
| 60% or more | 52.3% (n=639) | 53.4% (n=1,241) | 53.4% (n=1,241) | 54.9% (n=1,422) | 50.1% (n=814) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.6% (n=935) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,502) | 49.7% (n=1,260) | 47.5% (n=1,285) |
| 45–48% | 50.7% (n=1,446) | 50.0% (n=1,597) | 48.2% (n=1,702) |
| 48–50% | 49.6% (n=1,160) | 49.8% (n=1,433) | 51.3% (n=1,531) |
| 50–52% | 50.0% (n=1,194) | 51.0% (n=1,532) | 51.0% (n=1,472) |
| 52–55% | 52.4% (n=1,541) | 52.3% (n=1,574) | 50.9% (n=1,793) |
| 55–60% | 51.8% (n=1,676) | 50.0% (n=1,105) | 54.1% (n=1,308) |
| 60% or more | 52.8% (n=1,024) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 117 | 47.9% | -0.1% | 0.5% | -0.080 |
| FinBERT | 87 | 48.3% | -0.1% | 0.6% | -0.082 |

The two scorers agree on the direction of the mood on 71% of 140 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,048 | 51.4% | 49.6% | 49.5% | 48.4% | 50.5% | 54.6% |
| AMZN | 1,048 | 49.6% | 50.1% | 50.1% | 49.1% | 48.9% | 50.9% |
| GOOGL | 1,048 | 51.5% | 49.4% | 49.4% | 51.1% | 52.2% | 54.4% |
| JPM | 1,048 | 50.7% | 50.7% | 50.8% | 51.0% | 51.1% | 53.8% |
| META | 1,048 | 52.9% | 52.8% | 52.8% | 49.2% | 51.2% | 50.6% |
| MSFT | 1,048 | 51.6% | 52.0% | 52.0% | 50.1% | 52.2% | 51.9% |
| NVDA | 1,048 | 49.5% | 49.9% | 49.9% | 51.7% | 51.9% | 52.7% |
| TSLA | 1,048 | 53.0% | 53.1% | 53.1% | 49.8% | 52.6% | 49.8% |
| UNH | 1,047 | 50.2% | 48.6% | 48.6% | 49.9% | 52.1% | 51.4% |
| XOM | 1,047 | 49.8% | 48.7% | 48.7% | 51.2% | 53.2% | 52.2% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,048 | 51.1% | 50.9% | 51.6% | 53.1% |
| AMZN | 1,048 | 49.2% | 52.8% | 50.7% | 48.0% |
| GOOGL | 1,048 | 49.9% | 51.6% | 50.6% | 53.5% |
| JPM | 1,048 | 52.6% | 49.1% | 49.8% | 53.3% |
| META | 1,048 | 51.3% | 48.2% | 50.1% | 49.0% |
| MSFT | 1,048 | 51.0% | 50.3% | 50.3% | 48.9% |
| NVDA | 1,048 | 52.0% | 52.6% | 52.9% | 52.1% |
| TSLA | 1,048 | 52.6% | 51.6% | 53.6% | 48.8% |
| UNH | 1,047 | 53.4% | 50.5% | 51.5% | 47.6% |
| XOM | 1,047 | 51.4% | 49.4% | 51.4% | 49.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,048 | +38.4% | +8.1% | 0.48 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,048 | +34.6% | +7.4% | 0.47 | 50.2% |
| Top 3 by logistic, all sources (FinBERT) | 1,048 | +34.6% | +7.4% | 0.47 | 50.2% |
| Top 3 by gradient boosting | 989 | +70.2% | +14.5% | 0.79 | 36.9% |
| Top 3 by ensemble | 989 | +36.9% | +8.3% | 0.53 | 46.0% |
| Buy every stock, every session | 1,048 | -0.9% | -0.2% | 0.08 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,048 | -24.2% | -6.4% | -0.40 | 46.9% |
| Top 3 by gradient boosting | 989 | -43.3% | -13.5% | -0.83 | 39.6% |
| Top 3 by ensemble | 989 | -14.9% | -4.0% | -0.19 | 46.4% |
| Every stock minus SPY | 1,048 | -53.8% | -16.9% | -2.41 | 42.2% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7770 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 200 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 994 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 165 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-13 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-13 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-13 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-13 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-13 | 0 | 0 | 0 |
| META | ok | 2026-10-13 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-13 | 0 | 0 | 0 |
| JPM | ok | 2026-10-13 | 0 | 0 | 0 |
| XOM | ok | 2026-10-13 | 0 | 0 | 0 |
| UNH | ok | 2026-10-13 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
