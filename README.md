# paper-trading-slice

Paper-only trading slice: cash ledger, market fills, decision-logic assessment, tests, runbook.

**Not a live desk.** No brokerage API, no order proxy, no PnL promises.

## Run

```
python -m pytest -q
python paper_broker.py
python decision_logic.py
```

Python 3.9+ (stdlib + pytest).

## ~2h assessment

`decision_logic.py` — fixture prices → BUY/HOLD/SELL → paper fill + ledger.
Rule: buy one lot after a ≥3% bounce from the trough if flat; sell all after a ≥3% giveback from the peak if long.

## Scope

- In: one agreed paper path (signal fixture → fill → ledger) + tests + 1-page runbook
- Out: live orders, guaranteed returns, unauth scrape, W-9 / US-entity only
