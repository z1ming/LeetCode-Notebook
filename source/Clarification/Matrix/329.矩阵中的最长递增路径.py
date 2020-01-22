# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 示例 2:
#
# 输入: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]

            val = matrix[i][j]
            lookup[i][j] = 1 + max(
                dfs(i + 1, j) if 0 <= i + 1 < row and 0 <= j < col and matrix[i + 1][j] > val else 0,
                dfs(i - 1, j) if 0 <= i - 1 < row and 0 <= j < col and matrix[i - 1][j] > val else 0,
                dfs(i, j + 1) if 0 <= i < row and 0 <= j + 1 < col and matrix[i][j + 1] > val else 0,
                dfs(i, j - 1) if 0 <= i < row and 0 <= j - 1 < col and matrix[i][j - 1] > val else 0,
            )

            return lookup[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))


