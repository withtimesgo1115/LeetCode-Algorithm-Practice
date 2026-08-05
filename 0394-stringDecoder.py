"""
394. 字符串解码 (Decode String)

给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 恰好重复 k 次。
需要注意的是 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以假设原始字符串中的数据中不包含嵌套方括号，形如 3[a] 或 2[4[bc]] 的输入都是合法的。
同时保证方括号内的 s 只包含字母。

示例 1：
    输入：s = "3[a]2[bc]"
    输出："aaabcbc"

示例 2：
    输入：s = "3[a2[c]]"
    输出："accaccacc"

示例 3：
    输入：s = "2[abc]3[cd]ef"
    输出："abcabccddef"

示例 4：
    输入：s = "abc3[cd]xyz"
    输出："abccdcdcdxyz"

提示：
    1 <= s.length <= 30
    s 由小写英文字母、数字和方括号 '[]' 组成
    s 保证是一个 有效 的输入
    s 中所有整数的取值范围为 [1, 300]
"""


def decode_string(s: str) -> str:
    """Decode the encoded string."""
    num_stack: list[int] = []
    str_stack: list[str] = []
    num = 0
    result = ""

    for char in s:
        if char.isdigit():
            # Build the multiplier number
            num = num * 10 + int(char)
        elif char == "[":
            # Push current result and multiplier onto stacks
            str_stack.append(result)
            result = ""
            num_stack.append(num)
            num = 0
        elif char == "]":
            # Pop multiplier and previous string, then repeat
            repeat_times = num_stack.pop()
            result = str_stack.pop() + result * repeat_times
        else:
            # Regular character, append to result
            result += char

    return result
