"""
LeetCode #8 - String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer (similar to C/C++'s atoi function).
"""

import re


def my_atoi(s: str) -> int:
    """
    Regex-based approach.

    Match optional leading whitespace followed by an optional sign and
    digits. Clamp the result to the 32-bit signed integer range
    [-2^31, 2^31 - 1].
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    match = re.match(r'\s*([+-]?\d*)', s)
    if match:
        num_str = match.group(1)
        if not num_str or num_str in ('+', '-'):
            return 0
        num = int(num_str)
    else:
        return 0

    if num > INT_MAX:
        return INT_MAX
    elif num < INT_MIN:
        return INT_MIN
    return num
