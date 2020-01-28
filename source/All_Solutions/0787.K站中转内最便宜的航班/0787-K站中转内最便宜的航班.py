class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        ans = float('inf')
        dp = [[-1]*(K+1) for _ in range(n)]
        for i in range(K+1):
            dp[dst][i] = 0
        for i,j,k in flights:
            if j == dst:
                dp[i][0] = k

        for t in range(1,K+1):
            for i,j,k in flights:
                if dp[j][t-1] != -1:
                    dp[i][t] = min(dp[i][t], dp[j][t-1]+k) if dp[i][t]>0 else dp[j][t-1]+k

        for i in dp[src]:
            ans = min(i, ans) if i>0 else ans
        if ans == float('inf'):
            ans = -1
        return ans