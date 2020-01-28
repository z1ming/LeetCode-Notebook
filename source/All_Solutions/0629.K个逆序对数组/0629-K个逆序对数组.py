class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for i in range(n + 1)] 
        dp[0][0] = 1   
        for i in range(1, n + 1):
            dp[i][0] = 1    
            for j in range(1, k + 1):
                if j>=i: 
                    dp[i][j]=(dp[i][j-1]+dp[i-1][j]-dp[i-1][j-i]) % mod
                else:
                    dp[i][j]=(dp[i][j-1]+dp[i-1][j]) % mod
        return dp[n][k]