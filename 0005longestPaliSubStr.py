"""
LeetCode #5 - Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
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
