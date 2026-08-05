"""
冒泡排序 (Bubble Sort)

算法描述：
    冒泡排序是一种简单的交换排序算法。它重复地遍历要排序的列表，
    依次比较相邻的两个元素，如果它们的顺序错误就交换它们。
    每一轮遍历都会将当前未排序部分的最大元素"冒泡"到正确的位置。
    该过程重复进行，直到没有需要交换的元素为止。

示例：
    输入：[64, 34, 25, 12, 22, 11, 90]
    输出：[11, 12, 22, 25, 34, 64, 90]

    输入：[5, 1, 4, 2, 8]
    输出：[1, 2, 4, 5, 8]

实现方式：
    1. bubble_sort - 基础冒泡排序：
       每轮遍历都从头到尾比较相邻元素。
       时间复杂度：最优 O(n^2)，最差 O(n^2)，平均 O(n^2)
       空间复杂度：O(1)

    2. better_bubble_sort - 优化版冒泡排序：
       内层循环随轮次缩小范围，因为每轮结束后末尾已有序。
       时间复杂度：最优 O(n^2)，最差 O(n^2)，平均 O(n^2)
       空间复杂度：O(1)

    3. best_bubble_sort - 最优版冒泡排序：
       加入提前终止标志位，如果某一轮没有发生任何交换，
       说明列表已经有序，直接返回。
       时间复杂度：最优 O(n)（已有序时），最差 O(n^2)，平均 O(n^2)
       空间复杂度：O(1)

    冒泡排序是稳定排序（相等元素的相对顺序不会改变）。
"""


def bubble_sort(arr):
    """Basic bubble sort."""
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def better_bubble_sort(arr):
    """Optimized: inner loop shrinks as the largest elements bubble to the end."""
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def best_bubble_sort(arr):
    """Best case O(n): early exit if no swaps occur in a pass."""
    length = len(arr)
    for i in range(length):
        flag = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            return arr
