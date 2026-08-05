"""
Array Flatten

Flatten a nested list of arbitrary depth into a single flat list.
Multiple approaches are provided.
"""


def flatten_reduce(arr):
    """Recursive flatten using a reduce-like pattern."""
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_reduce(item))
        else:
            result.append(item)
    return result


def flatten_to_string(arr):
    """Flatten by converting to string, splitting, and mapping back to numbers."""
    flat = str(arr).replace('[', '').replace(']', '').split(',')
    return [int(x.strip()) for x in flat if x.strip()]


def flatten_join(arr):
    """Flatten by joining with commas, splitting, and parsing."""
    flat = ','.join(str(x) for x in arr).split(',')
    return [int(x) for x in flat if x.strip()]


def flatten_recursion(arr):
    """Recursive flatten."""
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_recursion(item))
        else:
            result.append(item)
    return result
