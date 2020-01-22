# 你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，通过调研，你希望从它出发能在 最短的距离和 内抵达周边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。
#
#  
#
# 注意：
#
# 你只能通过向上、下、左、右四个方向上移动。
#
# 给你一个由 0、1 和 2 组成的二维网格，其中：
#
# 0 代表你可以自由通过和选择建造的空地
# 1 代表你无非通行的建筑物
# 2 代表你无非通行的障碍物
#  
#
# 示例：
#
# 输入: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# 输出: 7
#
# 解析:
# 给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
# 由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。

import queue
import sys


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = [[0 for _ in range(c)] for _ in range(r)]
        dist = [[0 for _ in range(c)] for _ in range(r)]
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        buildings = 0

        # initial
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    buildings += 1
                    qu = queue.Queue()
                    visit = [[0 for _ in range(c)] for _ in range(r)]

                    qu.put((i, j))
                    visit[i][j] = 1
                    step = 0
                    while not qu.empty():
                        sz = qu.qsize()
                        step += 1

                        for k in range(sz):
                            curr = qu.get()
                            for m in range(4):
                                x = curr[0] + d[m][0]
                                y = curr[1] + d[m][1]
                                if x >= 0 and x < r and y >= 0 and y < c:
                                    if visit[x][y] == 0 and grid[x][y] == 0:
                                        visit[x][y] = 1
                                        count[x][y] += 1
                                        dist[x][y] += step
                                        qu.put((x, y))

        res = sys.maxsize
        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == 0 and count[i][j] == buildings:
                    res = min(res, dist[i][j])

        if res == sys.maxsize:
            return -1
        else:
            return res



