class Solution:
    def uniquePathsIII(self, grid: 'm * n grid') -> int:

        self.grid, self.paths = grid, 0
        self.reset()
        self.walk(1, self.start, grid)
        return self.paths

    def reset(self):

        self.m, self.n = len(self.grid), len(self.grid[0])
        self.spaces = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.start = (i, j)
                elif self.grid[i][j] == 2:
                    self.end = (i, j)
                elif not self.grid[i][j]:
                    self.spaces += 1

    def walk(self, cur_filled: int, start: '(i, j)', cur_grid: 'grid'):

        if cur_filled < self.spaces:
            for i_next, j_next in self.neighbor(start, cur_grid):
                next_start = (i_next, j_next)
                next_grid = [line[:] for line in cur_grid]
                next_grid[i_next][j_next] = 1
                if self.neighbor(self.end, next_grid) and (
                    self.neighbor(next_start, next_grid)):
                    self.walk(cur_filled + 1, next_start, next_grid)
        elif cur_filled == self.spaces:
            self.paths += 1
        else:
            self.paths = int(self.start in self.neighbor(self.end))

    def neighbor(self, center: '(i, j)', cur_grid = None) -> 'list[(i, j)]':
        '''返回(i, j)的相邻为0的合法坐标'''
        i, j = center
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if not i:
            neighbors.remove((i - 1, j))
        if i == self.m - 1:
            neighbors.remove((i + 1, j))
        if not j :
            neighbors.remove((i, j - 1))
        if j == self.n - 1:
            neighbors.remove((i, j + 1))

        if cur_grid:
        	neighbors = [(i, j) for i, j in neighbors if not cur_grid[i][j]]
        return neighbors