class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        line = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                line.append(grid[i][j])
        idx = k % len(line)
        line[:] = line[len(line) - idx:] + line[:len(line) - idx]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = line.pop(0)
        return grid