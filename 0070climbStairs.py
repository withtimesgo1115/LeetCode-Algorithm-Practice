"""
Climbing Stairs (LeetCode 70)

You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

Critical condition: f(n) = f(n-1) + f(n-2), f(1)=1, f(2)=2
"""


def climbStairs(n):
    """
    DP (dynamic programming) approach.
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
