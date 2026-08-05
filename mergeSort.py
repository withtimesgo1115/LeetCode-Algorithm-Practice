"""Merge Sort algorithm.
Divide and conquer sorting algorithm with O(n log n) time complexity.
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
