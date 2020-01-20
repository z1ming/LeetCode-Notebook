# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
# 说明:
# 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
#
# 示例:
#
# 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = [0]
        for i in nums:
            p += [p[-1] + i]
        ans = 0
        q = []
        for pi in p[::-1]:
            i,j = pi + lower,pi + upper
            l = bisect.bisect_left(q, i)
            r = bisect.bisect_right(q, j)
            ans += r - l
            bisect.insort(q, pi)
        return ans