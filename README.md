# Stock prediction lab

**A self-updating experiment that predicts whether 10 large US stocks will rise in their next trading session, learns from every right and wrong call, and publishes its full track record, including when it's no better than a coin flip.**

> Educational project, not financial advice. It only paper-trades: no real orders are ever placed.

## Live scoreboard

<!-- scoreboard:start -->
The first run hasn't happened yet. Start the **daily predictions** workflow once (see [Start it](#start-it-on-github-automatic-daily-runs)) and this section will fill itself in after every trading day.
<!-- scoreboard:end -->

## How it works

Every weekday after the US market closes, GitHub Actions runs `python -m stocklab daily`, which:

1. **Collects** today's prices, headlines and company filings from every source below.
2. **Scores yesterday.** Each earlier prediction is checked against how that session actually went.
3. **Learns.** Each stock's model is updated with the inputs it used and the real outcome. The update is proportional to the error, so a confident wrong call (say 90% "up" on a day the stock fell) changes the model about 9× more than a confident right one: **wrong predictions are the biggest lessons.**
4. **Predicts the next session** for every stock: will it close above its opening price?
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

**Two versions of every model run side by side:** *price only* and *price + news*. Comparing their live accuracy shows whether the news actually helps, rather than assuming it does.

## Why not keep training until the accuracy is high?

It's the obvious idea, and it's the trap most trading-bot projects fall into:

- **Retraining on the same history until the score looks good just memorises those days.** The score goes up; accuracy on the next, unseen day doesn't. This is overfitting.
- **Backtests that show 70–90% accuracy almost always have a bug** where the model can see information that didn't exist yet at prediction time (lookahead).
- **Real daily stock moves are very close to a coin flip.** A genuine, repeatable edge of a few percentage points is already valuable, because it applies to thousands of decisions.

So the lab does it differently:

- It **keeps learning from every new outcome**, forever. That's the "if it's wrong, take it as training" idea, done safely.
- It **never grades itself on data it has already learned from**: every prediction is recorded before the answer is known.
- Success means **beating simple rules by more than luck would explain**: always predicting up, always predicting down, or repeating today's direction. Every accuracy figure comes with a 95% range.

The tests check this honestly. On a simulated random market the model scores 50.0% (no hidden leaks). When a real pattern is planted in the simulated data, it finds it and reaches about 70%.

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

Change the watchlist, paper-trading threshold or sources in [`config.yaml`](config.yaml).

## Project structure

```
stocklab/
  sources/        prices (yfinance), news (RSS, Finnhub), filings (SEC EDGAR)
  sentiment.py    VADER + finance vocabulary
  features.py     features known at the close, and the next-session target
  model.py        online logistic regression (about 60 lines, no black box)
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
- **A different question:** predict whether a stock beats the market, or rank the 10 stocks against each other, rather than raw up/down.
- **Non-linear online models** (e.g. online gradient boosting) against this linear baseline.
- **Calibration:** check whether the "60% up" calls really come true about 60% of the time.

---

MIT licensed. Built by **Steven Nathaniel Santoso** · [GitHub](https://github.com/Stevnatsan). Not financial advice; past accuracy doesn't guarantee future results.
