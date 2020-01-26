# 给你一个 2D 矩阵 matrix，请计算出从左上角 (row1, col1) 到右下角 (row2, col2) 组成的矩形中所有元素的和。


# 上述粉色矩形框内的，该矩形由左上角 (row1, col1) = (2, 1) 和右下角 (row2, col2) = (4, 3) 确定。其中，所包括的元素总和 sum = 8。

# 示例：

# 给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix == [] or matrix == [[]]: return
        row, col = len(matrix), len(matrix[0])
        sum_arr = [[0] * (col + 1) for _ in range(row + 1)]
        self.update_dic = collections.defaultdict(int)

        for i in range(row):
            left = 0
            for j in range(col):
                sum_arr[i + 1][j + 1] = sum_arr[i][j + 1] + left + matrix[i][j]
                left += matrix[i][j]
        self.sum_arr = sum_arr
        self.matrix = matrix

    # 更新时间复杂度 O(1)
    def update(self, row: int, col: int, val: int) -> None:
        self.update_dic[(row, col)] = val - self.matrix[row][col]

    # 求和时间复杂度 O(N)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p1 = self.sum_arr[row2 + 1][col2 + 1]
        p2 = self.sum_arr[row2 + 1][col1]
        p3 = self.sum_arr[row1][col2 + 1]
        p4 = self.sum_arr[row1][col1]
        s = p1 - p2 - p3 + p4
        for (row, col), val in self.update_dic.items():
            if row1 <= row <= row2 and col1 <= col <= col2: s += val
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

