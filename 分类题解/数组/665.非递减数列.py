# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
#
# 示例 1:
#
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 示例 2:
#
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def is_sort(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                t1 = is_sort(nums[:i]+nums[i+1:])
                t2 = is_sort(nums[:i+1]+nums[i+2:])
                return t1 or t2
        return True

