# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3

'''
测试用时：232ms
'''
from typing import List


class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第1行、第一格开始，对每一格尝试进行一次DFS操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用DFS发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)

'''
测试用时：132ms
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        # 编写DFS函数
        def dfs(grid, r, c):
            grid[r][c] = "0"
            if r-1>=0 and grid[r-1][c] == "1":
                dfs(grid, r-1, c)
            if c-1>=0 and grid[r][c-1] == "1":
                dfs(grid, r, c-1)
            if r+1<nr and grid[r+1][c] == "1":
                dfs(grid, r+1, c)
            if c+1<nc and grid[r][c+1] == "1":
                dfs(grid, r, c+1)
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=="1":
                    count += 1
                    dfs(grid, i, j)
        return count