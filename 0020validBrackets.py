"""
LeetCode 20. 有效的括号 (Valid Parentheses)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。

有效字符串需满足：
    1. 左括号必须用相同类型的右括号闭合。
    2. 左括号必须以正确的顺序闭合。
    3. 每个右括号都有一个对应的相同类型的左括号。

示例 1:
    输入: s = "()"
    输出: true

示例 2:
    输入: s = "()[]{}"
    输出: true

示例 3:
    输入: s = "(]"
    输出: false

示例 4:
    输入: s = "([])"
    输出: true

提示:
    1 <= s.length <= 10^4
    s 仅由括号 '()[]{}' 组成
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
