# Stock prediction lab: latest report

Generated 2026-10-27 06:16 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | **58.8%** | **Buy at open** | 58.2% | – | 67 | positive (+0.11) | negative (-0.07) |
| 2 | MSFT | **58.7%** | **Buy at open** | 67.4% | **Outperform** | 55 | positive (+0.09) | positive (+0.08) |
| 3 | TSLA | **58.3%** | **Buy at open** | 66.3% | **Outperform** | 48 | positive (+0.19) | positive (+0.20) |
| 4 | XOM | **58.0%** | Stay out | 52.2% | – | 27 | positive (+0.13) | positive (+0.07) |
| 5 | META | **57.1%** | Stay out | 61.4% | – | 79 | positive (+0.06) | neutral (-0.01) |
| 6 | UNH | **54.8%** | Stay out | 48.2% | – | 9 | positive (+0.07) | positive (+0.13) |
| 7 | JPM | **54.7%** | Stay out | 50.0% | – | 21 | positive (+0.15) | neutral (+0.04) |
| 8 | AAPL | **53.4%** | Stay out | 64.6% | **Outperform** | 33 | neutral (+0.05) | negative (-0.09) |
| 9 | GOOGL | **53.1%** | Stay out | 48.1% | – | 35 | positive (+0.13) | neutral (+0.03) |
| 10 | AMZN | **52.6%** | Stay out | 48.5% | – | 49 | positive (+0.20) | positive (+0.07) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 51.6% | 57.6% | 56.6% | 64.6% | 49.2% | 50.6% | 53.4% | 57.6% |
| AMZN | 53.0% | 48.2% | 47.7% | 48.5% | 57.0% | 50.6% | 52.6% | 49.6% |
| GOOGL | 60.0% | 49.3% | 49.3% | 48.1% | 56.8% | 50.9% | 53.1% | 49.5% |
| JPM | 50.3% | 52.4% | 52.6% | 50.0% | 57.0% | 52.6% | 54.7% | 51.3% |
| META | 53.2% | 57.6% | 56.5% | 61.4% | 56.5% | 50.7% | 57.1% | 56.1% |
| MSFT | 54.4% | 63.2% | 62.8% | 67.4% | 54.2% | 50.2% | 58.7% | 58.8% |
| NVDA | 53.9% | 60.1% | 60.3% | 58.2% | 57.6% | 50.2% | 58.8% | 54.2% |
| TSLA | 50.3% | 66.6% | 66.3% | 66.3% | 50.0% | 48.8% | 58.3% | 57.6% |
| UNH | 50.2% | 53.1% | 53.3% | 48.2% | 56.5% | 50.6% | 54.8% | 49.4% |
| XOM | 63.1% | 63.4% | 63.8% | 52.2% | 52.7% | 51.2% | 58.0% | 51.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 220 | **52.3%** | 45.7%–58.9% | 50.0% | 47.3% | within noise | 0.2496 |
| Live, logistic, all sources (VADER) | 220 | **55.0%** | 48.4%–61.6% | 50.0% | 47.3% | within noise | 0.2492 |
| Live, logistic, all sources (FinBERT) | 220 | **55.9%** | 49.3%–62.5% | 50.0% | 47.3% | within noise | 0.2490 |
| Live, gradient boosting | 220 | **52.3%** | 45.7%–58.9% | 50.0% | 47.3% | within noise | 0.2492 |
| Live, ensemble | 220 | **53.6%** | 47.0%–60.2% | 50.0% | 47.3% | within noise | 0.2471 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 220 | **57.3%** | 50.7%–63.8% | 47.3% | 45.5% | within noise | 0.2477 |
| Live, gradient boosting | 220 | **55.0%** | 48.4%–61.6% | 47.3% | 45.5% | within noise | 0.2488 |
| Live, ensemble | 220 | **56.8%** | 50.3%–63.4% | 47.3% | 45.5% | within noise | 0.2466 |
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
| under 40% | 53.3% (n=255) | 50.7% (n=635) | 50.7% (n=637) | 55.0% (n=1,050) | 52.1% (n=476) |
| 40–45% | 51.7% (n=816) | 51.6% (n=1,129) | 51.6% (n=1,129) | 53.9% (n=1,058) | 52.4% (n=965) |
| 45–48% | 50.7% (n=1,313) | 50.6% (n=1,260) | 50.5% (n=1,263) | 50.9% (n=1,141) | 48.9% (n=1,232) |
| 48–50% | 52.4% (n=1,335) | 55.1% (n=1,159) | 55.1% (n=1,156) | 50.1% (n=1,009) | 51.4% (n=1,171) |
| 50–52% | 52.5% (n=1,722) | 51.1% (n=1,254) | 51.2% (n=1,255) | 47.7% (n=1,135) | 53.7% (n=1,418) |
| 52–55% | 52.1% (n=2,348) | 51.9% (n=1,766) | 51.9% (n=1,764) | 52.4% (n=1,616) | 52.5% (n=2,006) |
| 55–60% | 52.8% (n=2,134) | 52.4% (n=2,113) | 52.4% (n=2,112) | 52.7% (n=1,547) | 54.7% (n=1,893) |
| 60% or more | 52.4% (n=645) | 53.5% (n=1,252) | 53.5% (n=1,252) | 54.9% (n=1,422) | 50.1% (n=817) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=956) | 49.7% (n=768) | 51.4% (n=428) |
| 40–45% | 46.7% (n=1,523) | 49.7% (n=1,260) | 47.2% (n=1,308) |
| 45–48% | 50.8% (n=1,459) | 49.9% (n=1,608) | 48.2% (n=1,724) |
| 48–50% | 49.5% (n=1,164) | 49.7% (n=1,485) | 51.3% (n=1,545) |
| 50–52% | 49.9% (n=1,201) | 50.8% (n=1,559) | 51.0% (n=1,485) |
| 52–55% | 52.4% (n=1,551) | 52.3% (n=1,574) | 50.9% (n=1,799) |
| 55–60% | 51.9% (n=1,680) | 50.0% (n=1,105) | 54.0% (n=1,318) |
| 60% or more | 52.8% (n=1,034) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 193 | 48.7% | -0.1% | 0.5% | -0.104 |
| FinBERT | 148 | 48.6% | -0.1% | 0.5% | -0.142 |

