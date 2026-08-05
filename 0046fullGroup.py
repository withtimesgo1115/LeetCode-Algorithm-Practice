"""
46. 全排列

给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- nums 中的所有整数 互不相同
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
