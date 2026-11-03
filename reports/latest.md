# Stock prediction lab: latest report

Generated 2026-11-03 07:55 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | META | **59.0%** | **Buy at open** | 56.9% | **Outperform** | 37 | neutral (+0.01) | negative (-0.33) |
| 2 | AMZN | **57.4%** | **Buy at open** | 51.2% | – | 56 | positive (+0.13) | neutral (+0.04) |
| 3 | TSLA | **55.1%** | **Buy at open** | 58.6% | **Outperform** | 30 | positive (+0.11) | positive (+0.18) |
| 4 | NVDA | **55.1%** | Stay out | 54.8% | – | 57 | neutral (+0.02) | neutral (-0.02) |
| 5 | GOOGL | **54.1%** | Stay out | 64.7% | **Outperform** | 38 | negative (-0.10) | negative (-0.15) |
| 6 | UNH | **52.8%** | Stay out | 44.5% | – | 17 | positive (+0.12) | positive (+0.13) |
| 7 | XOM | **51.7%** | Stay out | 45.9% | – | 48 | positive (+0.13) | positive (+0.14) |
| 8 | JPM | **48.7%** | Stay out | 44.2% | – | 22 | positive (+0.24) | positive (+0.20) |
| 9 | MSFT | **48.0%** | Stay out | 43.1% | – | 38 | positive (+0.14) | neutral (+0.00) |
| 10 | AAPL | **47.2%** | Stay out | 52.8% | – | 73 | positive (+0.08) | negative (-0.10) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 47.3% | 48.9% | 49.3% | 52.8% | 45.5% | 48.1% | 47.2% | 50.4% |
| AMZN | 53.9% | 61.4% | 59.9% | 51.2% | 53.4% | 50.3% | 57.4% | 50.8% |
| GOOGL | 52.6% | 54.4% | 55.7% | 64.7% | 53.8% | 51.8% | 54.1% | 58.3% |
| JPM | 47.6% | 45.0% | 47.6% | 44.2% | 52.4% | 49.8% | 48.7% | 47.0% |
| META | 58.7% | 62.3% | 62.1% | 56.9% | 55.7% | 51.8% | 59.0% | 54.3% |
| MSFT | 42.4% | 41.6% | 42.6% | 43.1% | 54.4% | 50.0% | 48.0% | 46.6% |
| NVDA | 48.3% | 54.4% | 55.2% | 54.8% | 55.7% | 51.8% | 55.1% | 53.3% |
| TSLA | 48.2% | 59.5% | 59.9% | 58.6% | 50.6% | 49.8% | 55.1% | 54.2% |
| UNH | 54.0% | 52.3% | 52.2% | 44.5% | 53.2% | 50.0% | 52.8% | 47.3% |
| XOM | 52.8% | 51.6% | 51.9% | 45.9% | 51.9% | 50.0% | 51.7% | 48.0% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 270 | **52.2%** | 46.3%–58.2% | 46.7% | 47.8% | no | 0.2491 |
| Live, logistic, all sources (VADER) | 270 | **54.1%** | 48.1%–60.0% | 46.7% | 47.8% | within noise | 0.2517 |
| Live, logistic, all sources (FinBERT) | 270 | **54.4%** | 48.5%–60.4% | 46.7% | 47.8% | within noise | 0.2509 |
| Live, gradient boosting | 270 | **51.5%** | 45.5%–57.4% | 46.7% | 47.8% | no | 0.2496 |
| Live, ensemble | 270 | **53.3%** | 47.4%–59.3% | 46.7% | 47.8% | no | 0.2487 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 270 | **55.2%** | 49.3%–61.1% | 45.9% | 45.6% | within noise | 0.2511 |
| Live, gradient boosting | 270 | **54.4%** | 48.5%–60.4% | 45.9% | 45.6% | within noise | 0.2490 |
| Live, ensemble | 270 | **55.2%** | 49.3%–61.1% | 45.9% | 45.6% | within noise | 0.2483 |
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
| under 40% | 53.1% (n=256) | 50.5% (n=639) | 50.5% (n=641) | 55.0% (n=1,055) | 51.9% (n=480) |
| 40–45% | 51.5% (n=823) | 51.6% (n=1,130) | 51.5% (n=1,131) | 53.7% (n=1,063) | 52.3% (n=968) |
| 45–48% | 50.6% (n=1,319) | 50.4% (n=1,266) | 50.4% (n=1,270) | 50.8% (n=1,145) | 48.9% (n=1,237) |
| 48–50% | 52.3% (n=1,341) | 55.0% (n=1,165) | 55.0% (n=1,163) | 50.0% (n=1,017) | 51.2% (n=1,175) |
| 50–52% | 52.5% (n=1,734) | 51.1% (n=1,261) | 51.1% (n=1,261) | 47.5% (n=1,140) | 53.5% (n=1,426) |
| 52–55% | 51.9% (n=2,360) | 51.7% (n=1,773) | 51.8% (n=1,770) | 52.3% (n=1,624) | 52.6% (n=2,019) |
| 55–60% | 52.8% (n=2,136) | 52.4% (n=2,124) | 52.4% (n=2,120) | 52.6% (n=1,562) | 54.5% (n=1,905) |
| 60% or more | 52.4% (n=649) | 53.3% (n=1,260) | 53.2% (n=1,262) | 54.9% (n=1,422) | 50.0% (n=818) |
| **Average gap** | **4.0 pts** | **5.5 pts** | **5.5 pts** | **7.0 pts** | **4.3 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.3% (n=961) | 49.7% (n=768) | 51.2% (n=430) |
| 40–45% | 46.7% (n=1,533) | 49.7% (n=1,260) | 47.3% (n=1,312) |
| 45–48% | 50.6% (n=1,465) | 49.8% (n=1,615) | 48.0% (n=1,737) |
| 48–50% | 49.7% (n=1,170) | 49.6% (n=1,506) | 51.4% (n=1,554) |
| 50–52% | 49.9% (n=1,207) | 50.7% (n=1,580) | 50.9% (n=1,492) |
| 52–55% | 52.4% (n=1,553) | 52.3% (n=1,575) | 50.9% (n=1,806) |
| 55–60% | 51.9% (n=1,687) | 50.0% (n=1,105) | 53.9% (n=1,325) |
| 60% or more | 52.6% (n=1,042) | 51.1% (n=619) | 50.5% (n=372) |
| **Average gap** | **4.6 pts** | **4.3 pts** | **3.1 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 232 | 47.0% | -0.2% | -0.2% | -0.054 |
| FinBERT | 184 | 48.4% | -0.1% | 0.2% | -0.083 |

