from itertools import product
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        is_parlindrome = lambda string: string == string[::-1]
        l, r = int(L) ** 0.5, int(R) ** 0.5
        A, s = ["012"] * (((len(R) + 1) // 2 + 1) // 2), 0
        for a in product(*A):
            a = "".join(a).lstrip("0") or "0"
            for i in (int(a + a[::-1]), int(a + a[:-1][::-1])):
                s += (l <= i <= r and is_parlindrome(str(i ** 2)))
        return s + (int(L) <= 9 <= int(R))