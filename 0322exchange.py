"""
Coin Change.
LeetCode 322 - Given an array of coin denominations and a target amount,
find the minimum number of coins needed to make up that amount.
If it is not possible, return -1.
"""

import math


def coin_change(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins needed to make up the given amount."""
    # f[i] stores the minimum coins needed for amount i
    f = [0] * (amount + 1)

    for i in range(1, amount + 1):
        f[i] = math.inf
        for coin in coins:
            if i - coin >= 0:
                f[i] = min(f[i], f[i - coin] + 1)

    if f[amount] == math.inf:
        return -1

    return f[amount]
