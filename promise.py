"""
Promise 的 Python 实现（模拟 JavaScript Promise）

算法描述：
    Promise 是一种用于处理异步操作的对象，它代表一个异步操作的最终完成
    （或失败）及其结果值。本实现模拟了 JavaScript 中 Promise 的核心行为。

    一个 Promise 对象有三种状态：
        - pending（待定）：初始状态，既没有被兑现，也没有被拒绝。
        - resolved（已兑现）：操作成功完成。
        - rejected（已拒绝）：操作失败。

    状态转换规则：
        - pending -> resolved：调用 resolve(value) 时转换。
        - pending -> rejected：调用 reject(reason) 时转换。
        - 状态一旦转换就不可逆，即 resolved 或 rejected 后不会再改变。

    核心方法：
        - then(on_fulfilled, on_rejected)：注册回调函数。
          当 Promise 状态变为 resolved 时调用 on_fulfilled；
          当状态变为 rejected 时调用 on_rejected。
          如果在 pending 状态时注册回调，回调会被缓存，等待状态变更后执行。

    本实现支持：
        - 同步 resolve/reject
        - 异步回调缓存（pending 状态下注册回调）
        - then 链式调用（注册成功和失败的回调）

示例：
    # 同步 resolved
    p = MyPromise(lambda resolve, reject: resolve("成功"))
    p.then(lambda v: print(v))  # 输出: 成功

    # 同步 rejected
    p = MyPromise(lambda resolve, reject: reject("失败"))
    p.then(lambda v: print(v), lambda r: print(r))  # 输出: 失败

    # 异步回调
    p = MyPromise(lambda resolve, reject: resolve(42))
    p.then(lambda v: print(f"值为: {v}"))  # 输出: 值为: 42

复杂度分析：
    构造时间复杂度：O(1)
    then 注册回调时间复杂度：O(1)
    空间复杂度：O(k)，k 为注册的回调数量
"""

PENDING = 'pending'
RESOLVED = 'resolved'
REJECTED = 'rejected'


class MyPromise:
    """A simple Promise implementation inspired by JavaScript Promises."""

    def __init__(self, fn):
        self.state = PENDING
        self.value = None
        self.resolved_callbacks = []
        self.rejected_callbacks = []

        def resolve(value):
            if self.state == PENDING:
                self.state = RESOLVED
                self.value = value
                for cb in self.resolved_callbacks:
                    cb(self.value)

        def reject(value):
            if self.state == PENDING:
                self.state = REJECTED
                self.value = value
                for cb in self.rejected_callbacks:
                    cb(self.value)

        try:
            fn(resolve, reject)
        except Exception as e:
            reject(e)

    def then(self, on_fulfilled=None, on_rejected=None):
        """Register callbacks for resolved and rejected states."""
        if on_fulfilled is None:
            on_fulfilled = lambda v: v
        if on_rejected is None:
            on_rejected = lambda r: r  # noqa: E731

        if self.state == PENDING:
            self.resolved_callbacks.append(on_fulfilled)
            self.rejected_callbacks.append(on_rejected)
        elif self.state == RESOLVED:
            on_fulfilled(self.value)
        elif self.state == REJECTED:
            on_rejected(self.value)
