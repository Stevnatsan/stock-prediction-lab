# Stock prediction lab: latest report

Generated 2026-09-26 06:10 UTC.

## Next-session calls

| Rank | Stock | P(up) | Call | P(beats SPY) | vs the market | Headlines (24 h) | Mood: VADER | Mood: FinBERT |
|---|---|---|---|---|---|---|---|---|
| 1 | XOM | **58.2%** | **Buy at open** | 66.7% | **Outperform** | 11 | positive (+0.22) | neutral (+0.03) |
| 2 | AAPL | **54.6%** | **Buy at open** | 58.7% | **Outperform** | 33 | positive (+0.18) | positive (+0.20) |
| 3 | JPM | **53.9%** | **Buy at open** | 58.6% | **Outperform** | 31 | positive (+0.28) | neutral (+0.01) |
| 4 | AMZN | **52.3%** | Stay out | 47.6% | – | 55 | positive (+0.16) | neutral (-0.04) |
| 5 | TSLA | **51.7%** | Stay out | 53.5% | – | 32 | positive (+0.06) | neutral (-0.00) |
| 6 | UNH | **51.3%** | Stay out | 44.7% | – | 8 | positive (+0.13) | positive (+0.45) |
| 7 | GOOGL | **50.5%** | Stay out | 45.9% | – | 36 | positive (+0.08) | positive (+0.08) |
| 8 | NVDA | **48.9%** | Stay out | 46.5% | – | 72 | positive (+0.14) | neutral (+0.03) |
| 9 | META | **42.1%** | Stay out | 42.3% | – | 78 | positive (+0.12) | neutral (+0.02) |
| 10 | MSFT | **38.8%** | Stay out | 41.7% | – | 35 | positive (+0.15) | positive (+0.17) |

Every model's probability:

| Stock | P(up): logistic, price only | P(up): logistic, all sources (VADER) | P(up): logistic, all sources (FinBERT) | P(beats SPY): logistic, all sources (VADER) | P(up): gradient boosting | P(beats SPY): gradient boosting | P(up): ensemble | P(beats SPY): ensemble |
|---|---|---|---|---|---|---|---|---|
| AAPL | 57.8% | 56.1% | 56.1% | 58.7% | 53.1% | 49.7% | 54.6% | 54.2% |
| AMZN | 54.5% | 48.1% | 48.1% | 47.6% | 56.6% | 50.3% | 52.3% | 48.9% |
| GOOGL | 58.0% | 49.6% | 49.6% | 45.9% | 51.5% | 50.3% | 50.5% | 48.1% |
| JPM | 55.5% | 50.8% | 50.8% | 58.6% | 56.9% | 49.7% | 53.9% | 54.1% |
| META | 40.8% | 34.4% | 34.4% | 42.3% | 49.7% | 49.5% | 42.1% | 45.9% |
| MSFT | 47.6% | 29.1% | 29.1% | 41.7% | 48.5% | 49.7% | 38.8% | 45.7% |
| NVDA | 54.1% | 45.8% | 45.8% | 46.5% | 52.0% | 50.7% | 48.9% | 48.6% |
| TSLA | 55.8% | 52.7% | 52.7% | 53.5% | 50.7% | 50.7% | 51.7% | 52.1% |
| UNH | 49.7% | 46.0% | 46.0% | 44.7% | 56.6% | 50.3% | 51.3% | 47.5% |
| XOM | 61.4% | 64.7% | 64.7% | 66.7% | 51.7% | 50.7% | 58.2% | 58.7% |

## Accuracy: up or down?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, price only | 10 | **80.0%** | 55.2%–104.8% | 70.0% | 50.0% | within noise | 0.2141 |
| Live, logistic, all sources (VADER) | 10 | **70.0%** | 41.6%–98.4% | 70.0% | 50.0% | no | 0.2362 |
| Live, logistic, all sources (FinBERT) | 10 | **70.0%** | 41.6%–98.4% | 70.0% | 50.0% | no | 0.2362 |
| Live, gradient boosting | 10 | **80.0%** | 55.2%–104.8% | 70.0% | 50.0% | within noise | 0.2253 |
| Live, ensemble | 10 | **80.0%** | 55.2%–104.8% | 70.0% | 50.0% | within noise | 0.2291 |
| Historical replay, logistic, price only | 10,348 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no | 0.2523 |
| Historical replay, logistic, all sources (VADER) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, logistic, all sources (FinBERT) | 10,348 | **50.4%** | 49.4%–51.4% | 52.2% | 49.8% | no | 0.2544 |
| Historical replay, gradient boosting | 9,758 | **50.1%** | 49.1%–51.1% | 52.4% | 49.8% | no | 0.2592 |
| Historical replay, ensemble | 9,758 | **51.5%** | 50.5%–52.5% | 52.4% | 49.8% | no | 0.2533 |

## Accuracy: beats the market?

