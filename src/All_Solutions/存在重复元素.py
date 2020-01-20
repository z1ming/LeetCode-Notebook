# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            else:
                set1.add(nums[i])
        return False