# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

# 定义三元素：队列、节点、已访问元素之一：
# 节点
# 一般用类表示
class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])

        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                if i == 0:
                    return new_vertex.step

                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
        return -1