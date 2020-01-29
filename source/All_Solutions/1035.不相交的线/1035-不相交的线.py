class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        if n * m == 0:
            return n + m
        d = [[0] * (m + 1) for _ in range(n + 1)]
        # DP compute
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    d[i][j] = d[i-1][j-1] +1
                else:
                    d[i][j] = max(d[i-1][j],d[i][j-1], d[i-1][j-1])

        return d[n][m]