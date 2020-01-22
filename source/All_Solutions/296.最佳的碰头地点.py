# 有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。

# 给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。

# 1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。

# 示例：

# 输入:

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# 输出: 6

# 解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
#      (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        n, m = len(grid), len(grid[0])
        lx, ly = [], []
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    lx.append(x)
                    ly.append(y)
        lx.sort()
        ly.sort()
        cnt = len(lx)
        mx, my = lx[cnt >> 1], ly[cnt >> 1]
        res = 0
        for x in lx:    res += abs(x - mx)
        for y in ly:    res += abs(y - my)
        return res