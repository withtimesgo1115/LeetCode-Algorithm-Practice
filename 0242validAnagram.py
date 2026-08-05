"""
Valid Anagram.
Given two strings s and t, determine whether t is an anagram of s.
Provides two methods: sorting-based O(n log n) and frequency-map O(n).
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
