"""
Number of Islands (LeetCode 200)
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.
"""


def numIslands(grid):
    """Return the number of islands in the grid."""
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, r, c):
    """Depth-first search to mark all connected land cells as visited."""
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '2'  # mark as visited
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)
