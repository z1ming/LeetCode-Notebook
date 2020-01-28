class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax, colMax, n = [max(i) for i in grid], [max(i) for i in zip(*grid)], len(grid)
        return sum(min(rowMax[i], colMax[j]) - grid[i][j] for i in range(n) for j in range(n))