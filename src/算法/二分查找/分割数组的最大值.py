# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 示例:
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# Python解法，不是python3.太难了，困难还是不会，，
class Solution(object):
    def splitArray(self, nums, m):
        # binary search for min_max
        left, right = sum(nums) / m, sum(nums)
        while left <= right:
            mid = right - ((right - left) >> 1)
            if self.valid_max(nums, m, mid) and (not self.valid_max(nums, m, mid - 1)):
                return mid
            else:
                if not self.valid_max(nums, m, mid):
                    left = mid + 1
                else:
                    right = mid - 1

        return right

    def valid_max(self, nums, k, max):
        n = len(nums)
        div = 1
        sum = nums[0]
        for i in range(1, n):
            if sum > max:
                return False
            if sum + nums[i] > max:
                div += 1
                sum = nums[i]
            else:
                sum += nums[i]
        # note that we have to ensure sum <= max
        return (sum <= max) and (div <= k)
