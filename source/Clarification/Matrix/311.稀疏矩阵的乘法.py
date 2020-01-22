# 给定两个 稀疏矩阵 A 和 B，请你返回 AB。你可以默认 A 的列数等于 B 的行数。
#
# 请仔细阅读下面的示例。
#
# 示例：
#
# 输入:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
# 输出:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return [[]]

        a,c,b = len(A),len(B),len(B[0])
        AB = [[0 for _ in range(b)] for _ in range(a)]

        for i in range(a):
            for j in range(c):
                if A[i][j] != 0:
                    for k in range(b):
                        if B[j][k] != 0:
                            AB[i][k] += A[i][j] * B[j][k]
        return AB