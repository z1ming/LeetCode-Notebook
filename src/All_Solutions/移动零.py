# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
# 1.必须在原数组上操作，不能拷贝额外的数组。
# 2.尽量减少操作次数。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        n = len(nums)
        while j < n:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1,n):
            nums[k] = 0
        return nums