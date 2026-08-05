"""
归并排序（Merge Sort）

算法描述：
    归并排序是采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，
    再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

算法步骤：
    1. 把长度为 n 的输入序列分成两个长度为 n/2 的子序列。
    2. 对这两个子序列分别采用归并排序（递归）。
    3. 将两个排序好的子序列合并成一个最终的排序序列。

时间复杂度：
    - 最优：O(n log n)
    - 最差：O(n log n)
    - 平均：O(n log n)
    无论输入数据的初始状态如何，时间复杂度都稳定在 O(n log n)。
空间复杂度：O(n)，合并过程中需要额外的数组空间来存储临时结果。
稳定性：稳定排序算法，相等元素的相对顺序不会改变。

示例：
    输入：[38, 27, 43, 3, 9, 82, 10]
    输出：[3, 9, 10, 27, 38, 43, 82]

    分治过程：
    [38, 27, 43, 3, 9, 82, 10]
    -> [38, 27, 43, 3] + [9, 82, 10]
    -> [38, 27] + [43, 3] + [9, 82] + [10]
    -> [27, 38] + [3, 43] + [9, 82] + [10]
    -> [3, 27, 38, 43] + [9, 10, 82]
    -> [3, 9, 10, 27, 38, 43, 82]
"""


def merge_sort(arr):
    """Sort an array using merge sort and return a new sorted array."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return _merge_arr(left_arr, right_arr)


def _merge_arr(arr1, arr2):
    """Merge two sorted arrays into one sorted array."""
    i, j = 0, 0
    res = []
    len1, len2 = len(arr1), len(arr2)
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i < len1:
        res.extend(arr1[i:])
    else:
        res.extend(arr2[j:])
    return res
