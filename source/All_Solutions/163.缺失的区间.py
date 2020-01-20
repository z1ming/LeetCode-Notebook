# 给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
#
# 示例：
#
# 输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        nums = [lower-1]+nums+[upper+1]
        for i in range(len(nums)-1):
            d = nums[i+1] - nums[i]
            if d == 2:
                ans.append(str(nums[i]+1))
            elif d > 2:
                ans.append("{}->{}".format(nums[i]+1, nums[i+1]-1))
        return ans
