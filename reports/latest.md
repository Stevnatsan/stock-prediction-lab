# Stock prediction lab: latest report

Generated 2026-10-06 07:34 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **55.4%** | **Buy at open** | 63.3% | **Outperform** | 14 | positive (+0.10) | neutral (+0.03) |
| 2 | AAPL | **49.4%** | Stay out | 54.5% | **Outperform** | 33 | positive (+0.12) | positive (+0.08) |
| 3 | AMZN | **49.1%** | Stay out | 49.5% | – | 46 | positive (+0.20) | neutral (+0.01) |
| 4 | JPM | **48.8%** | Stay out | 57.1% | **Outperform** | 21 | positive (+0.23) | neutral (+0.03) |
| 5 | META | **47.2%** | Stay out | 47.8% | – | 50 | neutral (+0.05) | neutral (-0.02) |
| 6 | UNH | **46.2%** | Stay out | 42.1% | – | 10 | positive (+0.12) | negative (-0.10) |
| 7 | GOOGL | **45.4%** | Stay out | 47.9% | – | 24 | negative (-0.10) | neutral (+0.01) |
| 8 | MSFT | **42.1%** | Stay out | 50.0% | – | 30 | positive (+0.17) | positive (+0.14) |
| 9 | TSLA | **41.7%** | Stay out | 45.1% | – | 25 | positive (+0.16) | positive (+0.09) |
| 10 | NVDA | **41.1%** | Stay out | 39.0% | – | 68 | positive (+0.21) | positive (+0.16) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 53.9% | 54.7% | 54.5% | 54.5% | 44.1% | 50.4% | 49.4% | 52.4% |
| AMZN | 53.7% | 50.9% | 51.0% | 49.5% | 47.3% | 50.2% | 49.1% | 49.9% |
| GOOGL | 51.5% | 45.6% | 47.0% | 47.9% | 45.1% | 49.8% | 45.4% | 48.9% |
| JPM | 52.3% | 50.0% | 49.9% | 57.1% | 47.6% | 51.1% | 48.8% | 54.1% |
| META | 49.3% | 45.4% | 44.6% | 47.8% | 49.0% | 53.7% | 47.2% | 50.8% |
| MSFT | 51.1% | 42.0% | 41.8% | 50.0% | 42.3% | 49.1% | 42.1% | 49.5% |
| NVDA | 46.8% | 39.8% | 40.0% | 39.0% | 42.5% | 49.1% | 41.1% | 44.0% |
| TSLA | 44.1% | 42.1% | 40.5% | 45.1% | 41.3% | 49.1% | 41.7% | 47.1% |
| UNH | 48.6% | 47.3% | 47.3% | 42.1% | 45.1% | 49.8% | 46.2% | 46.0% |
| XOM | 54.8% | 66.7% | 65.5% | 63.3% | 44.1% | 50.4% | 55.4% | 56.8% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 70 | **51.4%** | 39.7%–63.1% | 54.3% | 55.7% | no | 0.2491 |
| Live, logistic, all sources (VADER) | 70 | **55.7%** | 44.1%–67.4% | 54.3% | 55.7% | no | 0.2507 |
| Live, logistic, all sources (FinBERT) | 70 | **55.7%** | 44.1%–67.4% | 54.3% | 55.7% | no | 0.2511 |
| Live, gradient boosting | 70 | **44.3%** | 32.6%–55.9% | 54.3% | 55.7% | no | 0.2518 |
| Live, ensemble | 70 | **55.7%** | 44.1%–67.4% | 54.3% | 55.7% | no | 0.2496 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 70 | **52.9%** | 41.2%–64.6% | 55.7% | 51.4% | no | 0.2555 |
| Live, gradient boosting | 70 | **58.6%** | 47.0%–70.1% | 55.7% | 51.4% | within noise | 0.2487 |
| Live, ensemble | 70 | **52.9%** | 41.2%–64.6% | 55.7% | 51.4% | no | 0.2508 |
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
| under 40% | 53.0% (n=247) | 50.7% (n=615) | 50.7% (n=617) | 55.0% (n=1,049) | 52.1% (n=474) |
| 40–45% | 51.8% (n=793) | 52.0% (n=1,099) | 52.1% (n=1,097) | 54.5% (n=1,028) | 52.9% (n=938) |
| 45–48% | 50.8% (n=1,293) | 50.4% (n=1,241) | 50.4% (n=1,243) | 50.7% (n=1,112) | 49.0% (n=1,195) |
| 48–50% | 52.6% (n=1,315) | 55.4% (n=1,144) | 55.4% (n=1,142) | 50.6% (n=985) | 51.3% (n=1,148) |
| 50–52% | 52.6% (n=1,701) | 51.1% (n=1,246) | 51.1% (n=1,246) | 47.3% (n=1,105) | 53.9% (n=1,400) |
| 52–55% | 52.3% (n=2,314) | 52.0% (n=1,746) | 52.0% (n=1,746) | 52.5% (n=1,589) | 52.6% (n=1,986) |
| 55–60% | 52.6% (n=2,116) | 52.4% (n=2,092) | 52.4% (n=2,092) | 52.7% (n=1,538) | 54.6% (n=1,875) |
| 60% or more | 52.3% (n=639) | 53.3% (n=1,235) | 53.3% (n=1,235) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=929) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 47.1% (n=1,494) | 49.7% (n=1,260) | 47.6% (n=1,278) |
| 45–48% | 50.9% (n=1,439) | 50.1% (n=1,586) | 48.5% (n=1,690) |
| 48–50% | 49.7% (n=1,152) | 50.1% (n=1,410) | 51.4% (n=1,518) |
| 50–52% | 50.0% (n=1,187) | 51.0% (n=1,509) | 51.1% (n=1,461) |
| 52–55% | 52.4% (n=1,533) | 52.3% (n=1,571) | 50.8% (n=1,786) |
| 55–60% | 51.8% (n=1,669) | 50.0% (n=1,105) | 54.0% (n=1,298) |
| 60% or more | 52.8% (n=1,015) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.4 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 62 | 51.6% | -0.1% | – | -0.042 |
| FinBERT | 44 | 52.3% | -0.1% | 0.6% | -0.062 |

