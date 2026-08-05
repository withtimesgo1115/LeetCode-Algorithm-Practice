"""Selection Sort algorithm.
Select the minimum value in the unsorted portion and place it at the head.
Best/Worst/Average: O(n^2)
"""


def select_sort(arr):
    """Sort an array in-place using selection sort and return it."""
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
