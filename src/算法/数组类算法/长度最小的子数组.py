# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if (n < 1 or sum(nums) < s):
            return 0

        # 维护一个滑动窗口nums[i,j], nums[i...j] < s
        i = 0
        j = -1
        total = 0
        res = n + 1
        while i <= n - 1:
            if (j + 1 < n) and total < s:
                j += 1
                total += nums[j]
            else:
                total -= nums[i]
                i += 1

            if (total >= s):
                res = min(res, j - i + 1)
        if res == n + 1:
            return 0
        return res