"""
Longest Increasing Subsequence (Longest Climbing Sub-Array).
LeetCode 300 variant - Given an array of integers, find the length of the
longest strictly increasing subsequence using dynamic programming.
"""


def length_of_lis(nums: list[int]) -> int:
    """Return the length of the longest increasing subsequence."""
    length = len(nums)
    if not length:
        return 0

    # dp[i] stores the length of the LIS ending at index i
    dp = [1] * length
    max_len = 1

    for i in range(1, length):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > max_len:
            max_len = dp[i]

    return max_len
