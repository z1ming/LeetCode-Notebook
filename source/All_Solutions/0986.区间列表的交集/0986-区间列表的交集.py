class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B)
        ans = []
        i, j = 0, 0
        while i < m and j < n:
            l, r = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if l <= r:
                ans += [[l, r]]
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans