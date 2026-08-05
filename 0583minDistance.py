"""
583. 两个字符串的删除操作 (Delete Operation for Two Strings)

给定两个单词 word1 和 word2 ，返回使得 word1 和 word2 相同所需的最小步数。
每步可以删除任意一个字符串中的一个字符。

示例 1：
    输入：word1 = "sea", word2 = "eat"
    输出：2
    解释：第一步将 "sea" 变为 "ea" ，第二步将 "eat" 变为 "ea"

示例 2：
    输入：word1 = "leetcode", word2 = "etco"
    输出：4

提示：
    1 <= word1.length, word2.length <= 500
    word1 和 word2 只包含小写英文字母
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
