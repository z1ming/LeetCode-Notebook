class Solution:
   def PredictTheWinner(self, nums: List[int]) -> bool:
       n = len(nums)
       if n % 2 == 0:
           return True
       dp = [[0]*n for _ in range(n)]
       for i in range(n):
           dp[i][i] = nums[i]
       for i in range(1, n):
           dp[i-1][i] = max(nums[i-1], nums[i])
       for i in range(n-2,-1,-1): 
           for j in range(i+2, n):
               dp[i][j] = max(nums[i] + min(dp[i+1][j-1], dp[i+2][j]),
                             nums[j] + min(dp[i+1][j-1], dp[i][j-2]))
       return dp[0][n-1] >= sum(nums) - dp[0][n-1]