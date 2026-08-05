"""
LeetCode #20 - Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid. An input string
is valid if open brackets are closed by the same type of brackets and
in the correct order.
"""


def is_valid(s: str) -> bool:
    """
    Stack-based approach - O(n) time, O(n) space.

    For each opening bracket, push the corresponding closing bracket
    onto the stack. For each closing bracket, check that it matches
    the top of the stack. At the end the stack must be empty.
    """
    if not s:
        return True

    left_to_right = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    stack = []

    for ch in s:
        if ch in left_to_right:
            stack.append(left_to_right[ch])
        else:
            if not stack or stack.pop() != ch:
                return False

    return len(stack) == 0
