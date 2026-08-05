"""
Subsets (LeetCode 78)

Given an integer array nums of unique elements, return all possible subsets (the power set).
Uses DFS backtracking.
"""


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    length = len(nums)
    subset = []

    def dfs(index):
        res.append(subset[:])
        for i in range(index, length):
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

    dfs(0)
    return res
