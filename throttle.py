"""
节流（Throttle）的 Python 实现

算法描述：
    节流是一种函数调用频率控制技术，确保一个函数在指定的时间间隔内
    最多只执行一次。常用于限制高频触发的事件处理函数（如滚动、窗口调整、
    鼠标移动等）的执行频率，以优化性能。

    本文件实现了三种节流方案（对应 JavaScript 中的常见实现）：

一、时间戳版（throttle）：
    记录上一次执行的时间戳，每次调用时检查当前时间与上次执行时间的差值。
    如果差值大于等于设定的延迟时间，则立即执行函数并更新时间戳。
    特点：第一次调用立即执行，停止调用后不会再次执行。

二、定时器版（throttle2）：
    使用定时器（threading.Timer）实现。第一次调用时设置定时器，
    在延迟时间后执行函数。在定时器运行期间，新的调用会被忽略。
    定时器结束后重置状态，允许下一次调用。
    特点：第一次调用不会立即执行，而是延迟后执行。

三、时间戳 + 定时器结合版（throttle3）：
    综合前两种方案的优点。如果距离上次执行的时间足够长，则立即执行；
    否则设置一个定时器，保证在延迟时间结束后至少执行一次。
    特点：既有立即执行的效果，又保证停止调用后有一次收尾执行。

参数：
    func: 需要被节流的函数。
    delay: 节流间隔时间（毫秒）。

示例：
    # 时间戳版节流
    def handle_scroll():
        print("scroll event handled")

    throttled_scroll = throttle(handle_scroll, 1000)
    # 在 1 秒内多次调用 throttled_scroll()，只有第一次会执行

    # 定时器版节流
    throttled_scroll2 = throttle2(handle_scroll, 1000)
    # 调用后延迟 1 秒执行，期间的新调用被忽略

    # 结合版节流
    throttled_scroll3 = throttle3(handle_scroll, 1000)
    # 第一次立即执行，后续调用在间隔结束后执行一次

复杂度分析：
    每次调用的时间复杂度：O(1)
    空间复杂度：O(1)，只需存储时间戳或定时器引用。
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
