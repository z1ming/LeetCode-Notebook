# 写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
#
# 1 是丑数。
# n 不超过1690。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*n
        l_a = 0
        l_b = 0
        l_c = 0
        dp[0] = 1
        for i in range(1,n):
            dp[i] = min(2*dp[l_a],3*dp[l_b],5*dp[l_c])
            if dp[i] >= 2*dp[l_a]:
                l_a += 1
            if dp[i] >= 3*dp[l_b]:
                l_b += 1
            if dp[i] >= 5* dp[l_c]:
                l_c += 1
        return dp[-1]