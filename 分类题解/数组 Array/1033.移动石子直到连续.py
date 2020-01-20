# 三枚石子放置在数轴上，位置分别为 a，b，c。
#
# 每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
#
# 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
#
# 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
#
#  
#
# 示例 1：
#
# 输入：a = 1, b = 2, c = 5
# 输出：[1, 2]
# 解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        tmp = [a,b,c] # 先对xyz赋值
        tmp.sort()
        x,y,z = tmp[0],tmp[1],tmp[2]
        if x + 1 == y and y + 1 == z: # a,b,c连续
            return [0,0]
        else:
            if y-x == 2 or z-y == 2 or (x+1 == y or y + 1 == z):  # 中间隔一个或者有两个挨着
                minimum_moves = 1
            else:
                minimum_moves = 2
            maximum_moves = (y-x)+(z-y)-2
        return [minimum_moves,maximum_moves]