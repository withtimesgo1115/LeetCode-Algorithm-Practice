"""
验证回文串 II (LeetCode 680)
给定一个非空字符串 s，删除最多一个字符后，判断是否能成为回文字符串。
"""


def validPalindrome(s):
    def _is_palindrome(start, end):
        """判断 s[start:end+1] 是否为回文串。"""
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    length = len(s)
    # 定义双指针
    i = 0
    j = length - 1
    # 双指针向中间移动，直到遇到不匹配的字符
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    # 遇到不匹配时，尝试跳过左边或右边的字符
    if _is_palindrome(i + 1, j):
        return True
    if _is_palindrome(i, j - 1):
        return True

    return False