| | Predictions | Accuracy | 95% range | Always beats | Same as today | Beats baselines? | Brier |
|---|---|---|---|---|---|---|---|
| Live, logistic, all sources (VADER) | 10 | **90.0%** | 71.4%–108.6% | 40.0% | 40.0% | yes | 0.2122 |
| Live, gradient boosting | 10 | **60.0%** | 29.6%–90.4% | 40.0% | 40.0% | no | 0.2495 |
| Live, ensemble | 10 | **80.0%** | 55.2%–104.8% | 40.0% | 40.0% | within noise | 0.2296 |
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
| under 40% | 52.8% (n=246) | 50.7% (n=605) | 50.7% (n=605) | 55.0% (n=1,049) | 52.0% (n=473) |
| 40–45% | 52.0% (n=791) | 52.0% (n=1,085) | 52.0% (n=1,085) | 54.5% (n=1,024) | 53.0% (n=922) |
| 45–48% | 50.7% (n=1,284) | 50.5% (n=1,236) | 50.5% (n=1,236) | 50.6% (n=1,097) | 49.0% (n=1,186) |
| 48–50% | 52.6% (n=1,306) | 55.5% (n=1,136) | 55.5% (n=1,136) | 50.3% (n=966) | 51.3% (n=1,140) |
| 50–52% | 52.5% (n=1,694) | 51.1% (n=1,238) | 51.1% (n=1,238) | 47.4% (n=1,092) | 53.8% (n=1,387) |
| 52–55% | 52.4% (n=2,303) | 52.0% (n=1,741) | 52.0% (n=1,741) | 52.6% (n=1,583) | 52.7% (n=1,975) |
| 55–60% | 52.6% (n=2,096) | 52.3% (n=2,086) | 52.3% (n=2,086) | 52.7% (n=1,535) | 54.6% (n=1,873) |
| 60% or more | 52.4% (n=638) | 53.2% (n=1,231) | 53.2% (n=1,231) | 54.9% (n=1,422) | 50.0% (n=812) |
| **Average gap** | **4.1 pts** | **5.5 pts** | **5.5 pts** | **7.1 pts** | **4.4 pts** |

**Beats the market?**

| Predicted | Logistic, all sources (VADER) | Gradient boosting | Ensemble |
|---|---|---|---|
| under 40% | 48.7% (n=927) | 49.7% (n=768) | 51.2% (n=426) |
| 40–45% | 46.9% (n=1,483) | 49.7% (n=1,260) | 47.6% (n=1,276) |
| 45–48% | 50.8% (n=1,430) | 50.1% (n=1,586) | 48.3% (n=1,678) |
| 48–50% | 49.7% (n=1,145) | 50.1% (n=1,386) | 51.4% (n=1,504) |
| 50–52% | 49.9% (n=1,185) | 50.6% (n=1,473) | 50.9% (n=1,450) |
| 52–55% | 52.2% (n=1,519) | 52.3% (n=1,571) | 51.0% (n=1,770) |
| 55–60% | 52.1% (n=1,659) | 50.0% (n=1,105) | 53.9% (n=1,293) |
| 60% or more | 52.7% (n=1,010) | 51.1% (n=619) | 50.7% (n=371) |
| **Average gap** | **4.7 pts** | **4.5 pts** | **3.2 pts** |

![Calibration](calibration.png)

## Headline sentiment: VADER vs FinBERT

Every headline is scored by both. Two ways to compare them: the live accuracy of the two otherwise identical logistic models above (*all sources (VADER)* vs *all sources (FinBERT)*), and directly, below: does the mood predict the next session?

| Scorer | Stock-days with a clear mood | Mood matched the next session | Next-session return: positive mood | negative mood | Rank correlation with return |
|---|---|---|---|---|---|
| VADER | 8 | 62.5% | -0.3% | – | +0.357 |
| FinBERT | 7 | 42.9% | -1.2% | 0.2% | +0.036 |

The two scorers agree on the direction of the mood on 75% of 20 stock-days with headlines.

## Per stock: up or down?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, price only | Logistic, all sources (VADER) | Logistic, all sources (FinBERT) | Gradient boosting | Ensemble | Always up |
|---|---|---|---|---|---|---|---|
| AAPL | 1,036 | 51.4% | 49.4% | 49.4% | 48.7% | 50.6% | 54.4% |
| AMZN | 1,036 | 49.6% | 50.0% | 50.0% | 49.1% | 49.1% | 50.9% |
| GOOGL | 1,036 | 51.4% | 49.3% | 49.3% | 51.2% | 52.0% | 54.3% |
| JPM | 1,036 | 50.9% | 50.9% | 50.9% | 51.2% | 51.3% | 54.1% |
| META | 1,036 | 52.7% | 52.6% | 52.6% | 48.8% | 51.0% | 50.8% |
| MSFT | 1,036 | 51.8% | 52.0% | 52.0% | 49.8% | 52.2% | 51.9% |
| NVDA | 1,036 | 49.4% | 49.6% | 49.6% | 51.6% | 51.7% | 53.0% |
| TSLA | 1,036 | 53.2% | 53.3% | 53.3% | 49.8% | 52.7% | 49.8% |
| UNH | 1,035 | 50.1% | 48.7% | 48.7% | 49.8% | 52.0% | 51.4% |
| XOM | 1,035 | 49.4% | 48.3% | 48.3% | 51.5% | 52.9% | 51.9% |

