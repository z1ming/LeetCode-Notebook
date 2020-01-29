class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ans, r, d = 0, 0, [(i - ranges[i], i + ranges[i]) for i in range(n + 1)]
        while r < n:
            l = max(d[i][1] for i in range(r, min(r + 101, n + 1)) if r >= d[i][0])
            if l == r: 
                return -1
            ans, r = ans + 1, l
        return ans