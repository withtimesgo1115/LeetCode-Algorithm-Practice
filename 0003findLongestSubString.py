"""
LeetCode #3 - Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Sliding window with a hash map - O(n) time, O(n) space.

    Maintain a window [i, j] and a map from character to its latest index.
    When a duplicate is found, advance i to max(map[char] + 1, i).
    """
    if not s:
        return 0

    char_index = {}
    max_len = 0
    i = 0

    for j, ch in enumerate(s):
        if ch in char_index:
            i = max(char_index[ch] + 1, i)
        max_len = max(max_len, j - i + 1)
        char_index[ch] = j

    return max_len
