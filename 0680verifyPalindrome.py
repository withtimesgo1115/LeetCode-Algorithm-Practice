"""
680. 验证回文串 II (Valid Palindrome II)

给你一个字符串 s，最多 可以从中删除一个字符。
请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

示例 1：
    输入：s = "aba"
    输出：true

示例 2：
    输入：s = "abca"
    输出：true
    解释：你可以删除字符 'c' 。

示例 3：
    输入：s = "abc"
    输出：false

提示：
    1 <= s.length <= 10^5
    s 由可打印的 ASCII 字符组成
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
