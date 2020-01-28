class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        l1 = len(A) 
        l2 = len(B) 
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)] 
        for i in range(1,l1+1): 
            for j in range(1,l2+1): 
                if A[i-1] == B[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1 
        return max(max(row) for row in dp)