class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        border,visit = set(),set()

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col and grid[r][c] == grid[r0][c0]):return False
            if (r, c) in visit:return True
            visit.add((r,c))
            if dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) < 4:border.add((r, c))
            return True
        
        dfs(r0,c0)
        for (x,y) in border:grid[x][y]=color
        return grid