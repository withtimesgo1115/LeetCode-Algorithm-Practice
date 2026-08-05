"""Throttle implementations in Python using closures and time tracking.

Provides three throttle variants analogous to the JS versions:
  - timestamp-based
  - timer-based (using threading.Timer)
  - combined timestamp + timer
"""

import time
import threading
from functools import wraps
from typing import Callable


def throttle(func: Callable, delay: float) -> Callable:
    """Timestamp-based throttle: execute immediately if enough time has elapsed."""
    prev = time.time() * 1000  # milliseconds, matching Date.now()

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal prev
        now = time.time() * 1000
        if now - prev >= delay:
            func(*args, **kwargs)
            prev = now

    return wrapper


def throttle2(func: Callable, delay: float) -> Callable:
    """Timer-based throttle: schedule execution after `delay` ms on first call."""
    timer: list[threading.Timer | None] = [None]

    @wraps(func)
    def wrapper(*args, **kwargs):
        if timer[0] is None:
            timer[0] = threading.Timer(delay / 1000.0, func, args=args, kwargs=kwargs)
            timer[0].start()

            def _clear():
                timer[0] = None

            # Schedule clearing after the timer fires
            threading.Timer(delay / 1000.0, _clear).start()

    return wrapper


def throttle3(func: Callable, delay: float) -> Callable:
    """Combined timestamp + timer throttle for both immediate and trailing execution."""
    timer: list[threading.Timer | None] = [None]
    start_time = time.time() * 1000

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal start_time
        cur_time = time.time() * 1000
        remaining = delay - (cur_time - start_time)

        if timer[0] is not None:
            timer[0].cancel()

        if remaining <= 0:
            func(*args, **kwargs)
            start_time = time.time() * 1000
        else:
            timer[0] = threading.Timer(remaining / 1000.0, func, args=args, kwargs=kwargs)
            timer[0].start()

    return wrapper
