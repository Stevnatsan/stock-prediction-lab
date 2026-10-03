# Stock prediction lab: latest report

Generated 2026-10-03 01:12 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **56.0%** | **Buy at open** | 68.9% | **Outperform** | 13 | positive (+0.08) | positive (+0.18) |
| 2 | AMZN | **53.1%** | **Buy at open** | 57.0% | – | 45 | positive (+0.22) | positive (+0.12) |
| 3 | AAPL | **52.3%** | **Buy at open** | 59.0% | **Outperform** | 34 | positive (+0.15) | neutral (-0.02) |
| 4 | GOOGL | **50.7%** | Stay out | 55.9% | – | 34 | positive (+0.17) | positive (+0.09) |
| 5 | JPM | **50.7%** | Stay out | 57.6% | **Outperform** | 25 | positive (+0.20) | neutral (+0.05) |
| 6 | UNH | **48.2%** | Stay out | 41.6% | – | 9 | neutral (+0.04) | negative (-0.13) |
| 7 | META | **46.3%** | Stay out | 45.7% | – | 47 | neutral (+0.05) | negative (-0.17) |
| 8 | MSFT | **45.8%** | Stay out | 54.4% | – | 26 | positive (+0.12) | neutral (+0.02) |
| 9 | TSLA | **44.7%** | Stay out | 46.1% | – | 40 | positive (+0.15) | positive (+0.21) |
| 10 | NVDA | **43.1%** | Stay out | 41.6% | – | 94 | positive (+0.17) | positive (+0.18) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 58.6% | 57.5% | 58.2% | 59.0% | 47.0% | 50.4% | 52.3% | 54.7% |
| AMZN | 58.0% | 56.6% | 56.5% | 57.0% | 49.5% | 50.4% | 53.1% | 53.7% |
| GOOGL | 56.5% | 54.3% | 54.4% | 55.9% | 47.1% | 50.4% | 50.7% | 53.1% |
| JPM | 54.6% | 51.2% | 51.2% | 57.6% | 50.2% | 51.1% | 50.7% | 54.4% |
| META | 48.0% | 41.9% | 41.7% | 45.7% | 50.7% | 51.9% | 46.3% | 48.8% |
| MSFT | 54.6% | 43.8% | 43.8% | 54.4% | 47.9% | 50.4% | 45.8% | 52.4% |
| NVDA | 46.5% | 40.4% | 39.6% | 41.6% | 45.9% | 49.4% | 43.1% | 45.5% |
| TSLA | 46.5% | 43.4% | 42.3% | 46.1% | 46.0% | 49.4% | 44.7% | 47.8% |
| UNH | 48.4% | 46.9% | 47.0% | 41.6% | 49.5% | 51.1% | 48.2% | 46.3% |
| XOM | 57.4% | 64.0% | 63.6% | 68.9% | 48.1% | 50.4% | 56.0% | 59.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 60 | **51.7%** | 39.0%–64.3% | 48.3% | 53.3% | no | 0.2518 |
| Live, logistic, all sources (VADER) | 60 | **58.3%** | 45.9%–70.8% | 48.3% | 53.3% | within noise | 0.2495 |
| Live, logistic, all sources (FinBERT) | 60 | **58.3%** | 45.9%–70.8% | 48.3% | 53.3% | within noise | 0.2497 |
| Live, gradient boosting | 60 | **50.0%** | 37.3%–62.7% | 48.3% | 53.3% | no | 0.2490 |
| Live, ensemble | 60 | **58.3%** | 45.9%–70.8% | 48.3% | 53.3% | within noise | 0.2475 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 60 | **58.3%** | 45.9%–70.8% | 55.0% | 53.3% | within noise | 0.2456 |
| Live, gradient boosting | 60 | **61.7%** | 49.4%–74.0% | 55.0% | 53.3% | within noise | 0.2485 |
| Live, ensemble | 60 | **58.3%** | 45.9%–70.8% | 55.0% | 53.3% | within noise | 0.2458 |
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
| under 40% | 53.0% (n=247) | 50.7% (n=615) | 50.6% (n=616) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=793) | 51.9% (n=1,095) | 51.9% (n=1,094) | 54.5% (n=1,028) | 52.8% (n=936) |
| 45–48% | 50.7% (n=1,290) | 50.4% (n=1,240) | 50.4% (n=1,242) | 50.5% (n=1,107) | 49.0% (n=1,193) |
| 48–50% | 52.6% (n=1,314) | 55.4% (n=1,144) | 55.4% (n=1,142) | 50.4% (n=982) | 51.3% (n=1,147) |
| 50–52% | 52.6% (n=1,701) | 51.2% (n=1,245) | 51.2% (n=1,245) | 47.3% (n=1,103) | 53.9% (n=1,398) |
| 52–55% | 52.3% (n=2,312) | 52.0% (n=1,745) | 52.0% (n=1,745) | 52.5% (n=1,589) | 52.6% (n=1,984) |
| 55–60% | 52.5% (n=2,112) | 52.3% (n=2,090) | 52.3% (n=2,090) | 52.7% (n=1,538) | 54.6% (n=1,874) |
| 60% or more | 52.3% (n=639) | 53.2% (n=1,234) | 53.2% (n=1,234) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=929) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.0% (n=1,492) | 49.7% (n=1,260) | 47.6% (n=1,278) |
| 45–48% | 50.8% (n=1,437) | 50.1% (n=1,586) | 48.4% (n=1,687) |
| 48–50% | 49.7% (n=1,152) | 50.0% (n=1,408) | 51.4% (n=1,517) |
| 50–52% | 50.0% (n=1,187) | 51.0% (n=1,501) | 51.1% (n=1,461) |
| 52–55% | 52.3% (n=1,532) | 52.3% (n=1,571) | 50.9% (n=1,781) |
| 55–60% | 51.9% (n=1,665) | 50.0% (n=1,105) | 54.0% (n=1,297) |
| 60% or more | 52.9% (n=1,014) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 54 | 46.3% | -0.3% | – | -0.079 |
| FinBERT | 37 | 48.6% | -0.3% | 0.4% | -0.107 |

