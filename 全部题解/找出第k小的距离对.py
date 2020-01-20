# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
#
# 示例 1:
#
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
# 提示:
#
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
# 太难了，看不懂，困难的题目还是不会
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
