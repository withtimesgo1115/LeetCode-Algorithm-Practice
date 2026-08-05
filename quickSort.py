"""Quick Sort algorithm.
Uses the partition scheme with the middle element as pivot.
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
