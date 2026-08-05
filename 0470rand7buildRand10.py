"""
470. 用 Rand7() 实现 Rand10() (Implement Rand10() Using Rand7())

已有方法 rand7() 可生成 1 到 7 范围内的均匀随机整数。
试写一个函数 rand10() 可生成 1 到 10 范围内的均匀随机整数。
不要使用系统的 Math.random() 方法。

示例 1：
    输入：1
    输出：[2]

示例 2：
    输入：2
    输出：[2, 8]

示例 3：
    输入：3
    输出：[3, 8, 10]

提示：
    1 <= num <= 10^4
    进阶：
    rand7() 调用次数的 期望值 是多少？能否尽可能少地调用 rand7()？
"""

import random


def rand7() -> int:
    """Generate a uniform random integer in [1, 7]."""
    return random.randint(1, 7)


def rand10() -> int:
    """Generate a uniform random integer in [1, 10] using only rand7()."""
    # (rand7()-1)*7 + rand7() generates uniform integers in [1, 49]
    num = (rand7() - 1) * 7 + rand7()
    while num > 10:
        num = (rand7() - 1) * 7 + rand7()
    return num
