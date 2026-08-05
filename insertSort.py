"""Insertion Sort algorithm.
Best: O(n), Worst: O(n^2), Average: O(n^2)
"""


def insert_sort(arr):
    """Sort an array in-place using insertion sort and return it."""
    length = len(arr)
    for i in range(length):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr
