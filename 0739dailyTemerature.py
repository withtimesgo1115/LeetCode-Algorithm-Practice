"""
LeetCode 739. 每日温度 (Daily Temperatures)

题目描述：
    给定一个整数数组 temperatures，表示每天的温度，返回一个数组 answer，
    其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
    如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1：
    输入：temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    输出：[1, 1, 4, 2, 1, 1, 0, 0]

示例 2：
    输入：temperatures = [30, 40, 50, 60]
    输出：[1, 1, 1, 0]

示例 3：
    输入：temperatures = [30, 60, 90]
    输出：[1, 1, 0]

约束条件：
    - 1 <= temperatures.length <= 10^5
    - 30 <= temperatures[i] <= 100

解题思路：
    方法一：暴力法，时间复杂度 O(n^2)，对每一天向后遍历寻找第一个更高温度的日子。
    方法二：单调栈，时间复杂度 O(n)，维护一个存储下标的单调递减栈，
           当遇到比栈顶温度高的元素时，依次弹出栈顶并计算天数差。
"""


def daily_temperatures_brute_force(T):
    """Brute-force approach: O(n^2) time complexity."""
    res = []
    for i in range(len(T)):
        count = 0
        cur_t = T[i]
        flag = False
        for j in range(i + 1, len(T)):
            if T[j] > cur_t:
                flag = True
                count += 1
                res.append(count)
                break
            else:
                count += 1
        if not flag:
            res.append(0)
    return res


def daily_temperatures(T):
    """Monotonic stack approach: O(n) time complexity."""
    length = len(T)
    stack = []
    res = [0] * length
    for i in range(length):
        while stack and T[i] > T[stack[-1]]:
            top = stack.pop()
            res[top] = i - top
        stack.append(i)
    return res
