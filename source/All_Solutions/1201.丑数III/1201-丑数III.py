class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd
        def lcm(x,y):
            return x * y // gcd(x,y)

        # use inclusion-exclusion theory to find ugly numbers in [2,x]
        def lower(x):
            lcm1 = lcm(a,b)
            lcm2 = lcm(b,c)
            lcm3 = lcm(a,c)
            lcm4 = lcm(lcm1,lcm2)
            return x // a + x // b + x // c + x // lcm4 - x // lcm1 - x // lcm2 - x // lcm3

        # use binary search to find x: s.t. lower(x) == n
        lo = 0
        hi = int(2e9)
        while lo != hi:
            mid = lo + hi >> 1
            if lower(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo