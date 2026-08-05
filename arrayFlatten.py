"""
数组扁平化 (Array Flatten)

题目描述：
    将一个任意深度的嵌套列表展开为一个单层扁平列表。
    本文件提供了多种实现方式。

示例：
    输入：[1, [2, [3, 4]], [5, 6]]
    输出：[1, 2, 3, 4, 5, 6]

    输入：[1, [2, 3], [[4, [5]], 6], 7]
    输出：[1, 2, 3, 4, 5, 6, 7]

实现方式：
    1. flatten_reduce - 递归展开法：遍历列表元素，若元素为列表则递归展开，
       否则直接添加到结果列表。时间复杂度 O(n)，空间复杂度 O(d)，
       其中 n 为元素总数，d 为最大嵌套深度（递归栈深度）。

    2. flatten_to_string - 字符串转换法：将列表转为字符串后去除方括号，
       再按逗号分割并转换回整数。时间复杂度 O(n)，空间复杂度 O(n)。

    3. flatten_join - 字符串拼接法：将所有元素转为字符串后用逗号连接，
       再按逗号分割并解析为整数。时间复杂度 O(n)，空间复杂度 O(n)。

    4. flatten_recursion - 递归展开法：与 flatten_reduce 思路相同，
       使用递归处理嵌套列表。时间复杂度 O(n)，空间复杂度 O(d)。
"""


def flatten_reduce(arr):
    """Recursive flatten using a reduce-like pattern."""
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_reduce(item))
        else:
            result.append(item)
    return result


def flatten_to_string(arr):
    """Flatten by converting to string, splitting, and mapping back to numbers."""
    flat = str(arr).replace('[', '').replace(']', '').split(',')
    return [int(x.strip()) for x in flat if x.strip()]


def flatten_join(arr):
    """Flatten by joining with commas, splitting, and parsing."""
    flat = ','.join(str(x) for x in arr).split(',')
    return [int(x) for x in flat if x.strip()]


def flatten_recursion(arr):
    """Recursive flatten."""
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_recursion(item))
        else:
            result.append(item)
    return result
