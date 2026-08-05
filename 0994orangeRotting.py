'''
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 新鲜橘子数量
        fresh = 0
        # BFS 队列，记录腐烂橘子的位置
        queue = deque()
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])

        # 遍历网格，统计新鲜橘子数量，并将腐烂橘子的位置加入队列
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0 # 记录分钟数
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # 四个方向, 方便后续遍历

        while queue and fresh > 0: # 当队列不为空且还有新鲜橘子时，继续腐烂过程
            minutes += 1 # 每次循环表示一分钟过去
            # 遍历当前队列中的所有腐烂橘子，也就是当前分钟内腐烂的橘子，换句话说也就是BFS里的每一层
            for _ in range(len(queue)):
                # 弹出当前腐烂橘子的位置，用popleft的原因是我们要按照先进先出的顺序来处理腐烂橘子，pop的话会导致后面腐烂的橘子先处理，影响结果
                r, c = queue.popleft() 
                # 遍历四个方向，检查相邻的橘子是否是新鲜的，如果是，就将其腐烂，并加入队列
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc # 计算相邻橘子的位置
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and grid[nr][nc] == 1
                    ): # 如果相邻橘子是新鲜的，就将其腐烂，并加入队列
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        return minutes if fresh == 0 else -1