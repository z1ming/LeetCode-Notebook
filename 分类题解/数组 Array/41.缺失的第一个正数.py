# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1

        if n == 1:
            return 2
        # 用1替换负数，0，和大于n的数
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # 使用索引和数字符号作为检查器
        # 例如，如果nums[1]是负数说明在数组中出现了数字1，如果
        # nums[2]是正数说明数字2没有出现
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        for i in range(1,n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n

        return n+1