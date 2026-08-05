"""
LeetCode 242. 有效的字母异位词

题目描述：
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    字母异位词指包含相同字母但可能顺序不同的字符串，每个字母出现的次数必须相同。

示例 1：
    输入：s = "anagram", t = "nagaram"
    输出：True

示例 2：
    输入：s = "rat", t = "car"
    输出：False

提示：
    1 <= s.length, t.length <= 5 * 10^4
    s 和 t 仅包含小写字母

进阶：如果输入字符串包含 Unicode 字符怎么办？你能调整你的解法来应对这种情况吗？

本文件提供两种解法：
    - 排序法：时间复杂度 O(n log n)
    - 频率映射法：时间复杂度 O(n)
"""

from collections import Counter


def is_anagram_sort(s, t):
    """Method 1: Sort both strings and compare. O(n log n)."""
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def is_anagram(s, t):
    """Method 2: Use a frequency map. O(n)."""
    if len(s) != len(t):
        return False

    count = Counter(s)
    for ch in t:
        if ch in count:
            count[ch] -= 1
        else:
            return False

    return all(v == 0 for v in count.values())
