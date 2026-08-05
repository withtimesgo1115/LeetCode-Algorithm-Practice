"""
Majority Element (LeetCode 169)
Given an array of size n, find the majority element.
The majority element is the element that appears more than floor(n/2) times.
Assumes the array is non-empty and the majority element always exists.
"""


# Method 1: Using a hash map
def majorityElement(nums):
    """Return the majority element using a hash map."""
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)


# Method 2: Using sort (the majority element must be at the middle index)
def majorityElementSort(nums):
    """Return the majority element by sorting."""
    nums.sort()
    index = len(nums) // 2
    return nums[index]
