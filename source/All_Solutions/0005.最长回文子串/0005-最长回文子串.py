# dp[i,i] = (dp[i+1,j-1] and Si == Sj)
# 初始状态：dp(i,i) = true
#           dp(i,i+1) = (Si == Si+1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 边界条件
        if n < 2: return s

        dp = [[False for _ in range(n)] for _ in range(n) ]
        start, max_len = 0, 1
        # 初始化
        for i in range(n):
            dp[i][i] = True
        # 动态规划
        # b a b a d
        # ^ ^
        # i j
        for j in range(1,n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 更新start，max_len的值
                if dp[i][j]:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        start = i
                        max_len = cur_len
        return s[start:start+max_len]
