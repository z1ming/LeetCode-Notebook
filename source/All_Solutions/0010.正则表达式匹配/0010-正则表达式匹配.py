class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1,m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]