# 给定一个矩阵 A， 返回 A 的转置矩阵。
#
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#  
#
# 示例 1：
#
# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
# 示例 2：
#
# 输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        # 初始化二维矩阵res，将A的转置复制到res
        res = [[None]*row for i in range(col)]# 一定要加上None，为元素个数占位
        print(res)
        for i,r in enumerate(A):
            for j,c in enumerate(r):
                res[j][i] = c
        return res

# 时间复杂度：O(N*M)
# 空间复杂度： O(N*M)