# Runbook

1. `python -m pytest -q` — three tests, all paper fills.
2. `python paper_broker.py` — demo BUY 100 @ 10 then SELL 40 @ 11.
3. Failures raise `ValueError` / `RuntimeError`; nothing is silent.
4. Out of scope: live brokerage, guaranteed PnL, production order routing.
5. Re-run needs only Python 3.9+ and pytest. No API keys.
