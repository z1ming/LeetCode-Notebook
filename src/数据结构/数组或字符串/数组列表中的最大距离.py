# 给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离
#
# 示例 1：
#
# 输入：
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# 输出： 4
# 解释：
# 一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
#  
#
# 注意：
#
# 每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
# 所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
# m 个数组中所有整数的范围在 [-10000, 10000] 内。

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1,len(arrays)):
            res = max(res,(arrays[i][-1] - min_val),(max_val - arrays[i][0]))
            min_val = min(min_val,arrays[i][0])
            max_val = max(max_val,arrays[i][-1])
        return res