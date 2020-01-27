class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_n = sum(nums)
        if (sum_n+S)%2!=0 or sum_n<S:
            return 0
        return self.sub_set(nums,(S+sum_n)//2)
        
    def sub_set(self,nums,S):
        dp = [0]*(S+1)
        dp[0] = 1
        for num in nums:
            #每一遍循环得到和值为i的方法数，以次更新
            for i in range(S,num-1,-1):
                dp[i] += dp[i-num]
        return dp[S]