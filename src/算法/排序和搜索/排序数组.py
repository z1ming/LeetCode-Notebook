# 给定一个整数数组 nums，将该数组升序排列。
#
#  
#
# 示例 1：
#
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums,0,len(nums)-1)

    def quick_sort(self,nums,start,end):
        left = start
        right = end
        # 递归的退出条件
        if left>right:
            return
        mid = nums[start]

        while left < right:
            while left < right and nums[right] >= mid:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        self.quick_sort(nums,start,left-1)
        self.quick_sort(nums,left+1,end)
        return nums