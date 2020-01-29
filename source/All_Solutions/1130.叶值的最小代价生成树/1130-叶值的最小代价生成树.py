class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp=[[0]*n for i in range(n)]
        mx=[[0]*n for i in range(n)]
        for i in range(n):
            mx[i][i]=arr[i]
        for l in range(1,n):
            for i in range(n-l):
                j = i+l
                for k in range(i,j):
                    tmp = dp[i][k]+dp[k+1][j]+mx[i][k]*mx[k+1][j]
                    if dp[i][j] == 0 or dp[i][j]>tmp:
                        dp[i][j]=tmp
                    mx[i][j] = max(mx[i][k],mx[k+1][j],mx[i][j])       
        return dp[0][n-1]
