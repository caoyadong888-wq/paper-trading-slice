# Runbook

1. `python -m pytest -q` — paper broker + decision-logic tests, all paper fills.
2. `python paper_broker.py` — demo BUY 100 @ 10 then SELL 40 @ 11.
3. `python decision_logic.py` — ~2h assessment: fixture → decide → paper fills.
4. Failures raise `ValueError` / `RuntimeError`; nothing is silent.
5. Out of scope: live brokerage, guaranteed PnL, production order routing.
6. Re-run needs only Python 3.9+ and pytest. No API keys.
