# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: 6

# 先对数组进行排序，返回数组前两个负数和最后一个正数，或后3个正数的乘积，取最大值。
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3],nums[0]*nums[1]*nums[-1])

# 时间复杂度：O(NlogN)，N为数组的长度，排序的时间复杂度为NlogN吗？
# 空间复杂度：O(logN)，排序使用的空间