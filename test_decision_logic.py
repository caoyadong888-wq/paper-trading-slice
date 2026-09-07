from decision_logic import FIXTURE, decide, run_fixture
from paper_broker import PaperBroker


def test_buy_after_3pct_bounce():
    assert decide([10.0, 10.0, 10.31], 0) == "BUY"
    assert decide([10.0, 10.0, 10.01], 0) == "HOLD"


def test_sell_after_3pct_giveback():
    assert decide([10.0, 11.0, 10.66], 100) == "SELL"
    assert decide([10.0, 11.0, 10.80], 100) == "HOLD"


def test_fixture_is_paper_only_and_fills():
    b = run_fixture()
    assert b.live is False
    assert len(b.fills) >= 1
    assert all(f.note == "paper" for f in b.fills)
    assert b.cash + b.position * FIXTURE[-1] == b.equity(FIXTURE[-1])


def test_live_broker_still_blocked():
    live = PaperBroker(live=True)
    try:
        live.market("BUY", 1, 1.0)
        raise AssertionError("live must stay blocked")
    except RuntimeError:
        pass
