class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[0], -1*x[1]])
        left, mx, res = -1, -1, 0
        for l, r in intervals:
            if l != left and mx < r:
                left, mx = l, max(mx, r)
                res += 1
        return res