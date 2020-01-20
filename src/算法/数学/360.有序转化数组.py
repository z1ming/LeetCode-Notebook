# 给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax2 + bx + c，请将函数值产生的数组返回。
#
# 要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。
#
# 示例 1：
#
# 输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
# 示例 2：
#
# 输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]

from functools import lru_cache
import bisect


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        @lru_cache(None)
        def get_calculate(num):
            return a * (num ** 2) + b * num + c

        length = len(nums)
        ans = []
        if a > 0:
            left = bisect.bisect_left(nums, -b / (2 * a)) - 1
            right = left + 1
            while left >= 0 or right < length:
                left_num = get_calculate(nums[left]) if left >= 0 else float('inf')
                right_num = get_calculate(nums[right]) if right < length else float('inf')
                if left_num <= right_num:
                    ans.append(left_num)
                    left -= 1
                else:
                    ans.append(right_num)
                    right += 1
        else:
            left = 0
            right = length - 1
            while left <= right:
                left_num = get_calculate(nums[left])
                right_num = get_calculate(nums[right])
                if left_num <= right_num:
                    ans.append(left_num)
                    left += 1
                else:
                    ans.append(right_num)
                    right -= 1
        return ans