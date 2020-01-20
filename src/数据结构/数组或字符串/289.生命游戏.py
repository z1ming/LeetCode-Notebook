# 根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
# 示例:
#
# 输入:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# 输出:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 通过本例我们将学习如何搜素一共二维数组
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def countCeil(x:int,y:int) -> int:
            count = 0
            for x_offset in range(-1,2):
                for y_offset in range(-1,2):
                    if x_offset == y_offset == 0:
                        continue
                    if 0<= x + x_offset < row and 0 <= y + y_offset < col:
                        count += board[x + x_offset][y+ y_offset] & 0x0F
            if count == 3 or (board[x][y] and count == 2):
                count = 1
            else:
                count = 0
            board[x][y] |= (count <<4)  # |=意思是按位或

        for x in range(row):
            for y in range(col):
                countCeil(x, y)
        for x in range(row):
            for y in range(col):
                board[x][y] = (board[x][y] & 0xF0) >> 4