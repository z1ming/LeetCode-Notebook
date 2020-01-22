# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 将数组拉平
        array = [y for x in matrix for y in x]
        return heapq.nsmallest(k,array)[-1]