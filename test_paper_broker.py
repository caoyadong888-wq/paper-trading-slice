import pytest
from paper_broker import PaperBroker


def test_buy_then_sell_updates_cash_and_position():
    b = PaperBroker(cash=10000.0)
    b.market("BUY", 100, 10.0)
    assert b.cash == 9000.0
    assert b.position == 100
    b.market("SELL", 40, 11.0)
    assert b.cash == 9440.0
    assert b.position == 60
    assert len(b.fills) == 2


def test_rejects_overbuy_and_oversell():
    b = PaperBroker(cash=100.0)
    with pytest.raises(ValueError):
        b.market("BUY", 20, 10.0)
    b.market("BUY", 5, 10.0)
    with pytest.raises(ValueError):
        b.market("SELL", 6, 10.0)


def test_live_flag_hard_off():
    b = PaperBroker(live=True)
    with pytest.raises(RuntimeError):
        b.market("BUY", 1, 1.0)
