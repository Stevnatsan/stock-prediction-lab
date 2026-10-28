# Stock prediction lab: latest report

Generated 2026-10-28 01:21 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | TSLA | **61.5%** | **Buy at open** | 67.9% | **Outperform** | 50 | positive (+0.22) | positive (+0.39) |
| 2 | AAPL | **59.5%** | **Buy at open** | 64.8% | **Outperform** | 33 | positive (+0.13) | positive (+0.13) |
| 3 | XOM | **58.4%** | **Buy at open** | 51.1% | – | 21 | positive (+0.14) | neutral (-0.02) |
| 4 | META | **57.4%** | Stay out | 55.3% | **Outperform** | 64 | positive (+0.11) | positive (+0.14) |
| 5 | JPM | **53.9%** | Stay out | 48.9% | – | 24 | positive (+0.12) | positive (+0.08) |
| 6 | UNH | **53.2%** | Stay out | 44.5% | – | 7 | positive (+0.16) | neutral (+0.00) |
| 7 | AMZN | **52.8%** | Stay out | 49.6% | – | 43 | positive (+0.29) | positive (+0.19) |
| 8 | MSFT | **52.2%** | Stay out | 50.9% | – | 62 | positive (+0.17) | positive (+0.22) |
| 9 | GOOGL | **51.4%** | Stay out | 44.1% | – | 55 | positive (+0.08) | neutral (+0.04) |
| 10 | NVDA | **50.5%** | Stay out | 45.1% | – | 79 | positive (+0.13) | positive (+0.08) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 55.0% | 62.6% | 62.3% | 64.8% | 56.3% | 49.4% | 59.5% | 57.1% |
| AMZN | 51.6% | 50.6% | 49.2% | 49.6% | 55.1% | 50.0% | 52.8% | 49.8% |
| GOOGL | 52.0% | 46.7% | 47.0% | 44.1% | 56.1% | 50.2% | 51.4% | 47.2% |
| JPM | 50.0% | 50.7% | 51.0% | 48.9% | 57.1% | 50.0% | 53.9% | 49.5% |
| META | 50.1% | 57.2% | 56.9% | 55.3% | 57.5% | 50.2% | 57.4% | 52.8% |
| MSFT | 46.5% | 49.1% | 47.6% | 50.9% | 55.3% | 51.2% | 52.2% | 51.1% |
| NVDA | 47.7% | 50.5% | 50.3% | 45.1% | 50.5% | 49.3% | 50.5% | 47.2% |
| TSLA | 53.1% | 68.8% | 69.4% | 67.9% | 54.3% | 49.5% | 61.5% | 58.7% |
| UNH | 49.2% | 51.0% | 51.2% | 44.5% | 55.4% | 49.4% | 53.2% | 46.9% |
| XOM | 60.3% | 59.8% | 60.3% | 51.1% | 57.0% | 50.5% | 58.4% | 50.8% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 230 | **51.7%** | 45.3%–58.2% | 49.6% | 47.0% | within noise | 0.2502 |
| Live, logistic, all sources (VADER) | 230 | **53.5%** | 47.0%–59.9% | 49.6% | 47.0% | within noise | 0.2508 |
| Live, logistic, all sources (FinBERT) | 230 | **54.3%** | 47.9%–60.8% | 49.6% | 47.0% | within noise | 0.2506 |
| Live, gradient boosting | 230 | **50.9%** | 44.4%–57.3% | 49.6% | 47.0% | within noise | 0.2503 |
| Live, ensemble | 230 | **53.0%** | 46.6%–59.5% | 49.6% | 47.0% | within noise | 0.2485 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 230 | **56.1%** | 49.7%–62.5% | 47.0% | 45.2% | within noise | 0.2487 |
| Live, gradient boosting | 230 | **53.9%** | 47.5%–60.4% | 47.0% | 45.2% | within noise | 0.2490 |
| Live, ensemble | 230 | **55.7%** | 49.2%–62.1% | 47.0% | 45.2% | within noise | 0.2472 |
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
| 45–48% | 50.7% (n=1,313) | 50.6% (n=1,260) | 50.6% (n=1,264) | 50.9% (n=1,141) | 48.9% (n=1,232) |
| 48–50% | 52.4% (n=1,335) | 55.2% (n=1,161) | 55.1% (n=1,157) | 50.2% (n=1,011) | 51.4% (n=1,171) |
| 50–52% | 52.5% (n=1,726) | 51.1% (n=1,254) | 51.2% (n=1,255) | 47.7% (n=1,135) | 53.7% (n=1,418) |
| 52–55% | 52.1% (n=2,352) | 51.8% (n=1,768) | 51.9% (n=1,766) | 52.3% (n=1,618) | 52.6% (n=2,011) |
| 55–60% | 52.8% (n=2,134) | 52.4% (n=2,115) | 52.4% (n=2,114) | 52.6% (n=1,553) | 54.6% (n=1,898) |
| 60% or more | 52.4% (n=647) | 53.4% (n=1,256) | 53.4% (n=1,256) | 54.9% (n=1,422) | 50.1% (n=817) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=956) | 49.7% (n=768) | 51.4% (n=428) |
| 40–45% | 46.7% (n=1,523) | 49.7% (n=1,260) | 47.2% (n=1,308) |
| 45–48% | 50.8% (n=1,459) | 49.9% (n=1,608) | 48.2% (n=1,724) |
| 48–50% | 49.5% (n=1,167) | 49.7% (n=1,486) | 51.3% (n=1,548) |
| 50–52% | 49.8% (n=1,202) | 50.7% (n=1,567) | 50.9% (n=1,487) |
| 52–55% | 52.4% (n=1,552) | 52.3% (n=1,575) | 50.9% (n=1,800) |
| 55–60% | 51.9% (n=1,681) | 50.0% (n=1,105) | 54.0% (n=1,322) |
| 60% or more | 52.8% (n=1,038) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.4 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 202 | 48.0% | -0.1% | 0.5% | -0.071 |
| FinBERT | 155 | 48.4% | -0.0% | 0.5% | -0.133 |

