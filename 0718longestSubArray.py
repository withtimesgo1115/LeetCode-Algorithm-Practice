"""
长度最小的子数组 / 最长重复子数组 (LeetCode 718)
给两个整数数组 A 和 B，返回两个数组中公共的、长度最长的子数组的长度。
"""


def findLength(A, B):
    n = len(A)
    m = len(B)
    ans = 0
    # dp[i][j] 表示以 A[i] 和 B[j] 开头的最长公共子数组长度
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
            ans = max(ans, dp[i][j])
    return ans
