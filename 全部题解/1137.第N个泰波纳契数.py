# 泰波那契序列 Tn 定义如下： 
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
#
#  
#
# 示例 1：
#
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# 方法一：递归虽然可以，但是会超时
import functools
class Solution:
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0:return 0
        if n == 1:return 1
        if n == 2:return 1
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # 递归到底应该怎么理解???
        # 按公式直接写就行
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
# 时间复杂度：O(N)
# 空间复杂度：O(1)

# 方法二：迭代，可通过
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a,b,c = 0,1,1
        while n>2:
            res = a+b+c
            a,b,c = b,c,res
            n -= 1
        return res