The two scorers agree on the direction of the mood on 70% of 240 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 23 | 47.8% | 60.9% | 56.5% | 26.1% | 43.5% | 65.2% |
| AMZN | 23 | 56.5% | 52.2% | 56.5% | 56.5% | 47.8% | 43.5% |
| GOOGL | 23 | 65.2% | 60.9% | 56.5% | 65.2% | 82.6% | 47.8% |
| JPM | 23 | 39.1% | 30.4% | 39.1% | 34.8% | 21.7% | 39.1% |
| META | 23 | 47.8% | 56.5% | 56.5% | 60.9% | 60.9% | 34.8% |
| MSFT | 23 | 43.5% | 47.8% | 47.8% | 60.9% | 47.8% | 52.2% |
| NVDA | 23 | 47.8% | 60.9% | 60.9% | 65.2% | 60.9% | 34.8% |
| TSLA | 23 | 47.8% | 56.5% | 56.5% | 39.1% | 43.5% | 56.5% |
| UNH | 23 | 52.2% | 43.5% | 43.5% | 60.9% | 52.2% | 52.2% |
| XOM | 23 | 69.6% | 65.2% | 69.6% | 39.1% | 69.6% | 69.6% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 23 | 65.2% | 39.1% | 69.6% | 60.9% |
| AMZN | 23 | 52.2% | 56.5% | 52.2% | 47.8% |
| GOOGL | 23 | 56.5% | 69.6% | 52.2% | 43.5% |
| JPM | 23 | 43.5% | 56.5% | 43.5% | 43.5% |
| META | 23 | 60.9% | 39.1% | 52.2% | 30.4% |
| MSFT | 23 | 60.9% | 60.9% | 60.9% | 52.2% |
| NVDA | 23 | 52.2% | 52.2% | 52.2% | 39.1% |
| TSLA | 23 | 56.5% | 52.2% | 56.5% | 47.8% |
| UNH | 23 | 52.2% | 56.5% | 56.5% | 43.5% |
| XOM | 23 | 60.9% | 56.5% | 60.9% | 60.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,058 | +43.0% | +8.9% | 0.52 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,058 | +41.3% | +8.6% | 0.53 | 50.5% |
| Top 3 by logistic, all sources (FinBERT) | 1,058 | +41.2% | +8.6% | 0.53 | 50.5% |
| Top 3 by gradient boosting | 999 | +69.8% | +14.3% | 0.78 | 36.8% |
| Top 3 by ensemble | 999 | +39.9% | +8.8% | 0.56 | 46.1% |
| Buy every stock, every session | 1,058 | -2.8% | -0.7% | 0.05 | 52.0% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,058 | -21.8% | -5.7% | -0.34 | 47.0% |
| Top 3 by gradient boosting | 999 | -43.4% | -13.4% | -0.82 | 39.2% |
| Top 3 by ensemble | 999 | -12.3% | -3.3% | -0.14 | 46.3% |
| Every stock minus SPY | 1,058 | -54.7% | -17.2% | -2.46 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7842 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 791 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 933 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| options | 10 | 0 | 20 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| stocktwits | 10 | 0 | 300 |  |
| yahoo_rss | 10 | 0 | 174 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-27 | 0 | 8 | 33 |
| MSFT | ok | 2026-10-27 | 0 | 8 | 62 |
| NVDA | ok | 2026-10-27 | 0 | 8 | 79 |
| AMZN | ok | 2026-10-27 | 0 | 8 | 43 |
| GOOGL | ok | 2026-10-27 | 0 | 8 | 55 |
| META | ok | 2026-10-27 | 0 | 8 | 64 |
| TSLA | ok | 2026-10-27 | 0 | 8 | 50 |
| JPM | ok | 2026-10-27 | 0 | 8 | 24 |
| XOM | ok | 2026-10-27 | 0 | 8 | 21 |
| UNH | ok | 2026-10-27 | 0 | 8 | 7 |

---

Educational project. Not financial advice.
