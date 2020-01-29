class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]: return -1
        row = len(grid)
        col = len(grid[0])
        q = [(0,0,0)]
        visited = set((0,0,0))
        res = -1
        while q:
            res += 1
            tmp = q
            q = []
            for x,y,t in tmp:
                if t > k:
                    continue
                if x == row -1 and y == col -1 and t <= k:
                    return res
                for i,j in [(1,0),(0,1),(0,-1),(-1,0)]:
                    ti = x + i
                    tj = y + j
                    if 0<=ti<row and 0<=tj<col and (ti, tj, t+grid[ti][tj]) not in visited:
                        q.append((ti, tj, t + grid[ti][tj]))
                        visited.add((ti, tj, t + grid[ti][tj]))
        return -1