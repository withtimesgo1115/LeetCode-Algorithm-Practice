"""
Decode String.
LeetCode 394 - Given an encoded string of the form k[encoded_string],
where encoded_string is repeated exactly k times, return the decoded string.
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
