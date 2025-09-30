import pytest

from cooltime_guard import Guard


class FakeClock:
    def __init__(self, start: float = 0) -> None:
        self.t = start
        self.dt = 0.0

    def clock(self) -> int:
        return int(self.t * 1_000_000_000)

    def sleep(self, dt: float) -> None:
        self.t += dt
        self.dt = dt

    def elapsed_time(self) -> float:
        return self.t
    
    def last_sleep_time(self) -> float:
        return self.dt


def test_first_entry_no_wait() -> None:
    fake = FakeClock(0)
    g = Guard(0.01, clock=fake.clock, sleep=fake.sleep)
    entered: float = 0.0
    with g:
        entered = fake.elapsed_time()
    assert entered == pytest.approx(0.0)


def test_wait_for_remaining_time() -> None:
    fake = FakeClock(0)
    g = Guard(0.01, clock=fake.clock, sleep=fake.sleep)

    with g:
        pass  # exit at t=0 and record last_exit=0

    entered2: float = 0.0
    with g:
        entered2 = fake.elapsed_time()

    assert entered2 == pytest.approx(0.01)


def test_exception_updates_last_exit() -> None:
    fake = FakeClock(0)
    g = Guard(0.02, clock=fake.clock, sleep=fake.sleep)

    with pytest.raises(ValueError):
        with g:
            raise ValueError("boom")

    entered2: float = 0.0
    with g:
        entered2 = fake.elapsed_time()

    assert entered2 == pytest.approx(0.02)


def test_zero_interval_no_wait() -> None:
    fake = FakeClock(0)
    g = Guard(0, clock=fake.clock, sleep=fake.sleep)
    t1: float = 0.0
    with g:
        t1 = fake.elapsed_time()
    t2: float = 0.0
    with g:
        t2 = fake.elapsed_time()
    assert t2 == t1


def test_sleep_time() -> None:
    fake = FakeClock(0)
    g = Guard(0.1, clock=fake.clock, sleep=fake.sleep)
    assert g.ready is True

    elapsed: float = 0.0
    with g:
        elapsed = fake.elapsed_time()
    assert elapsed == pytest.approx(0.0)
    assert g.ready is False

    last_sleep_time: float = 0.0
    fake.sleep(0.03)
    with g:
        last_sleep_time = fake.last_sleep_time()
    assert last_sleep_time == pytest.approx(0.07)
    assert g.ready is False

    fake.sleep(0.05)
    with g:
        last_sleep_time = fake.last_sleep_time()
    assert last_sleep_time == pytest.approx(0.05)
    assert g.ready is False

    fake.sleep(0.099)
    with g:
        last_sleep_time = fake.last_sleep_time()
    assert last_sleep_time == pytest.approx(0.001)
    assert g.ready is False

    fake.sleep(0.1)
    fake.sleep(0.0) # reset last_sleep_time
    assert g.ready is True
    with g:
        last_sleep_time = fake.last_sleep_time()
    assert last_sleep_time == pytest.approx(0.0)
    assert g.ready is False
