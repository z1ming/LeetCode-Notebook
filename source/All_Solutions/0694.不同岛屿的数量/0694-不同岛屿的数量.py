class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, pos, rel_pos):
            if grid[x][y] != 1: return
            grid[x][y] = -1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                if 0 <= x+dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == 1:
                    new_rel_pos = (rel_pos[0] + dx, rel_pos[1] + dy)
                    pos.append(new_rel_pos)
                    dfs(x+dx, y+dy, pos, new_rel_pos)
        shapes = set()
        row, col = len(grid), len(grid[0])
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    pos = []
                    dfs(x, y, pos, (0, 0))
                    shapes.add(tuple(pos))
        return len(shapes)
