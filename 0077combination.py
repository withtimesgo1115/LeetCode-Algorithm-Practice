"""
Combinations (LeetCode 77)

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n]. Uses DFS backtracking.
"""


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    subset = []

    def dfs(index):
        if len(subset) == k:
            res.append(subset[:])
            return
        for i in range(index, n + 1):
            subset.append(i)
            dfs(i + 1)
            subset.pop()

    dfs(1)
    return res
