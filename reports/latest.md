# Stock prediction lab: latest report

Generated 2026-10-24 05:51 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **71.0%** | **Buy at open** | 67.0% | **Outperform** | 55 | neutral (-0.01) | negative (-0.28) |
| 2 | TSLA | **66.4%** | **Buy at open** | 64.3% | **Outperform** | 28 | positive (+0.09) | negative (-0.16) |
| 3 | MSFT | **60.1%** | **Buy at open** | 68.2% | **Outperform** | 32 | positive (+0.15) | positive (+0.09) |
| 4 | UNH | **53.9%** | Stay out | 46.9% | – | 7 | neutral (+0.05) | neutral (+0.03) |
| 5 | AMZN | **52.9%** | Stay out | 52.3% | – | 32 | positive (+0.11) | negative (-0.12) |
| 6 | AAPL | **50.1%** | Stay out | 43.9% | – | 36 | positive (+0.15) | positive (+0.17) |
| 7 | NVDA | **48.1%** | Stay out | 42.6% | – | 60 | positive (+0.06) | negative (-0.11) |
| 8 | JPM | **45.9%** | Stay out | 48.2% | – | 19 | positive (+0.10) | neutral (-0.04) |
| 9 | GOOGL | **38.3%** | Stay out | 39.5% | – | 27 | positive (+0.08) | neutral (-0.01) |
| 10 | XOM | **33.9%** | Stay out | 27.6% | – | 21 | positive (+0.26) | positive (+0.19) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 49.0% | 51.1% | 50.1% | 43.9% | 50.7% | 50.6% | 50.9% | 47.3% |
| AMZN | 52.2% | 52.0% | 52.9% | 52.3% | 58.6% | 50.5% | 55.3% | 51.4% |
| GOOGL | 47.4% | 39.3% | 38.3% | 39.5% | 50.9% | 50.2% | 45.1% | 44.9% |
| JPM | 51.3% | 46.3% | 45.9% | 48.2% | 53.6% | 50.5% | 49.9% | 49.3% |
| META | 63.1% | 72.7% | 71.0% | 67.0% | 53.9% | 50.8% | 63.3% | 58.9% |
| MSFT | 55.6% | 60.0% | 60.1% | 68.2% | 54.5% | 50.9% | 57.3% | 59.6% |
| NVDA | 45.0% | 48.1% | 48.1% | 42.6% | 55.0% | 48.6% | 51.5% | 45.6% |
| TSLA | 58.1% | 67.6% | 66.4% | 64.3% | 50.4% | 47.9% | 59.0% | 56.1% |
| UNH | 47.6% | 53.7% | 53.9% | 46.9% | 54.9% | 50.9% | 54.3% | 48.9% |
| XOM | 37.5% | 32.2% | 33.9% | 27.6% | 57.6% | 48.8% | 44.9% | 38.2% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 210 | **52.4%** | 45.6%–59.1% | 49.5% | 46.7% | within noise | 0.2487 |
| Live, logistic, all sources (VADER) | 210 | **55.7%** | 49.0%–62.4% | 49.5% | 46.7% | within noise | 0.2479 |
| Live, logistic, all sources (FinBERT) | 210 | **56.7%** | 50.0%–63.4% | 49.5% | 46.7% | within noise | 0.2478 |
| Live, gradient boosting | 210 | **51.9%** | 45.1%–58.7% | 49.5% | 46.7% | within noise | 0.2493 |
| Live, ensemble | 210 | **53.8%** | 47.1%–60.6% | 49.5% | 46.7% | within noise | 0.2465 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 210 | **57.1%** | 50.4%–63.8% | 47.6% | 43.8% | within noise | 0.2471 |
| Live, gradient boosting | 210 | **57.1%** | 50.4%–63.8% | 47.6% | 43.8% | within noise | 0.2484 |
| Live, ensemble | 210 | **56.7%** | 50.0%–63.4% | 47.6% | 43.8% | within noise | 0.2462 |
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
| under 40% | 53.1% (n=254) | 50.7% (n=633) | 50.7% (n=635) | 55.0% (n=1,050) | 52.1% (n=476) |
| 40–45% | 51.7% (n=815) | 51.6% (n=1,129) | 51.6% (n=1,129) | 53.9% (n=1,058) | 52.4% (n=964) |
| 45–48% | 50.8% (n=1,311) | 50.5% (n=1,259) | 50.5% (n=1,262) | 50.9% (n=1,141) | 49.0% (n=1,231) |
| 48–50% | 52.3% (n=1,334) | 55.1% (n=1,158) | 55.1% (n=1,155) | 50.1% (n=1,009) | 51.4% (n=1,170) |
| 50–52% | 52.5% (n=1,721) | 51.1% (n=1,253) | 51.1% (n=1,254) | 47.6% (n=1,132) | 53.6% (n=1,416) |
| 52–55% | 52.2% (n=2,347) | 51.9% (n=1,764) | 52.0% (n=1,762) | 52.4% (n=1,612) | 52.6% (n=2,005) |
| 55–60% | 52.7% (n=2,132) | 52.4% (n=2,113) | 52.4% (n=2,112) | 52.7% (n=1,544) | 54.7% (n=1,890) |
| 60% or more | 52.5% (n=644) | 53.5% (n=1,249) | 53.5% (n=1,249) | 54.9% (n=1,422) | 50.1% (n=816) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=954) | 49.7% (n=768) | 51.3% (n=427) |
| 40–45% | 46.7% (n=1,521) | 49.7% (n=1,260) | 47.2% (n=1,307) |
| 45–48% | 50.8% (n=1,458) | 49.9% (n=1,607) | 48.2% (n=1,722) |
| 48–50% | 49.5% (n=1,163) | 49.6% (n=1,483) | 51.3% (n=1,543) |
| 50–52% | 49.9% (n=1,201) | 51.0% (n=1,552) | 51.0% (n=1,484) |
| 52–55% | 52.5% (n=1,550) | 52.3% (n=1,574) | 50.9% (n=1,799) |
| 55–60% | 51.9% (n=1,680) | 50.0% (n=1,105) | 54.0% (n=1,315) |
| 60% or more | 52.8% (n=1,031) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 185 | 47.6% | -0.1% | 0.5% | -0.109 |
| FinBERT | 141 | 47.5% | -0.1% | 0.5% | -0.151 |

