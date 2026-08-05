"""
Multiply Strings (LeetCode 43)

Given two non-negative integers represented as strings, return their product
also as a string.
"""


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if int(num1) == 0 or int(num2) == 0:
        return "0"
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        n1 = int(num1[i])
        for j in range(len(num2) - 1, -1, -1):
            n2 = int(num2[j])
            total = res[i + j + 1] + n1 * n2
            res[i + j + 1] = total % 10
            res[i + j] += total // 10
    result = []
    for i in range(len(res)):
        if i == 0 and res[i] == 0:
            continue
        result.append(str(res[i]))
    return "".join(result)
