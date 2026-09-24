# Stock prediction lab

**A self-updating quant experiment: four models compete to predict whether the US stocks you choose will rise in their next trading session. It learns from every right and wrong call, paper-trades the best model's top picks, and publishes its full track record, including when it's no better than a coin flip.**

> Educational project, not financial advice. It only paper-trades: no real orders are ever placed.

## Live scoreboard

<!-- scoreboard:start -->
**Updated:** 2026-09-24 15:29 UTC

### Next-session calls

Will each stock close above its opening price in the next session? Calls use the **champion**: whichever of the four models was most accurate over the last 120 sessions (now: logistic, price + news). **Buy at open** marks the (up to) 3 highest-rated stocks with P(up) ≥ 52%: the paper-trading strategy.

No open calls right now. New ones are made after each US market close.

### Which model is winning?

| Model | Accuracy, last 120 sessions |
|---|---|
| **Logistic, price + news (champion)** | 50.3% |
| Logistic, price only | 50.3% |

### How accurate has it been?

| | Predictions | Accuracy | 95% range | Always up | Same as today | Beats baselines? |
|---|---|---|---|---|---|---|
| Historical replay, logistic, price + news | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |
| Historical replay, logistic, price only | 10,338 | **51.0%** | 50.0%–51.9% | 52.2% | 49.8% | no |

Any model has to beat three simple rules: always predict up (*Always up* is the share of sessions that rose), always predict down, and predict the same direction as today (*Same as today*). *Beats baselines* is only "yes" when the whole 95% range is above all three.

![Rolling accuracy](reports/rolling_accuracy.png)

Full report, with per-stock results, paper trading and source health: [reports/latest.md](reports/latest.md)
<!-- scoreboard:end -->

## How it works

Every weekday after the US market closes, GitHub Actions runs `python -m stocklab daily`, which:

1. **Collects** today's prices, headlines and company filings from every source below.
2. **Scores yesterday.** Each earlier prediction is checked against how that session actually went.
3. **Learns.** The online models are updated with the inputs they used and the real outcome. The update is proportional to the error, so a confident wrong call (say 90% "up" on a day the stock fell) changes the model about 9× more than a confident right one: **wrong predictions are the biggest lessons.** Gradient boosting is retrained on every finished session.
4. **Predicts the next session** for every stock with all four models, and makes the calls with the recent **champion**.
5. **Publishes** the calls, the accuracy so far and the charts to this README and [`reports/latest.md`](reports/latest.md), then commits every prediction, headline and model weight to the repo.

The first time it sees a stock, it replays about 4 years of that stock's history through the same predict → score → learn loop, so each model starts with experience rather than from zero.

## Data sources

| Source | What it provides | Needs |
|---|---|---|
| Yahoo Finance (via `yfinance`) | Daily open, high, low, close and volume for each stock and for SPY (the market) | nothing |
| Yahoo Finance RSS | Latest headlines for each stock | nothing |
| Google News RSS | Headlines matching "<ticker> stock" | nothing |
| SEC EDGAR | 8-K filings, which companies must file for material events | `SEC_USER_AGENT` (your name and email, SEC policy) |
| Finnhub | Company news | `FINNHUB_API_KEY` (free tier) |

Sources without their key are skipped automatically. Any source that fails on a given day is logged in the report and skipped, so one broken feed never stops the run.

## What the model looks at

