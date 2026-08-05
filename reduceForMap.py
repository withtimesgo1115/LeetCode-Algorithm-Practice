"""
使用 reduce 实现 map（用 reduce 实现 map 的功能）

算法描述：
    本实现展示了如何使用 reduce（归约）来构建 map（映射）的功能。
    map 的作用是对数组中的每个元素执行回调函数，并返回一个新数组；
    reduce 的作用是将数组中的元素通过累积器归约为一个单一值。

    核心思路：
        将 reduce 的累积值设为一个新数组，每次迭代时将回调函数的
        返回值追加到累积数组中，最终得到的数组就是 map 的效果。

    这等价于 JavaScript 中的：
        Array.prototype.map = function(callback) {
            return this.reduce((acc, cur, i) => acc.concat([callback(cur, i, this)]), []);
        }

参数：
    arr: 输入列表。
    callback: 转换函数，接收 (value, index, array) 三个参数，返回转换后的值。

返回值：
    一个新的列表，其中每个元素都是原列表对应元素经过 callback 转换后的结果。

示例：
    # 将每个元素乘以 2
    map_with_reduce([1, 2, 3, 4], lambda v, i, a: v * 2)
    输出：[2, 4, 6, 8]

    # 获取每个元素的索引信息
    map_with_reduce(['a', 'b', 'c'], lambda v, i, a: f"{i}:{v}")
    输出：['0:a', '1:b', '2:c']

复杂度分析：
    时间复杂度：O(n)，其中 n 为数组长度，每个元素访问一次。
    空间复杂度：O(n)，需要创建一个新的数组来存储结果。
    注意：由于每次迭代都创建新列表（acc + [...]），实际时间复杂度为 O(n^2)；
    若改用 append 可优化至 O(n)。
"""

from functools import reduce


def map_with_reduce(arr, callback):
    """Implement map functionality using reduce.

    Args:
        arr: The input list.
        callback: A function taking (value, index, array) and returning a transformed value.

    Returns:
        A new list with each element transformed by the callback.
    """
    return reduce(
        lambda acc, cur: acc + [callback(cur[1], cur[0], arr)],
        enumerate(arr),
        []
    )
