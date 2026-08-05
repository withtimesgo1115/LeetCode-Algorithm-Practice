"""
Delete Operation for Two Strings (Minimum Distance).
LeetCode 583 - Given two strings word1 and word2, find the minimum number of
deletions required to make both strings equal. Each deletion removes one
character from either string.

Approach: Find the longest common subsequence (LCS), then the answer is
len(word1) + len(word2) - 2 * len(LCS).
"""


def min_distance(word1: str, word2: str) -> int:
    """Return the minimum number of deletions to make word1 and word2 equal."""
    len1 = len(word1)
    len2 = len(word2)

    # dp[i][j] = length of LCS of word1[:i] and word2[:j]
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return len1 + len2 - 2 * dp[len1][len2]
