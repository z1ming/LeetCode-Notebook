# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
#
# 示例:
#
# nums = [1, 2, 3]
# target = 4
#
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# 请注意，顺序不同的序列被视作不同的组合。
#
# 因此输出为 7。
# 进阶：
# 如果给定的数组中含有负数会怎么样？
# 问题会产生什么变化？
# 我们需要在题目中添加什么限制来允许负数的出现？

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i]:和为i的组合的个数
        n = len(nums)
        if n == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target+1)]
        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这一步要加深体会
        dp[0] = 1
        for i in range(1,target + 1):
            for j in range(n):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[-1]