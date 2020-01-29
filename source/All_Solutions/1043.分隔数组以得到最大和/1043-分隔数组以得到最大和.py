class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        if not n:
            return 0
        elif K >= n:
            return max(A)*n
        else:
            grid = [[0]*n for i in range(n)]
            for i in range(n):
                grid[i][i] = A[i]
            for i in range(1,K):
                for j in range(n-i):
                    grid[j][j+i] = max(grid[j][j+i-1],A[j+i])
            dp = A[:]
            for i in range(K):
                dp[i] = grid[0][i]*(i+1)
            for i in range(K,n):
                dp[i] += dp[i-1]
                for j in range(1,K):
                    dp[i] = max(grid[i-j][i]*(j+1)+dp[i-j-1],dp[i])
            return dp[-1]