The two scorers agree on the direction of the mood on 66% of 70 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,041 | 51.4% | 49.5% | 49.5% | 48.6% | 50.4% | 54.5% |
| AMZN | 1,041 | 49.6% | 50.0% | 50.0% | 49.2% | 49.1% | 50.8% |
| GOOGL | 1,041 | 51.4% | 49.4% | 49.4% | 51.2% | 52.2% | 54.3% |
| JPM | 1,041 | 50.7% | 50.8% | 50.8% | 50.9% | 51.0% | 53.9% |
| META | 1,041 | 52.8% | 52.7% | 52.7% | 49.0% | 51.1% | 50.6% |
| MSFT | 1,041 | 51.7% | 52.0% | 52.0% | 49.8% | 52.1% | 52.0% |
| NVDA | 1,041 | 49.5% | 49.8% | 49.8% | 51.6% | 51.8% | 52.8% |
| TSLA | 1,041 | 53.0% | 53.2% | 53.2% | 49.8% | 52.6% | 49.8% |
| UNH | 1,040 | 50.1% | 48.6% | 48.6% | 49.9% | 52.1% | 51.4% |
| XOM | 1,040 | 49.5% | 48.5% | 48.5% | 51.3% | 53.0% | 52.0% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,041 | 51.1% | 51.0% | 51.5% | 53.1% |
| AMZN | 1,041 | 49.3% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,041 | 49.9% | 51.5% | 50.6% | 53.6% |
| JPM | 1,041 | 52.5% | 49.0% | 49.8% | 53.3% |
| META | 1,041 | 51.3% | 48.3% | 50.2% | 49.0% |
| MSFT | 1,041 | 50.9% | 50.2% | 50.2% | 48.9% |
| NVDA | 1,041 | 52.0% | 52.4% | 52.9% | 52.3% |
| TSLA | 1,041 | 52.5% | 51.4% | 53.6% | 48.8% |
| UNH | 1,040 | 53.3% | 50.4% | 51.4% | 47.7% |
| XOM | 1,040 | 51.2% | 49.4% | 51.3% | 49.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,041 | +34.9% | +7.5% | 0.45 | 50.6% |
| Top 3 by logistic, all sources (VADER) | 1,041 | +33.3% | +7.2% | 0.46 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,041 | +33.3% | +7.2% | 0.46 | 50.0% |
| Top 3 by gradient boosting | 982 | +65.8% | +13.9% | 0.77 | 37.0% |
| Top 3 by ensemble | 982 | +35.5% | +8.1% | 0.52 | 45.8% |
| Buy every stock, every session | 1,041 | -1.0% | -0.2% | 0.07 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,041 | -23.9% | -6.4% | -0.40 | 46.9% |
| Top 3 by gradient boosting | 982 | -41.1% | -12.7% | -0.77 | 39.9% |
| Top 3 by ensemble | 982 | -14.8% | -4.0% | -0.19 | 46.3% |
| Every stock minus SPY | 1,041 | -53.1% | -16.8% | -2.38 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7671 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 331 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1004 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11946 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 162 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-02 | 0 | 8 | 34 |
| MSFT | ok | 2026-10-02 | 0 | 8 | 26 |
| NVDA | ok | 2026-10-02 | 0 | 8 | 94 |
| AMZN | ok | 2026-10-02 | 0 | 8 | 45 |
| GOOGL | ok | 2026-10-02 | 0 | 8 | 34 |
| META | ok | 2026-10-02 | 0 | 8 | 47 |
| TSLA | ok | 2026-10-02 | 0 | 8 | 40 |
| JPM | ok | 2026-10-02 | 0 | 8 | 25 |
| XOM | ok | 2026-10-02 | 0 | 8 | 13 |
| UNH | ok | 2026-10-02 | 0 | 8 | 9 |

---

Educational project. Not financial advice.
