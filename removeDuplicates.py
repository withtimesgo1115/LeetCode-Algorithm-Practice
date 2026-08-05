"""Remove duplicates from an array.
Time complexity: O(n^2) due to in-place removal.
"""


def unique(arr):
    """Remove duplicate elements from a list in-place and return it."""
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            j += 1
        i += 1
    return arr
