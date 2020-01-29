class Solution(object):
    def palindromePartition(self, s, k):
        n = len(s)
        if n == k:
            return 0
        # 计算cost数组
        cost = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j - 1, -1, -1):
                if j - i <= 2:
                    if s[i] != s[j]:
                        cost[i][j] = 1
                else:
                    cost[i][j] = cost[i + 1][j - 1] + (1 if s[i] != s[j] else 0)
        dp = [[float("inf")] * (k + 1) for _ in range(n)]
        # 初始化
        for i in range(n):
            dp[i][1] = cost[0][i]
        for K in range(2, k + 1):
            for i in range(n):
                for j in range(i):
                    dp[i][K] = min(dp[j][K - 1] + cost[j + 1][i], dp[i][K])
        return dp[-1][-1]