"""
Daily Temperatures (LeetCode 739)

Given a list of daily temperatures, return a list where each element represents
the number of days you would have to wait until a warmer temperature.
If there is no future day with a higher temperature, use 0 instead.

Example: temperatures = [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
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