The two scorers agree on the direction of the mood on 66% of 80 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,042 | 51.4% | 49.5% | 49.5% | 48.5% | 50.5% | 54.5% |
| AMZN | 1,042 | 49.6% | 50.1% | 50.1% | 49.1% | 49.1% | 50.9% |
| GOOGL | 1,042 | 51.4% | 49.4% | 49.4% | 51.2% | 52.3% | 54.3% |
| JPM | 1,042 | 50.7% | 50.8% | 50.8% | 50.9% | 51.0% | 53.8% |
| META | 1,042 | 52.8% | 52.7% | 52.7% | 49.0% | 51.1% | 50.7% |
| MSFT | 1,042 | 51.7% | 51.9% | 51.9% | 49.7% | 52.1% | 52.0% |
| NVDA | 1,042 | 49.4% | 49.7% | 49.7% | 51.6% | 51.8% | 52.9% |
| TSLA | 1,042 | 53.0% | 53.2% | 53.2% | 49.7% | 52.6% | 49.8% |
| UNH | 1,041 | 50.0% | 48.5% | 48.5% | 49.9% | 52.0% | 51.5% |
| XOM | 1,041 | 49.6% | 48.5% | 48.5% | 51.2% | 53.1% | 52.1% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,042 | 51.1% | 51.0% | 51.5% | 53.1% |
| AMZN | 1,042 | 49.2% | 52.7% | 50.7% | 48.0% |
| GOOGL | 1,042 | 49.9% | 51.6% | 50.7% | 53.6% |
| JPM | 1,042 | 52.5% | 48.9% | 49.7% | 53.3% |
| META | 1,042 | 51.2% | 48.3% | 50.2% | 49.0% |
| MSFT | 1,042 | 51.0% | 50.3% | 50.3% | 48.9% |
| NVDA | 1,042 | 51.9% | 52.4% | 52.8% | 52.3% |
| TSLA | 1,042 | 52.5% | 51.4% | 53.5% | 48.8% |
| UNH | 1,041 | 53.2% | 50.4% | 51.3% | 47.7% |
| XOM | 1,041 | 51.2% | 49.4% | 51.2% | 49.7% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,042 | +35.1% | +7.5% | 0.46 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,042 | +33.5% | +7.2% | 0.46 | 50.1% |
| Top 3 by logistic, all sources (FinBERT) | 1,042 | +33.5% | +7.2% | 0.46 | 50.1% |
| Top 3 by gradient boosting | 983 | +65.8% | +13.8% | 0.77 | 36.9% |
| Top 3 by ensemble | 983 | +35.7% | +8.1% | 0.52 | 45.9% |
| Buy every stock, every session | 1,042 | -0.1% | -0.0% | 0.09 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,042 | -24.5% | -6.6% | -0.41 | 46.8% |
| Top 3 by gradient boosting | 983 | -41.1% | -12.7% | -0.77 | 39.9% |
| Top 3 by ensemble | 983 | -15.5% | -4.2% | -0.20 | 46.3% |
| Every stock minus SPY | 1,042 | -53.0% | -16.7% | -2.37 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7674 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 164 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 1000 |  |
| macro_yahoo | 1 | 0 | 1088 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 162 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-05 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-05 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-05 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-05 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-05 | 0 | 0 | 0 |
| META | ok | 2026-10-05 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-05 | 0 | 0 | 0 |
| JPM | ok | 2026-10-05 | 0 | 0 | 0 |
| XOM | ok | 2026-10-05 | 0 | 0 | 0 |
| UNH | ok | 2026-10-05 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
