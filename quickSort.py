"""
快速排序（Quick Sort）

算法描述：
    快速排序是一种基于分治策略的高效排序算法。它通过选择一个基准元素（pivot），
    将数组分为两部分：小于基准的元素和大于基准的元素，然后递归地对这两部分
    进行排序。

    本实现选择中间位置的元素作为基准值（pivot），使用双指针从两端向中间扫描
    并进行交换。

算法步骤：
    1. 选择一个基准元素（本实现选取中间位置的元素）。
    2. 设置两个指针，分别指向子数组的左端和右端。
    3. 左指针向右移动，直到找到一个大于等于基准的元素。
    4. 右指针向左移动，直到找到一个小于等于基准的元素。
    5. 如果左指针 <= 右指针，交换这两个元素，两个指针各移动一步。
    6. 重复步骤 3-5，直到左指针超过右指针。
    7. 递归地对基准左侧和右侧的子数组进行排序。

时间复杂度：
    - 最优：O(n log n)，每次分区都能均匀分割。
    - 最差：O(n^2)，当数组已经有序且每次选取的基准为最大或最小值时。
    - 平均：O(n log n)
空间复杂度：O(log n)，递归调用栈的深度，最差情况下为 O(n)。
稳定性：不稳定排序算法，相同元素的相对顺序可能在交换过程中改变。

示例：
    输入：[10, 7, 8, 9, 1, 5]
    输出：[1, 5, 7, 8, 9, 10]
"""


def quick_sort(arr, left=0, right=None):
    """Sort an array in-place using quick sort and return it."""
    if right is None:
        right = len(arr) - 1
    if len(arr) > 1:
        next_pivot = _partition(arr, left, right)
        if left < next_pivot - 1:
            quick_sort(arr, left, next_pivot - 1)
        if next_pivot < right:
            quick_sort(arr, next_pivot, right)
    return arr


def _partition(arr, left, right):
    """Partition the array around a pivot and return the pivot index."""
    pivot_value = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot_value:
            i += 1
        while arr[j] > pivot_value:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i
