"""Company filings from SEC EDGAR (free). The SEC asks every client to identify itself,
so this source only runs when SEC_USER_AGENT is set, e.g. "Your Name your@email.com"."""
from datetime import date

import requests

TICKER_MAP = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS = "https://data.sec.gov/submissions/CIK{cik:010d}.json"


class EdgarClient:
    def __init__(self, user_agent):
        self.headers = {"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"}
        self._ciks = None

    def _cik(self, ticker):
        if self._ciks is None:
            response = requests.get(TICKER_MAP, headers=self.headers, timeout=30)
            response.raise_for_status()
            self._ciks = {row["ticker"].upper(): int(row["cik_str"]) for row in response.json().values()}
        return self._ciks[ticker.upper()]

    def filing_dates(self, ticker, forms=("8-K",)):
        """Dates on which the company filed any of `forms` (most recent ~1,000 filings)."""
        response = requests.get(SUBMISSIONS.format(cik=self._cik(ticker)), headers=self.headers, timeout=30)
        response.raise_for_status()
        recent = response.json()["filings"]["recent"]
        return sorted(date.fromisoformat(d) for f, d in zip(recent["form"], recent["filingDate"]) if f in forms)
