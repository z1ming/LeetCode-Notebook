# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
#
# 示例:
#
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row,col):
            return not (rows[col] or hills[row - col] or dales[row + col])
        # 放置皇后
        def place_queen(row,col):
            rows[col] = 1
            hills[row - col] = 1  # 主对角线
            dales[row + col] = 1  # 副对角线
        # 移除皇后
        def remove_queen(row,col):
            rows[col] = 0
            hills[row - col] = 0  # 主对角线
            dales[row + col] = 0  # 副对角线
        # 回溯
        def backtrack(row = 0,count = 0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n: # 如果放了n个皇后，则有一种解决方案
                        count += 1
                    else:
                        count = backtrack(row + 1,count)
                    remove_queen(row, col)
            return count

        rows = [0] * n
        hills = [0] * (2 * n - 1) # 主对角线
        dales = [0] * (2 * n - 1) # 副对角线
        return backtrack()