The two scorers agree on the direction of the mood on 70% of 230 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 22 | 45.5% | 59.1% | 54.5% | 27.3% | 40.9% | 63.6% |
| AMZN | 22 | 54.5% | 54.5% | 59.1% | 54.5% | 45.5% | 40.9% |
| GOOGL | 22 | 63.6% | 63.6% | 59.1% | 63.6% | 81.8% | 45.5% |
| JPM | 22 | 40.9% | 31.8% | 40.9% | 36.4% | 22.7% | 40.9% |
| META | 22 | 50.0% | 59.1% | 59.1% | 63.6% | 63.6% | 36.4% |
| MSFT | 22 | 45.5% | 50.0% | 50.0% | 63.6% | 50.0% | 54.5% |
| NVDA | 22 | 50.0% | 63.6% | 63.6% | 68.2% | 63.6% | 36.4% |
| TSLA | 22 | 45.5% | 54.5% | 54.5% | 40.9% | 40.9% | 54.5% |
| UNH | 22 | 54.5% | 45.5% | 45.5% | 63.6% | 54.5% | 54.5% |
| XOM | 22 | 72.7% | 68.2% | 72.7% | 40.9% | 72.7% | 72.7% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 22 | 63.6% | 36.4% | 68.2% | 59.1% |
| AMZN | 22 | 54.5% | 54.5% | 54.5% | 45.5% |
| GOOGL | 22 | 59.1% | 68.2% | 54.5% | 40.9% |
| JPM | 22 | 45.5% | 59.1% | 45.5% | 45.5% |
| META | 22 | 63.6% | 40.9% | 54.5% | 31.8% |
| MSFT | 22 | 63.6% | 63.6% | 63.6% | 54.5% |
| NVDA | 22 | 54.5% | 54.5% | 54.5% | 40.9% |
| TSLA | 22 | 54.5% | 54.5% | 54.5% | 45.5% |
| UNH | 22 | 50.0% | 59.1% | 54.5% | 45.5% |
| XOM | 22 | 63.6% | 59.1% | 63.6% | 63.6% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,057 | +43.5% | +9.0% | 0.52 | 51.1% |
| Top 3 by logistic, all sources (VADER) | 1,057 | +41.2% | +8.6% | 0.53 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,057 | +41.2% | +8.6% | 0.53 | 50.4% |
| Top 3 by gradient boosting | 998 | +69.7% | +14.3% | 0.78 | 36.8% |
| Top 3 by ensemble | 998 | +39.0% | +8.7% | 0.55 | 46.1% |
| Buy every stock, every session | 1,057 | -2.9% | -0.7% | 0.05 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,057 | -22.4% | -5.9% | -0.35 | 46.9% |
| Top 3 by gradient boosting | 998 | -42.9% | -13.2% | -0.81 | 39.3% |
| Top 3 by ensemble | 998 | -13.1% | -3.5% | -0.15 | 46.3% |
| Every stock minus SPY | 1,057 | -54.6% | -17.2% | -2.45 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7840 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 9 | 0 | 290 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 976 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 158 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-26 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-26 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-26 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-26 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-26 | 0 | 0 | 0 |
| META | ok | 2026-10-26 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-26 | 0 | 0 | 0 |
| JPM | ok | 2026-10-26 | 0 | 0 | 0 |
| XOM | ok | 2026-10-26 | 0 | 0 | 0 |
| UNH | ok | 2026-10-26 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