| Price features (known at today's close) | News features (collected tonight) |
|---|---|
| returns over 1, 5 and 20 days · 20-day volatility · RSI · distance from the 50-day average · volume vs normal · overnight gap · today's open → close move · market (SPY) returns | average headline sentiment (24 h) · number of headlines · 3-day sentiment trend · any news at all? · recent SEC 8-K filings |

Headline sentiment uses VADER with an added finance vocabulary ("beats", "downgrade", "recall", "lawsuit"…).

## The models

Four models make a prediction for every stock, every day, and are scored the same way:

| Model | How it works | Why it's here |
|---|---|---|
| **Logistic, price + news** | Online logistic regression, one per stock, updated after every session. | Simple, transparent, adapts quickly. |
| **Logistic, price only** | The same model without the news features. | Shows whether news actually helps, rather than assuming it does. |
| **Gradient boosting** | Hundreds of small decision trees (`HistGradientBoostingClassifier`), trained on all watched stocks pooled together and retrained on every finished session. | Catches non-linear patterns, such as "a big drop only matters when volatility is low". |
| **Ensemble** | The average of the two main models' probabilities. | Averaging different models often beats each one alone. |

**The champion makes the calls.** Whichever model was most accurate over the last 120 sessions is used for tonight's calls, so the bot switches to a better model automatically when one starts winning.

**The quant strategy (paper trading).** Each session, rank the stocks by the champion's P(up) and buy, at the open, the top 3 with P(up) ≥ 52%, then sell at the close. The report tracks every model's version of this strategy against simply buying everything, with total return, yearly return and Sharpe ratio after trading costs.

## Choose your stocks

The watchlist starts with 10 large stocks. Any of the **503 S&P 500 companies** in [`STOCKS.md`](STOCKS.md) (grouped by sector) can be added, up to 40 at a time:

1. Open **Actions → choose stocks → Run workflow**.
2. Type symbols to **add** (e.g. `KO, PEP, BRK-B`) and/or **remove** (e.g. `TSLA`), then click **Run workflow**.
3. The bot updates [`config.yaml`](config.yaml), learns each new stock's last 4 years, and includes it in every daily prediction from the next close.

Symbols outside the S&P 500 (other US stocks or ETFs such as `QQQ`) also work if Yahoo Finance has them.

## About "live" prices

The bot trains on **actual traded prices**: every open and close comes from real trades on US exchanges (via Yahoo Finance), refreshed after every close. It works with daily prices on purpose, because it predicts whole sessions and runs once a day for free. Real-time tick data would need a broker or paid data feed (for example a free Alpaca paper-trading account), which could be added later to place simulated orders with real fills.

## Why not keep training until the accuracy is high?

It's the obvious idea, and it's the trap most trading-bot projects fall into:

- **Retraining on the same history until the score looks good just memorises those days.** The score goes up; accuracy on the next, unseen day doesn't. This is overfitting.
- **Backtests that show 70–90% accuracy almost always have a bug** where the model can see information that didn't exist yet at prediction time (lookahead).
- **Real daily stock moves are very close to a coin flip.** A genuine, repeatable edge of a few percentage points is already valuable, because it applies to thousands of decisions.

So the lab does it differently:

- It **keeps learning from every new outcome**, forever. That's the "if it's wrong, take it as training" idea, done safely.
- It **never grades itself on data it has already learned from**: every prediction is recorded before the answer is known.
- Success means **beating simple rules by more than luck would explain**: always predicting up, always predicting down, or repeating today's direction. Every accuracy figure comes with a 95% range.

The tests check this honestly for both kinds of model. On a simulated random market they score 50% (no hidden leaks); when a real pattern is planted in the simulated data, they find it and reach about 70%.

## How to access the project

### See the results (nothing to install)

- **This README:** the scoreboard above updates after every US trading day.
- **Full report:** [`reports/latest.md`](reports/latest.md) has per-stock accuracy, paper trading and data-source health.
- **Raw history:** every prediction ever made is in [`state/predictions.csv`](state/predictions.csv), model weights are in [`state/models/`](state/models), and collected headlines are in [`state/news/`](state/news).

### Start it on GitHub (automatic daily runs)

1. Use this repository (or your fork), open the **Actions** tab, and enable workflows if GitHub asks.
2. *Optional:* under **Settings → Secrets and variables → Actions**, add `SEC_USER_AGENT` (e.g. `Jane Doe jane@example.com`) and/or `FINNHUB_API_KEY`.
3. Open **Actions → daily predictions → Run workflow**. The first run downloads history and replays it, which takes a few minutes.
4. From then on it runs automatically every weekday at 22:15 UTC, after the US close. If GitHub ever pauses the schedule, re-enable it from the Actions tab.

### Run it on your computer

Python 3.10 or newer.

```bash
git clone https://github.com/Stevnatsan/stock-prediction-lab.git
cd stock-prediction-lab
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m stocklab daily             # collect, score, learn, predict, write the report
python -m stocklab report            # rebuild the report from saved results only
pytest                               # run the tests
```

Change the watchlist with `python -m stocklab watchlist --add "KO, PEP" --remove TSLA`, or edit [`config.yaml`](config.yaml) directly for the paper-trading threshold and sources. `python -m stocklab catalogue` refreshes the S&P 500 list.

## Project structure

```
stocklab/
  sources/        prices (yfinance), news (RSS, Finnhub), filings (SEC EDGAR)
  sentiment.py    VADER + finance vocabulary
  features.py     features known at the close, and the next-session target
  model.py        online logistic regression (about 60 lines, no black box)
  boosting.py     gradient boosting, pooled across stocks, walk-forward retrained
  catalogue.py    the S&P 500 list (catalogue/sp500.csv, STOCKS.md)
  watchlist.py    add or remove stocks
  engine.py       the predict → score → learn loop
  pipeline.py     one daily run
  report.py       README scoreboard, reports/latest.md, charts
state/            predictions, pending calls, headlines, model weights (committed by the bot)
reports/          latest report and charts
tests/            no-lookahead, random-walk, planted-pattern and end-to-end tests
```

## Ideas to take it further

- **Better sentiment:** swap VADER for FinBERT, a language model trained on financial text, and compare live.
- **More sources:** earnings calendars, analyst revisions, options-implied volatility, macro data (FRED), Reddit/StockTwits.
- **A different question:** predict whether a stock beats the market (SPY) rather than raw up/down.
- **Live paper orders:** connect an Alpaca paper-trading account so the top picks are placed as simulated orders with real fills.
- **Calibration:** check whether the "60% up" calls really come true about 60% of the time.

---

MIT licensed. Built by **Steven Nathaniel Santoso** · [GitHub](https://github.com/Stevnatsan). Not financial advice; past accuracy doesn't guarantee future results.
