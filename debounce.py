"""
防抖 (Debounce)

算法描述：
    防抖是一种常用的函数调用控制策略。防抖装饰器会延迟函数的执行，
    如果在指定的等待时间内该函数被再次调用，则重新计时；
    只有当等待时间结束且期间没有新的调用时，函数才会真正执行。

    防抖常用于以下场景：
    - 搜索框输入联想：用户停止输入后才发送搜索请求
    - 窗口 resize 事件：窗口大小调整完成后才执行布局计算
    - 按钮防重复点击：防止用户短时间内多次点击触发多次请求

示例：
    假设 wait = 2 秒，对函数 fn 应用防抖：
    - 第 0 秒调用 fn -> 不立即执行，开始 2 秒倒计时
    - 第 1 秒调用 fn -> 取消上一次倒计时，重新开始 2 秒倒计时
    - 第 3 秒调用 fn -> 取消上一次倒计时，重新开始 2 秒倒计时
    - 第 5 秒没有新调用 -> fn 真正执行

实现方式：
    使用 Python 的 threading.Timer 实现定时器，threading.Lock 保证线程安全。
    每次调用被装饰的函数时，先取消之前的定时器（如果存在），
    然后创建新的定时器在 wait 秒后执行目标函数。

    时间复杂度：每次调用 O(1)
    空间复杂度：O(1)（仅维护一个定时器和一个锁）
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
