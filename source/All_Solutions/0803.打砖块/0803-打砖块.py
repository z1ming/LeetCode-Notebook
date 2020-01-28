class Solution(object):
    MV_DIRECT = zip([1, -1, 0, 0], [0, 0, 1, -1])

    def cal_new_connect_cnt(self, grid, m, n, x, y):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
            return 0
        grid[x][y] = 2
        return 1 + sum([self.cal_new_connect_cnt(grid, m, n, x + dx, y + dy) for dx, dy in self.MV_DIRECT])

    def judge_round_2(self, grid, m, n, x, y):
        return not (x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 2)

    def hitBricks(self, grid, hits):
        """
        可将过程倒过来，先移除所有砖块，然后一块一块的添加，计算每增加一块，多少砖块的状态变为不会落下
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        n, m = len(grid), len(grid[0])
        for x, y in hits:
            grid[x][y] -= 1
        for i in xrange(m):
            self.cal_new_connect_cnt(grid, m, n, 0, i)
        ret_list = [0] * len(hits)
        for i in xrange(len(hits) - 1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] == 1:
                if x == 0 or any([self.judge_round_2(grid, m, n, x + dx, y + dy) for dx, dy in self.MV_DIRECT]):
                    ret_list[i] = max(self.cal_new_connect_cnt(grid, m, n, x, y) - 1, 0)
        return ret_list