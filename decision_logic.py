"""~2h paper assessment: fixture prices -> decision -> paper fill.

Not a live desk. No brokerage API.
"""
from __future__ import annotations

from typing import Iterable, List, Tuple

from paper_broker import PaperBroker

Decision = str  # BUY | SELL | HOLD

# Tiny fixture: open -> drift up -> pullback. Paper marks only.
FIXTURE = [10.00, 10.20, 10.50, 10.40, 10.10, 10.30, 10.60]


def decide(prices: Iterable[float], position: int) -> Decision:
    seq: List[float] = [float(x) for x in prices]
    if len(seq) < 3:
        return "HOLD"
    last = seq[-1]
    peak = max(seq)
    trough = min(seq[:-1]) if len(seq) > 1 else last
    # Up from trough >= 3% and flat/up last tick -> buy one lot if flat.
    if position == 0 and last >= trough * 1.03 and last >= seq[-2]:
        return "BUY"
    # Give back >= 3% from peak while long -> sell all paper shares.
    if position > 0 and last <= peak * 0.97:
        return "SELL"
    return "HOLD"


def run_fixture(prices: Iterable[float] = FIXTURE, lot: int = 100) -> PaperBroker:
    broker = PaperBroker(cash=10000.0, live=False)
    seen: List[float] = []
    for px in prices:
        seen.append(float(px))
        action = decide(seen, broker.position)
        if action == "BUY":
            broker.market("BUY", lot, seen[-1])
        elif action == "SELL" and broker.position:
            broker.market("SELL", broker.position, seen[-1])
    return broker


def ledger(broker: PaperBroker, mark: float) -> Tuple[float, int, float, int]:
    return broker.cash, broker.position, broker.equity(mark), len(broker.fills)


def main() -> None:
    b = run_fixture()
    cash, pos, eq, n = ledger(b, FIXTURE[-1])
    print("cash=%.2f pos=%s equity=%.2f fills=%s last=%s" % (cash, pos, eq, n, FIXTURE[-1]))
    print("fills:", [(f.side, f.qty, f.price) for f in b.fills])


if __name__ == "__main__":
    main()
