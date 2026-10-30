# Stock prediction lab: latest report

Generated 2026-10-30 07:05 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **56.4%** | **Buy at open** | 56.4% | **Outperform** | 42 | neutral (-0.00) | negative (-0.11) |
| 2 | AAPL | **54.4%** | **Buy at open** | 47.3% | – | 33 | positive (+0.13) | neutral (+0.02) |
| 3 | NVDA | **54.1%** | **Buy at open** | 53.1% | **Outperform** | 59 | neutral (+0.01) | negative (-0.16) |
| 4 | TSLA | **52.2%** | Stay out | 56.5% | **Outperform** | 22 | positive (+0.14) | positive (+0.14) |
| 5 | UNH | **51.4%** | Stay out | 44.9% | – | 5 | neutral (-0.01) | negative (-0.08) |
| 6 | JPM | **49.4%** | Stay out | 44.1% | – | 20 | positive (+0.14) | neutral (+0.01) |
| 7 | XOM | **47.6%** | Stay out | 41.8% | – | 39 | positive (+0.14) | neutral (+0.04) |
| 8 | GOOGL | **44.9%** | Stay out | 50.7% | – | 95 | negative (-0.14) | negative (-0.52) |
| 9 | MSFT | **38.7%** | Stay out | 31.7% | – | 62 | positive (+0.07) | negative (-0.06) |
| 10 | AMZN | **31.4%** | Stay out | 38.4% | – | 63 | neutral (+0.03) | negative (-0.50) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 54.4% | 60.1% | 60.5% | 47.3% | 48.8% | 49.3% | 54.4% | 48.3% |
| AMZN | 43.2% | 34.1% | 39.1% | 38.4% | 28.7% | 46.2% | 31.4% | 42.3% |
| GOOGL | 36.5% | 47.0% | 41.0% | 50.7% | 42.8% | 51.2% | 44.9% | 51.0% |
| JPM | 49.6% | 47.8% | 47.8% | 44.1% | 51.0% | 49.5% | 49.4% | 46.8% |
| META | 54.2% | 58.1% | 56.8% | 56.4% | 54.7% | 49.9% | 56.4% | 53.1% |
| MSFT | 42.3% | 37.9% | 39.0% | 31.7% | 39.5% | 49.9% | 38.7% | 40.8% |
| NVDA | 52.7% | 55.1% | 54.7% | 53.1% | 53.1% | 50.8% | 54.1% | 51.9% |
| TSLA | 43.3% | 57.1% | 56.8% | 56.5% | 47.4% | 49.8% | 52.2% | 53.1% |
| UNH | 51.0% | 52.8% | 54.2% | 44.9% | 50.1% | 49.5% | 51.4% | 47.2% |
| XOM | 57.6% | 56.6% | 56.5% | 41.8% | 38.7% | 46.4% | 47.6% | 44.1% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 250 | **52.4%** | 46.2%–58.6% | 48.4% | 46.4% | within noise | 0.2495 |
| Live, logistic, all sources (VADER) | 250 | **53.6%** | 47.4%–59.8% | 48.4% | 46.4% | within noise | 0.2516 |
| Live, logistic, all sources (FinBERT) | 250 | **53.6%** | 47.4%–59.8% | 48.4% | 46.4% | within noise | 0.2513 |
| Live, gradient boosting | 250 | **50.4%** | 44.2%–56.6% | 48.4% | 46.4% | no | 0.2499 |
| Live, ensemble | 250 | **52.8%** | 46.6%–59.0% | 48.4% | 46.4% | within noise | 0.2487 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 250 | **56.0%** | 49.8%–62.2% | 45.6% | 45.6% | within noise | 0.2489 |
| Live, gradient boosting | 250 | **55.6%** | 49.4%–61.8% | 45.6% | 45.6% | within noise | 0.2486 |
| Live, ensemble | 250 | **55.6%** | 49.4%–61.8% | 45.6% | 45.6% | within noise | 0.2471 |
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
| under 40% | 53.3% (n=255) | 50.5% (n=637) | 50.5% (n=639) | 55.0% (n=1,051) | 51.9% (n=478) |
| 40–45% | 51.7% (n=817) | 51.6% (n=1,129) | 51.6% (n=1,129) | 53.8% (n=1,059) | 52.4% (n=965) |
| 45–48% | 50.6% (n=1,316) | 50.6% (n=1,261) | 50.5% (n=1,267) | 50.9% (n=1,141) | 48.9% (n=1,232) |
| 48–50% | 52.3% (n=1,340) | 55.1% (n=1,164) | 55.2% (n=1,160) | 50.2% (n=1,013) | 51.4% (n=1,172) |
| 50–52% | 52.5% (n=1,732) | 51.2% (n=1,260) | 51.2% (n=1,259) | 47.5% (n=1,138) | 53.6% (n=1,424) |
| 52–55% | 52.0% (n=2,355) | 51.8% (n=1,769) | 51.9% (n=1,768) | 52.3% (n=1,622) | 52.6% (n=2,016) |
| 55–60% | 52.7% (n=2,135) | 52.4% (n=2,120) | 52.3% (n=2,116) | 52.6% (n=1,562) | 54.5% (n=1,903) |
| 60% or more | 52.5% (n=648) | 53.3% (n=1,258) | 53.3% (n=1,260) | 54.9% (n=1,422) | 50.0% (n=818) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.2% (n=958) | 49.7% (n=768) | 51.2% (n=430) |
| 40–45% | 46.7% (n=1,526) | 49.7% (n=1,260) | 47.2% (n=1,308) |
| 45–48% | 50.6% (n=1,463) | 49.8% (n=1,611) | 48.1% (n=1,730) |
| 48–50% | 49.6% (n=1,169) | 49.5% (n=1,496) | 51.3% (n=1,551) |
| 50–52% | 49.9% (n=1,205) | 50.8% (n=1,574) | 50.9% (n=1,490) |
| 52–55% | 52.4% (n=1,552) | 52.3% (n=1,575) | 50.8% (n=1,804) |
| 55–60% | 51.8% (n=1,685) | 50.0% (n=1,105) | 53.9% (n=1,324) |
| 60% or more | 52.7% (n=1,040) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 220 | 47.7% | -0.1% | 0.1% | -0.065 |
| FinBERT | 168 | 46.4% | -0.1% | 0.5% | -0.137 |

