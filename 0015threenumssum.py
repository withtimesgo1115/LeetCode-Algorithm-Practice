"""
LeetCode #15 - 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and
nums[i] + nums[j] + nums[k] == 0. No duplicate triplets in the result.
"""


def three_sum(nums):
    """
    Sort + two-pointer approach - O(n^2) time.

    Sort the array first. For each element, use two pointers (left and
    right) to find pairs that sum to the negation of the current element.
    Skip duplicates to avoid repeated triplets.
    """
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif total > 0:
                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return res
