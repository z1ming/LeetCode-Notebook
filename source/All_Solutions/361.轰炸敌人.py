# 想象一下炸弹人游戏，在你面前有一个二维的网格来表示地图，网格中的格子分别被以下三种符号占据：
#
# 'W' 表示一堵墙
# 'E' 表示一个敌人
# '0'（数字 0）表示一个空位
#
#
# 请你计算一个炸弹最多能炸多少敌人。
#
# 由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。
#
# 注意：你只能把炸弹放在一个空的格子里
#
# 示例:
#
# 输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# 输出: 3
# 解释: 对于如下网格
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# 假如在位置 (1,1) 放置炸弹的话，可以炸到 3 个敌人

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        r = len(grid)
        c = len(grid[0])

        def cal(row,col):
            res = 0
            left,right = col - 1,col + 1
            while left >= 0 and grid[row][left] != "W":
                if grid[row][left] == 'E':
                    res += 1
                left -= 1
            while right < c and grid[row][right] != 'W':
                if grid[row][right] == 'E':
                    res += 1
                right += 1
            up,down = row - 1,row + 1
            while up >= 0 and grid[up][col] != 'W':
                if grid[up][col] == 'E':
                    res += 1
                up -= 1
            while down < r and grid[down][col] != 'W':
                if grid[down][col] == 'E':
                    res += 1
                down += 1
            return res
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "0":
                    res = max(res,cal(i,j))
        return res


