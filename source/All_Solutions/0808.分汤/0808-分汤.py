class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4450:
            return 1
        def dfs(a, b):  # 返回A先分配完的概率、B先分配完的概率和同时分配完的概率
            if a == 0:
                return (1, 0, 0) if b > 0 else (0, 0, 1)
            if b == 0:
                return 0, 1, 0
            if (a, b) not in dp:
                x1, y1, z1 = dfs(max(a-100, 0), b)
                x2, y2, z2 = dfs(max(a-75, 0), max(b-25, 0))
                x3, y3, z3 = dfs(max(a-50, 0), max(b-50, 0))
                x4, y4, z4 = dfs(max(a-25, 0), max(b-75, 0))
                dp[a, b] = (x1+x2+x3+x4)/4, (y1+y2+y3+y4)/4, (z1+z2+z3+z4)/4
            return dp[a, b]
        dp = {}
        x, y, z = dfs(N, N)
        return x+z/2