The two scorers agree on the direction of the mood on 69% of 280 stock-days with headlines.

## Per stock: up or down?

Based on live predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 27 | 48.1% | 59.3% | 55.6% | 29.6% | 44.4% | 59.3% |
| AMZN | 27 | 55.6% | 55.6% | 55.6% | 51.9% | 48.1% | 48.1% |
| GOOGL | 27 | 66.7% | 59.3% | 59.3% | 70.4% | 81.5% | 44.4% |
| JPM | 27 | 44.4% | 37.0% | 44.4% | 37.0% | 29.6% | 37.0% |
| META | 27 | 44.4% | 55.6% | 51.9% | 63.0% | 59.3% | 37.0% |
| MSFT | 27 | 51.9% | 55.6% | 55.6% | 63.0% | 51.9% | 44.4% |
| NVDA | 27 | 48.1% | 55.6% | 55.6% | 59.3% | 55.6% | 29.6% |
| TSLA | 27 | 48.1% | 55.6% | 55.6% | 37.0% | 44.4% | 51.9% |
| UNH | 27 | 44.4% | 40.7% | 40.7% | 59.3% | 51.9% | 48.1% |
| XOM | 27 | 70.4% | 66.7% | 70.4% | 44.4% | 66.7% | 66.7% |

## Per stock: beats the market?

Based on live predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 27 | 59.3% | 40.7% | 66.7% | 59.3% |
| AMZN | 27 | 48.1% | 59.3% | 48.1% | 51.9% |
| GOOGL | 27 | 55.6% | 70.4% | 51.9% | 44.4% |
| JPM | 27 | 44.4% | 59.3% | 44.4% | 44.4% |
| META | 27 | 59.3% | 33.3% | 51.9% | 33.3% |
| MSFT | 27 | 59.3% | 59.3% | 59.3% | 48.1% |
| NVDA | 27 | 51.9% | 48.1% | 51.9% | 33.3% |
| TSLA | 27 | 51.9% | 51.9% | 51.9% | 48.1% |
| UNH | 27 | 59.3% | 63.0% | 63.0% | 37.0% |
| XOM | 27 | 63.0% | 59.3% | 63.0% | 59.3% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,062 | +40.3% | +8.4% | 0.50 | 50.9% |
| Top 3 by logistic, all sources (VADER) | 1,062 | +38.7% | +8.1% | 0.50 | 50.4% |
| Top 3 by logistic, all sources (FinBERT) | 1,062 | +40.3% | +8.4% | 0.52 | 50.4% |
| Top 3 by gradient boosting | 1,003 | +64.8% | +13.4% | 0.75 | 36.7% |
| Top 3 by ensemble | 1,003 | +35.7% | +8.0% | 0.51 | 46.0% |
| Buy every stock, every session | 1,062 | -5.3% | -1.3% | 0.01 | 51.8% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,062 | -23.2% | -6.1% | -0.37 | 46.9% |
| Top 3 by gradient boosting | 1,003 | -43.4% | -13.3% | -0.82 | 39.1% |
| Top 3 by ensemble | 1,003 | -13.1% | -3.5% | -0.15 | 46.3% |
| Every stock minus SPY | 1,062 | -55.3% | -17.4% | -2.49 | 42.0% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7827 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 10 | 0 | 187 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 966 |  |
| macro_yahoo | 1 | 0 | 1089 |  |
| major_news | 10 | 0 | 1000 |  |
| prices | 11 | 0 | 11957 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 177 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-11-02 | 0 | 0 | 0 |
| MSFT | ok | 2026-11-02 | 0 | 0 | 0 |
| NVDA | ok | 2026-11-02 | 0 | 0 | 0 |
| AMZN | ok | 2026-11-02 | 0 | 0 | 0 |
| GOOGL | ok | 2026-11-02 | 0 | 0 | 0 |
| META | ok | 2026-11-02 | 0 | 0 | 0 |
| TSLA | ok | 2026-11-02 | 0 | 0 | 0 |
| JPM | ok | 2026-11-02 | 0 | 0 | 0 |
| XOM | ok | 2026-11-02 | 0 | 0 | 0 |
| UNH | ok | 2026-11-02 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
