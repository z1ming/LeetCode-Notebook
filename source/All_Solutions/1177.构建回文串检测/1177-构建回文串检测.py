class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        d = [0]*len(s)
        k = 0
        for i, c in enumerate(s):
            k ^= 1 << (ord(c) - ord("a"))
            d[i]=k
        ans = []
        for start, end, k in queries:
            if k<13:
                c = d[end]
                if start > 0:
                    c ^= d[start-1]
                c = (c & 0x55555555) + ((c >> 1) & 0x55555555)
                c = (c & 0x33333333) + ((c >> 2) & 0x33333333)
                c = (c & 0x0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f)
                c = (c & 0x00ff00ff) + ((c >> 8) & 0x00ff00ff)
                c = (c & 0x0000ffff) + ((c >> 16) & 0x0000ffff)
                ans.append(c <= (2 * k + 1))
            else:
                ans.append(True)
        return ans
