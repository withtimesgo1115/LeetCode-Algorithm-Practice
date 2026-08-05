"""
LeetCode #1 - Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""


def two_sum(nums, target):
    """
    Hash map approach - O(n) time, O(n) space.

    Use a dict to store each value and its index. For each element, check
    whether (target - value) already exists in the dict.
    """
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
