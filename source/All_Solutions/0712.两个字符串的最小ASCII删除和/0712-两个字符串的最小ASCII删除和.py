class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m,n=len(s1),len(s2)
        dp=[[float('inf') for _ in range(n+1)] for i in range(m+1)]
        dp[0][0]=0
        for i in range(m):
            dp[i+1][0]=dp[i][0]+ord(s1[i])
        for i in range(n):
            dp[0][i+1]=dp[0][i]+ord(s2[i])
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
        return dp[-1][-1]