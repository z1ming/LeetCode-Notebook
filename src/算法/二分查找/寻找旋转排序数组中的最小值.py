# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[0]
        else:
            while left < right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return nums[pivot + 1]
                else:
                    if nums[pivot] < nums[right]:
                        right = pivot
                    else:
                        left = pivot
        return nums[pivot]