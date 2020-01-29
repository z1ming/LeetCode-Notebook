class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[float("inf")] * len(A) for _ in range(len(A))]
        for i in range(len(A)-1):
            dp[i][i+1] = 0
        for d in range(2,len(A)):
            for i in range(0, len(A)-d):
                j = i+d
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        return dp[0][len(A)-1]