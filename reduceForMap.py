"""Implement map using reduce.
Demonstrates how Array.prototype.map can be built on top of reduce.
"""

from functools import reduce


def map_with_reduce(arr, callback):
    """Implement map functionality using reduce.

    Args:
        arr: The input list.
        callback: A function taking (value, index, array) and returning a transformed value.

    Returns:
        A new list with each element transformed by the callback.
    """
    return reduce(
        lambda acc, cur: acc + [callback(cur[1], cur[0], arr)],
        enumerate(arr),
        []
    )
