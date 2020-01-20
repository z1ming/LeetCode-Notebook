# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
# 示例 2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
# 说明:
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        gap = math.ceil((max_num - min_num)/(n-1))
        bucket = [[float("inf"),float("-inf")] for _ in range(n -1)]
        # 求出每个桶的最大值，和最小值
        for num in nums:
            if num == max_num or num == min_num:
                continue
            loc = (num - min_num) // gap
            bucket[loc][0] = min(num,bucket[loc][0])
            bucket[loc][1] = max(num,bucket[loc][1])

        # 遍历整个桶
        preMin = min_num
        res = float("-inf")
        for x ,y in bucket:
            if x == float("inf"):
                continue
            res = max(res,x - preMin)
            preMin = y
        res = max(res,max_num - preMin)
        return res