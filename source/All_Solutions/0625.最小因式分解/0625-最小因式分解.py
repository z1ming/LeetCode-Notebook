class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a==1:
            return 1
        stack = []
        for i in range(9,1,-1):
            while a % i == 0:
                a = a // i
                stack.append(i)
        if a != 1:
            return 0
        else:
            ans = 0
            while stack:
                ans = 10 * ans
                ans += stack.pop()
            return ans if ans < 2**31 -1 else 0

