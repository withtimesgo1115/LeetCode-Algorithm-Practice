"""
Word Zip Code / Minimum Length Encoding (LeetCode 820)

Given a list of words, encode them into a string S with '#' as separator
and an index list A. Find the minimum length of the encoded string.

Example: words = ["time", "me", "bell"] -> 10
Explanation: S = "time#bell#", indexes = [0, 2, 5]
"""


def minimum_length_encoding(words):
    myset = set(words)
    for item in list(myset):
        for i in range(1, len(item)):
            substr = item[i:]
            if substr in myset:
                myset.discard(substr)
    res = 0
    for item in myset:
        res += len(item) + 1
    return res
