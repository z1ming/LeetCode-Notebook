class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return LCS(s,s[::-1]) + k >= len(s)

def LCS(a, b):
    m, n = len(a)+1, len(b)+1
    F = [[0]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if a[i-1]==b[j-1]:
                F[i][j]=F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    return F[m-1][n-1]