import os
import pytest
import time

from cooltime_guard import Guard


@pytest.mark.skipif(os.environ.get("CI") == "true", reason="This test is skipped on CI")
def test_guard_example() -> None:
    guard = Guard(interval=0.005)

    def f() -> float:
        start = time.time()
        elapsed = 0.0
        with guard:
            elapsed = time.time() - start
        return elapsed

    assert f() == pytest.approx(0.0)  # First call should not wait
    assert f() >= 0.005  # Second call should wait at least 5 ms
    assert f() >= 0.005  # Third call should also wait at least 5 ms
    time.sleep(0.05)  # Wait for more than the interval
    assert f() == pytest.approx(0.0)  # Now it should not wait again


@pytest.mark.skipif(os.environ.get("CI") == "true", reason="This test is skipped on CI")
def test_guard_ready_property() -> None:
    guard = Guard(interval=0.01)
    assert guard.ready is True
    with guard:
        pass
    assert guard.ready is False
    time.sleep(0.02)
    assert guard.ready is True


def test_guard_interval() -> None:
    guard = Guard(interval=1)
    assert guard.interval == 1.0
    assert guard.interval_ns == 1_000_000_000
