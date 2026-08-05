"""
Largest Human Island (LeetCode 827)

In a 2D grid, 0 represents water and 1 represents land. You can change at most
one 0 to 1. What is the largest island area after the change?
(Two cells connected vertically or horizontally form an island.)

Example: grid = [[1,0],[0,1]] -> 3
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
