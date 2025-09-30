from __future__ import annotations

import time
from typing import Callable, Literal


class Guard:
    """
    A context manager that enforces a minimum cool-down interval between
    consecutive with-blocks, measured from the previous block's exit time.

    If the previous block exited less than `interval` seconds ago, entering the next
    block will sleep for the remaining time before starting the block.

    Notes:
        `Guard` does not perform lock control for threading/multiprocessing.
        Therefore, if code blocks execute in parallel, the intended behavior 
        may not occur. In such cases, use locks in conjunction with guards.

    Parameters:
        interval (float): Cool-down duration as seconds (float) or datetime.timedelta.
    """

    def __init__(
        self,
        interval: float,
        *,
        clock: Callable[[], int] = time.perf_counter_ns,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._interval = interval
        self._interval_ns = int(interval * 1_000_000_000)
        self._clock = clock
        self._sleep = sleep
        self._last_exit: int | None = None
    
    def _remaining(self) -> int:
        if self._last_exit is None:
            return 0
        remaining = (self._last_exit + self._interval_ns) - self._clock()
        return max(0, remaining)

    @property
    def interval(self) -> float:
        """Cool-down interval in seconds."""
        return self._interval
    
    @property
    def interval_ns(self) -> int:
        """Cool-down interval in nanoseconds."""
        return self._interval_ns

    @property
    def ready(self) -> bool:
        """Whether the guard is ready to enter without waiting."""
        return self._remaining() <= 0

    def __enter__(self) -> "Guard":
        # Compute and perform any necessary wait based on previous exit time.
        remaining_ns = self._remaining()
        if remaining_ns > 0:
            self._sleep(remaining_ns / 1_000_000_000)
        return self

    def __exit__(self, exc_type, exc, tb) -> Literal[False]:
        # Record exit time regardless of exceptions.
        self._last_exit = self._clock()
        return False