The two scorers agree on the direction of the mood on 70% of 220 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 21 | 47.6% | 57.1% | 52.4% | 23.8% | 38.1% | 61.9% |
| AMZN | 21 | 57.1% | 57.1% | 61.9% | 57.1% | 47.6% | 42.9% |
| GOOGL | 21 | 61.9% | 61.9% | 57.1% | 66.7% | 81.0% | 47.6% |
| JPM | 21 | 38.1% | 33.3% | 42.9% | 33.3% | 23.8% | 38.1% |
| META | 21 | 52.4% | 61.9% | 61.9% | 66.7% | 66.7% | 38.1% |
| MSFT | 21 | 42.9% | 47.6% | 47.6% | 61.9% | 47.6% | 52.4% |
| NVDA | 21 | 52.4% | 66.7% | 66.7% | 66.7% | 61.9% | 33.3% |
| TSLA | 21 | 42.9% | 52.4% | 52.4% | 38.1% | 38.1% | 52.4% |
| UNH | 21 | 52.4% | 47.6% | 47.6% | 66.7% | 57.1% | 57.1% |
| XOM | 21 | 76.2% | 71.4% | 76.2% | 38.1% | 76.2% | 71.4% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 21 | 61.9% | 38.1% | 66.7% | 61.9% |
| AMZN | 21 | 57.1% | 57.1% | 57.1% | 47.6% |
| GOOGL | 21 | 57.1% | 71.4% | 52.4% | 42.9% |
| JPM | 21 | 42.9% | 61.9% | 42.9% | 47.6% |
| META | 21 | 66.7% | 42.9% | 57.1% | 33.3% |
| MSFT | 21 | 61.9% | 61.9% | 61.9% | 52.4% |
| NVDA | 21 | 57.1% | 57.1% | 57.1% | 38.1% |
| TSLA | 21 | 52.4% | 57.1% | 52.4% | 42.9% |
| UNH | 21 | 47.6% | 61.9% | 52.4% | 47.6% |
| XOM | 21 | 66.7% | 61.9% | 66.7% | 61.9% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,056 | +43.1% | +8.9% | 0.52 | 51.0% |
| Top 3 by logistic, all sources (VADER) | 1,056 | +40.8% | +8.5% | 0.52 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,056 | +40.7% | +8.5% | 0.52 | 50.4% |
| Top 3 by gradient boosting | 997 | +65.8% | +13.6% | 0.76 | 36.6% |
| Top 3 by ensemble | 997 | +38.6% | +8.6% | 0.55 | 46.0% |
| Buy every stock, every session | 1,056 | -2.9% | -0.7% | 0.05 | 51.9% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,056 | -22.3% | -5.9% | -0.35 | 47.0% |
| Top 3 by gradient boosting | 997 | -43.3% | -13.4% | -0.82 | 39.3% |
| Top 3 by ensemble | 997 | -13.0% | -3.5% | -0.15 | 46.3% |
| Every stock minus SPY | 1,056 | -54.4% | -17.1% | -2.44 | 42.1% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7835 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 7 | 0 | 34 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 0 | 10 | 0 | HTTPError: 503 Server Error: Service Unavailable for url: https://news.google.com/rss/search?q=UNH+stock&hl=en-US&gl=US&ceid=US:en |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 0 | 10 | 0 | HTTPError: 503 Server Error: Service Unavailable for url: https://news.google.com/rss/search?q=%28unh+OR+unitedhealth%29+%28site%3Areuters.com+OR+site%3Abloomberg.com+OR+site%3Acnbc.com+OR+site%3Awsj. |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 165 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-10-23 | 0 | 0 | 0 |
| MSFT | ok | 2026-10-23 | 0 | 0 | 0 |
| NVDA | ok | 2026-10-23 | 0 | 0 | 0 |
| AMZN | ok | 2026-10-23 | 0 | 0 | 0 |
| GOOGL | ok | 2026-10-23 | 0 | 0 | 0 |
| META | ok | 2026-10-23 | 0 | 0 | 0 |
| TSLA | ok | 2026-10-23 | 0 | 0 | 0 |
| JPM | ok | 2026-10-23 | 0 | 0 | 0 |
| XOM | ok | 2026-10-23 | 0 | 0 | 0 |
| UNH | ok | 2026-10-23 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
