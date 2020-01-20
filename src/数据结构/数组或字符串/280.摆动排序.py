# 给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。
#
# 示例:
#
# 输入: nums = [3,5,2,1,6,4]
# 输出: 一个可能的解答是 [3,5,1,6,2,4]
# 方法一：先排序，从nums[1]开始两两交换
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i += 2
# time:O(NlogN)
# space:O(1),通常，使用堆排序，空间复杂度是O(1)

# 方法二：一遍交换之令人惊讶
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if (i % 2 == 0 and nums[i] > nums[i+1]) or \
            (i % 2 == 1 and nums[i] < nums[i+1]):
                nums[i],nums[i+1] = nums[i+1],nums[i]