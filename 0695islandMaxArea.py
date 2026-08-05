"""
岛屿的最大面积 (LeetCode 695)
给定一个包含了一些 0 和 1 的非空二维数组 grid。
一个岛屿由相邻的 1（代表土地）构成，相邻要求两个 1 必须在水平或竖直方向上相邻。
找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 0。
"""


def maxAreaOfIsland(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                a = _area(grid, i, j)
                if a > res:
                    res = a
    return res


def _area(grid, r, c):
    """递归计算以 (r, c) 为起点的岛屿面积。"""
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return 0
    if grid[r][c] != 1:
        return 0
    grid[r][c] = 2  # 标记为已访问
    return 1 + _area(grid, r - 1, c) + _area(grid, r + 1, c) + _area(grid, r, c - 1) + _area(grid, r, c + 1)
