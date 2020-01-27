# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
# 示例 1:
#
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_n = sum(nums)
        if (sum_n + S) % 2 != 0 or sum_n < S:
            return 0
        return self.sub_set(nums, (S + sum_n) // 2)

    def sub_set(self, nums, S):
        dp = [0] * (S + 1)
        dp[0] = 1
        for num in nums:
            # 每一遍循环得到和值为i的方法数，以次更新
            for i in range(S, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[S]