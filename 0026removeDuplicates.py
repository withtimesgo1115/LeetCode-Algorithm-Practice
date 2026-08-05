"""
Remove Duplicates from Sorted Array (LeetCode 26)

Given a sorted array, remove duplicates in-place using two pointers
(one slow, one fast) and return the length of the new array.
Time: O(n), Space: O(1).
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    # slow pointer
    i = 0
    # fast pointer
    for j in range(1, len(nums)):
        # once two different elements are found, move slow pointer forward
        # and assign current value of fast pointer to slow pointer position
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