## Per stock: beats the market?

Based on all scored (mostly historical replay) predictions.

| Stock | Sessions | Logistic, all sources (VADER) | Gradient boosting | Ensemble | Always beats |
|---|---|---|---|---|---|
| AAPL | 1,036 | 51.0% | 51.1% | 51.4% | 53.1% |
| AMZN | 1,036 | 49.2% | 52.6% | 50.7% | 47.9% |
| GOOGL | 1,036 | 49.9% | 51.4% | 50.7% | 53.5% |
| JPM | 1,036 | 52.7% | 49.0% | 49.9% | 53.5% |
| META | 1,036 | 51.3% | 48.2% | 50.2% | 49.0% |
| MSFT | 1,036 | 50.9% | 50.2% | 50.2% | 48.8% |
| NVDA | 1,036 | 51.9% | 52.4% | 52.8% | 52.3% |
| TSLA | 1,036 | 52.6% | 51.5% | 53.6% | 48.8% |
| UNH | 1,035 | 53.5% | 50.2% | 51.5% | 47.6% |
| XOM | 1,035 | 51.0% | 49.3% | 51.0% | 49.5% |

## Paper trading (simulated from prices)

Hypothetical: each session a strategy buys, at the open, the (up to) 3 stocks its model rates highest with P ≥ 52%, and sells them at the close, paying 5 bp per trade. The *beats the market* version also shorts the same amount of SPY, so it only earns the stocks' return above the market's (two trades, double cost).

**Up or down**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, price only | 1,036 | +35.3% | +7.6% | 0.46 | 50.7% |
| Top 3 by logistic, all sources (VADER) | 1,036 | +33.9% | +7.4% | 0.47 | 50.0% |
| Top 3 by logistic, all sources (FinBERT) | 1,036 | +33.9% | +7.4% | 0.47 | 50.0% |
| Top 3 by gradient boosting | 977 | +68.3% | +14.4% | 0.79 | 37.1% |
| Top 3 by ensemble | 977 | +36.2% | +8.3% | 0.53 | 45.9% |
| Buy every stock, every session | 1,036 | +0.5% | +0.1% | 0.09 | 52.1% |

**Beats the market (market-neutral)**

| Strategy | Sessions | Total return | Per year | Sharpe | Winning days |
|---|---|---|---|---|---|
| Top 3 by logistic, all sources (VADER) | 1,036 | -24.6% | -6.6% | -0.41 | 46.7% |
| Top 3 by gradient boosting | 977 | -40.7% | -12.6% | -0.76 | 40.1% |
| Top 3 by ensemble | 977 | -15.7% | -4.3% | -0.20 | 46.2% |
| Every stock minus SPY | 1,036 | -52.9% | -16.7% | -2.37 | 42.3% |

![Paper trading](paper_trading.png)

## Paper orders at Alpaca (real fills)

No paper orders yet. Connect an Alpaca paper account (see the README) and the champion's picks are sent as real simulated orders every session.

## Data sources this run

| Source | Calls ok | Failed | Items | Note |
|---|---|---|---|---|
| alpaca | 0 | 0 | 0 | skipped: set ALPACA_API_KEY and ALPACA_SECRET_KEY to enable |
| analysts | 10 | 0 | 7670 |  |
| earnings | 10 | 0 | 500 |  |
| finbert | 9 | 0 | 70 |  |
| finnhub | 0 | 0 | 0 | skipped: set FINNHUB_API_KEY to enable |
| fred | 0 | 1 | 0 | ReadTimeout: HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20) |
| google_news | 10 | 0 | 993 |  |
| macro_yahoo | 1 | 0 | 1087 |  |
| prices | 11 | 0 | 11935 |  |
| reddit | 0 | 0 | 0 | skipped: set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to enable |
| sec_filings | 0 | 0 | 0 | skipped: set SEC_USER_AGENT to enable |
| yahoo_rss | 10 | 0 | 182 |  |

## This run, per stock

| Stock | Status | Data through | History replayed | Scored today | Headlines (24 h) |
|---|---|---|---|---|---|
| AAPL | ok | 2026-09-25 | 0 | 0 | 0 |
| MSFT | ok | 2026-09-25 | 0 | 0 | 0 |
| NVDA | ok | 2026-09-25 | 0 | 0 | 0 |
| AMZN | ok | 2026-09-25 | 0 | 0 | 0 |
| GOOGL | ok | 2026-09-25 | 0 | 0 | 0 |
| META | ok | 2026-09-25 | 0 | 0 | 0 |
| TSLA | ok | 2026-09-25 | 0 | 0 | 0 |
| JPM | ok | 2026-09-25 | 0 | 0 | 0 |
| XOM | ok | 2026-09-25 | 0 | 0 | 0 |
| UNH | ok | 2026-09-25 | 0 | 0 | 0 |

---

Educational project. Not financial advice.
