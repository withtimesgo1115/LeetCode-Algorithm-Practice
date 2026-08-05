"""
Full Permutations (LeetCode 46)

Given an array of distinct integers, return all possible permutations.
Uses DFS with a visited tracker.
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    length = len(nums)
    curr = []
    res = []
    visited = {}

    def dfs(nth):
        if nth == length:
            res.append(curr[:])
            return
        for i in range(length):
            if not visited.get(nums[i], 0):
                visited[nums[i]] = 1
                curr.append(nums[i])
                dfs(nth + 1)
                curr.pop()
                visited[nums[i]] = 0

    dfs(0)
    return res
