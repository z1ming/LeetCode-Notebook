class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps==1 or arrLen==1:
            return 1
        m=min(steps,arrLen)
        dp=[0]*m
        dp[0]=dp[1]=1
        DP=[0]*m
        for _ in range(1,steps):         
            for i in range(m):
                if i ==0:
                    DP[i]=dp[0]+dp[1]
                elif i==(m-1):
                    DP[i]=dp[m-1]+dp[m-2]
                else:
                    DP[i]=dp[i-1]+dp[i]+dp[i+1]
            dp=DP.copy()
        return DP[0]%(10**9 + 7)