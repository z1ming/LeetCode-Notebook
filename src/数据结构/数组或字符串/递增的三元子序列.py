# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num, sec_num = float('inf'), float('inf')  # 初始化最小值，次小值

        for i in nums:
            min_num = min(i, min_num)  # 维护min_num为最小值
            if i > min_num:  # 找到了次小值
                sec_num = min(i, sec_num)
            if i > sec_num:  # 找到了第三大的数
                return True

        return False
