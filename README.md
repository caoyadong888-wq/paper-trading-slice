# paper-trading-slice

Paper-only trading slice: cash ledger, market fills, tests, runbook.

**Not a live desk.** No brokerage API, no order proxy, no PnL promises.

## Run

```
python -m pytest -q
python paper_broker.py
```

Python 3.9+ (stdlib + pytest).

## Scope

- In: one agreed paper path (signal fixture → fill → ledger) + tests + 1-page runbook
- Out: live orders, guaranteed returns, unauth scrape, W-9 / US-entity only
