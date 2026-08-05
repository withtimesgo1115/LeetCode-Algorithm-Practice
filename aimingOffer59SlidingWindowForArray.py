"""
Sliding Window Maximum (Sword Offer 59 / LeetCode 239)

Given an array and a sliding window of size k, find the maximum value
in each window position.

Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
"""


def _calc_max(arr, left, right):
    if not arr:
        return None
    max_num = arr[left]
    for i in range(left, right + 1):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


def max_sliding_window(nums, k):
    length = len(nums)
    res = []
    left = 0
    right = k - 1
    while right < length:
        max_val = _calc_max(nums, left, right)
        res.append(max_val)
        left += 1
        right += 1
    return res
