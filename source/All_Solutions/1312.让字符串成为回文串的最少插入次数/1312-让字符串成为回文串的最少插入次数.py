class Solution:
    def minInsertions(self, s: str) -> int:
        from functools import lru_cache
        @lru_cache(300000)
        def F(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return F(i + 1, j - 1)
            return 1 + min(F(i + 1, j), F(i, j - 1))
        return F(0, len(s) - 1)