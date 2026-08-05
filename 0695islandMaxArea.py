"""
695. 岛屿的最大面积 (Max Area of Island)

给你一个大小为 m x n 的二进制矩阵 grid 。
岛屿 是由一些相邻的 1 （代表土地）构成的组合，这里的「相邻」要求两个 1 必须在
水平或者竖直的四个方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。
计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

示例 1：
    输入：grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    输出：6
    解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

示例 2：
    输入：grid = [[0,0,0,0,0,0,0,0]]
    输出：0

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] 为 0 或 1
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
