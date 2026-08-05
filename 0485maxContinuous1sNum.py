"""
Max Consecutive Ones.
LeetCode 485 - Given a binary array, find the maximum number of consecutive 1s.
"""


def find_max_consecutive_ones(nums: list[int]) -> int:
    """Return the maximum number of consecutive 1s in the array."""
    count = 0
    max_count = 0

    if 0 not in nums:
        return len(nums)

    for num in nums:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count
