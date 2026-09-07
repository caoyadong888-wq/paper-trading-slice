"""In-memory paper broker. No live orders."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Fill:
    side: str
    qty: int
    price: float
    note: str = "paper"


@dataclass
class PaperBroker:
    cash: float = 10000.0
    position: int = 0
    fills: List[Fill] = field(default_factory=list)
    live: bool = False

    def market(self, side: str, qty: int, price: float) -> Fill:
        if self.live:
            raise RuntimeError("live orders are disabled")
        if qty <= 0 or price <= 0:
            raise ValueError("qty and price must be positive")
        side = side.upper()
        notional = qty * price
        if side == "BUY":
            if notional > self.cash + 1e-9:
                raise ValueError("insufficient paper cash")
            self.cash -= notional
            self.position += qty
        elif side == "SELL":
            if qty > self.position:
                raise ValueError("insufficient paper shares")
            self.cash += notional
            self.position -= qty
        else:
            raise ValueError("side must be BUY or SELL")
        fill = Fill(side=side, qty=qty, price=price)
        self.fills.append(fill)
        return fill

    def equity(self, mark: float) -> float:
        return self.cash + self.position * mark


def demo() -> None:
    b = PaperBroker()
    b.market("BUY", 100, 10.0)
    b.market("SELL", 40, 11.0)
    print("cash=%.2f pos=%s equity=%.2f fills=%s" % (b.cash, b.position, b.equity(11.0), len(b.fills)))


if __name__ == "__main__":
    demo()
