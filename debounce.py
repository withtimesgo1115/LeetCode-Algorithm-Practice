"""
Debounce

A debounce decorator that delays invoking a function until after a specified
wait time has elapsed since the last call. Python equivalent using threading.
"""

import threading


def debounce(wait):
    """
    Decorator that debounces a function call.
    The function will only be called after `wait` seconds have elapsed
    since the last invocation.

    Args:
        wait: Delay in seconds before executing the function.
    """
    def decorator(fn):
        timer = [None]
        lock = threading.Lock()

        def debounced(*args, **kwargs):
            with lock:
                if timer[0] is not None:
                    timer[0].cancel()
                timer[0] = threading.Timer(wait, fn, args=args, kwargs=kwargs)
                timer[0].start()

        return debounced
    return decorator
