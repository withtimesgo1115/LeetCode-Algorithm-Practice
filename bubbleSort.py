"""
Bubble Sort

Best: O(n)  Worst: O(n^2)  Average: O(n^2)

Multiple variants from basic to optimized.
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
