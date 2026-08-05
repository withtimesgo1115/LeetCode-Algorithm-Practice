"""
LeetCode 827. 最大人工岛 (Making A Large Island)

题目描述：
    给你一个大小为 n x n 的二进制矩阵 grid。最多只能将一格 0 变成 1。
    返回执行此操作后，grid 中最大的岛屿面积是多少？
    岛屿由一组上、下、左、右四个方向相连的 1 形成。

示例 1：
    输入：grid = [[1,0],[0,1]]
    输出：3
    解释：将一格 0 变成 1，岛屿面积变为 3。

示例 2：
    输入：grid = [[1,1],[1,0]]
    输出：4
    解释：将右下角的 0 变成 1，整个矩阵变为一个面积为 4 的岛屿。

示例 3：
    输入：grid = [[1,1],[1,1]]
    输出：4
    解释：没有 0 可以变成 1，岛屿面积已经是 4。

约束条件：
    - n == grid.length == grid[i].length
    - 1 <= n <= 500
    - grid[i][j] 为 0 或 1

解题思路：
    1. 首先用 DFS 遍历所有岛屿，给每个岛屿标记不同的编号，并记录每个岛屿的面积。
    2. 然后遍历所有海洋格子（值为 0 的格子），尝试将其变为陆地，
       检查其上下左右四个方向连接的岛屿编号，将不同岛屿的面积相加（加 1 代表自身），
       取最大值即为答案。
"""


def _in_area(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def _area(grid, r, c, index):
    if not _in_area(grid, r, c):
        return 0
    if grid[r][c] != 1:
        return 0
    grid[r][c] = index
    return (1 + _area(grid, r - 1, c, index) + _area(grid, r + 1, c, index)
            + _area(grid, r, c - 1, index) + _area(grid, r, c + 1, index))


def _find_neighbours(grid, r, c):
    neighbours = set()
    if _in_area(grid, r - 1, c) and grid[r - 1][c] != 0:
        neighbours.add(grid[r - 1][c])
    if _in_area(grid, r + 1, c) and grid[r + 1][c] != 0:
        neighbours.add(grid[r + 1][c])
    if _in_area(grid, r, c - 1) and grid[r][c - 1] != 0:
        neighbours.add(grid[r][c - 1])
    if _in_area(grid, r, c + 1) and grid[r][c + 1] != 0:
        neighbours.add(grid[r][c + 1])
    return neighbours


def largest_island(grid):
    if not grid or len(grid) == 0:
        return 1
    res = 0
    index = 2
    index_and_areas = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                cur_area = _area(grid, i, j, index)
                index_and_areas[index] = cur_area
                index += 1
                res = max(res, cur_area)
    if res == 0:
        return 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                neighbour_set = _find_neighbours(grid, i, j)
                if len(neighbour_set) < 1:
                    continue
                combined = 1
                for x in neighbour_set:
                    combined += index_and_areas[x]
                res = max(res, combined)
    return res
