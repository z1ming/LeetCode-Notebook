# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 题目中出现了数组的频数，想到利用哈希表，
        # “返回长度”可以A.用哈希表保存索引B.设置指针保存索引值，再计算长度
        # 使用三个字典分别保存x第一次出现、最后一次出现的索引，和x的个数
        left,right,count = {},{},{}
        res = len(nums)
        for i,x in enumerate(nums):
            if x not in left:  # 如果x已经在字典中则不需要再更新左索引
                left[x] = i
            right[x] = i
            count[x] = count.get(x,0) + 1 # count={x:出现次数}

        angle = max(count.values())
        for j in count:
            if count[j] == angle:
                res = min(res,right[j]-left[j]+1)
        return res
# 时间复杂度： O(N)，N是nums的长度，每个循环需要O（N）的时间
# 空间复杂度： O(N)，left,right,count使用的空间