class Solution:
    def __init__(self):
        self.k = 0 # k: size of island

    def area_of_island(self, grid, m, n, i, j, k):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
            return 
        grid[i][j] = 2
        self.k += 1
        
        self.area_of_island(grid, m, n, i+1, j, k+1)
        self.area_of_island(grid, m, n, i-1, j, k+1)
        self.area_of_island(grid, m, n, i, j+1, k+1)
        self.area_of_island(grid, m, n, i, j-1, k+1)
        
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0
        
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                self.area_of_island(grid, m, n, i, j, 0)
                res = max(res, self.k)
                self.k = 0
        return res