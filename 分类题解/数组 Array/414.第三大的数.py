# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
#
# 示例 1:
#
# 输入: [3, 2, 1]
#
# 输出: 1
#
# 解释: 第三大的数是 1

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums = sorted(nums,reverse=True)
        return nums[2]
# 时间复杂度：O(n)?
# 空间复杂度：O(n)?