The two scorers agree on the direction of the mood on 70% of 260 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 25 | 48.0% | 60.0% | 56.0% | 24.0% | 44.0% | 64.0% |
| AMZN | 25 | 60.0% | 56.0% | 56.0% | 56.0% | 52.0% | 44.0% |
| GOOGL | 25 | 68.0% | 60.0% | 56.0% | 68.0% | 84.0% | 48.0% |
| JPM | 25 | 44.0% | 36.0% | 44.0% | 36.0% | 24.0% | 40.0% |
| META | 25 | 44.0% | 56.0% | 52.0% | 60.0% | 60.0% | 36.0% |
| MSFT | 25 | 48.0% | 52.0% | 52.0% | 60.0% | 48.0% | 48.0% |
| NVDA | 25 | 48.0% | 56.0% | 56.0% | 60.0% | 56.0% | 32.0% |
| TSLA | 25 | 48.0% | 52.0% | 52.0% | 36.0% | 40.0% | 52.0% |
| UNH | 25 | 48.0% | 44.0% | 44.0% | 60.0% | 52.0% | 52.0% |
| XOM | 25 | 68.0% | 64.0% | 68.0% | 44.0% | 68.0% | 68.0% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 25 | 64.0% | 40.0% | 68.0% | 60.0% |
| AMZN | 25 | 52.0% | 60.0% | 52.0% | 48.0% |
| GOOGL | 25 | 56.0% | 72.0% | 52.0% | 44.0% |
| JPM | 25 | 44.0% | 60.0% | 44.0% | 44.0% |
| META | 25 | 60.0% | 36.0% | 52.0% | 32.0% |
| MSFT | 25 | 60.0% | 60.0% | 60.0% | 48.0% |
| NVDA | 25 | 52.0% | 52.0% | 52.0% | 36.0% |
| TSLA | 25 | 52.0% | 56.0% | 52.0% | 44.0% |
| UNH | 25 | 56.0% | 60.0% | 60.0% | 40.0% |
| XOM | 25 | 64.0% | 60.0% | 64.0% | 60.0% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,060 | +41.7% | +8.6% | 0.51 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,060 | +40.1% | +8.3% | 0.52 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,060 | +40.1% | +8.3% | 0.52 | 50.4% |
| Top 3 by gradient boosting | 1,001 | +67.5% | +13.9% | 0.76 | 36.7% |
| Top 3 by ensemble | 1,001 | +38.8% | +8.6% | 0.55 | 46.1% |
| Buy every stock, every session | 1,060 | -3.8% | -0.9% | 0.03 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,060 | -23.3% | -6.1% | -0.37 | 46.9% |
| Top 3 by gradient boosting | 1,001 | -43.4% | -13.3% | -0.82 | 39.2% |
| Top 3 by ensemble | 1,001 | -14.1% | -3.8% | -0.17 | 46.3% |
| Every stock minus SPY | 1,060 | -55.3% | -17.4% | -2.49 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7875 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 210 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 986 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 164 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-29 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-29 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-29 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-29 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-29 | 0 | 0 | 0 |
| META | ok | 2026-10-29 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-29 | 0 | 0 | 0 |
| JPM | ok | 2026-10-29 | 0 | 0 | 0 |
| XOM | ok | 2026-10-29 | 0 | 0 | 0 |
| UNH | ok | 2026-10-29 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
