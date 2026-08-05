"""
LeetCode 300. 最长递增子序列

题目描述：
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
    子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。

示例 1：
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4。

示例 2：
    输入：nums = [0,1,0,3,2,3]
    输出：4

示例 3：
    输入：nums = [7,7,7,7,7,7,7]
    输出：1

提示：
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

进阶：
    你能将算法的时间复杂度降低到 O(n log(n)) 吗？

本文件使用动态规划解法：
    dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度。
    对于每个 i，遍历 j < i，若 nums[j] < nums[i]，则 dp[i] = max(dp[i], dp[j] + 1)。
    时间复杂度 O(n^2)。
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
