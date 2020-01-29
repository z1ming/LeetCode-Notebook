class Solution:
    def longestDupSubstring(self, S: str) -> str:
        import functools
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        n = len(S)
        def test(l):
            p = pow(26,l,mod)
            cur = functools.reduce(lambda x,y:(x*26+y)%mod,A[:l])
            seed = {cur}
            for index in range(l,n):
                cur =(cur * 26 + A[index] - A[index-l] * p) % mod
                if cur in seed:
                    return index - l + 1
                seed.add(cur)
            return -1
        low,high = 0,n
        res = 0
        while low < high:
            mid = (low + high + 1) // 2
            pos = test(mid)
            if pos != -1:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res:res+low]

