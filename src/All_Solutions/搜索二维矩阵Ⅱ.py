# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 暴力算法
        for row in matrix:
            if target in row:
                return True

        return False
# 时间复杂度：O(MN)
# 空间复杂度：O(1)

# 方法二：
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        # 从左下角开搜
        row = len(matrix) - 1
        col = 0
        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            if matrix[row][col] < target:
                col += 1
        return False
# 时间复杂度：O（m+n）
# 空间复杂度：O(1)