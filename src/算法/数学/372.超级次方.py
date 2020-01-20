# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
# 示例 1:
#
# 输入: a = 2, b = [3]
# 输出: 8
# 示例 2:
#
# 输入: a = 2, b = [1,0]
# 输出: 1024

class Solution:
    def qpow(self,x,n,m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m
            n >>= 1
        return ans
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337