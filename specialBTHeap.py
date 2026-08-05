"""Heap operations for a binary heap stored in an array.
Provides down-heap (sift down) and up-heap (sift up) operations.
Operates on a global heap list with index-based parent/child relationships.
"""

import math


def down_heap(heap, low, high):
    """Sift down: move the element at index `low` downward to restore heap property.

    Args:
        heap: The list representing the heap.
        low: The starting index (top of the subtree).
        high: The ending index (bottom of the subtree).
    """
    i = low
    j = i * 2 + 1
    while j <= high:
        # If right child exists and is larger than left child, pick right child
        if j + 1 <= high and heap[j + 1] > heap[j]:
            j = j + 1
        # If current node is smaller than the larger child, swap them
        if heap[i] < heap[j]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = j * 2 + 1
        else:
            break


def up_heap(heap, low, high):
    """Sift up: move the element at index `high` upward to restore heap property.

    Args:
        heap: The list representing the heap.
        low: The starting index (top boundary).
        high: The ending index (the newly inserted element).
    """
    i = high
    j = (i - 1) // 2
    while j >= low:
        if heap[j] < heap[i]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = (i - 1) // 2
        else:
            break
