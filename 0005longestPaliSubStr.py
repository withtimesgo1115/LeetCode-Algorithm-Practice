"""
LeetCode 5. 最长回文子串 (Longest Palindromic Substring)

给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1:
    输入: s = "babad"
    输出: "bab"
    解释: "aba" 同样是符合题意的答案。

示例 2:
    输入: s = "cbbd"
    输出: "bb"

提示:
    1 <= s.length <= 1000
    s 仅由数字和英文字母组成
"""


def longest_palindrome(s: str) -> str:
    """
    Dynamic programming approach - O(n^2) time, O(n^2) space.

    dp[i][j] is True if s[i..j] is a palindrome.
    Base cases: single chars are palindromes; two adjacent equal chars
    form a palindrome. Transition: dp[i][j] = dp[i+1][j-1] when
    s[i] == s[j].
    """
    n = len(s)
    if n < 2:
        return s

    max_len = 1
    begin = 0

    # dp[i][j] indicates whether s[i..j] is a palindrome
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    for j in range(1, n):
        for i in range(j):
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i

    return s[begin:begin + max_len]
