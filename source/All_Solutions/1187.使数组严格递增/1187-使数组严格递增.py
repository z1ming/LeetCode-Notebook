class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        maxV = 1000000001
        dp = [[maxV for i in range(n+1)] for _ in range(n+1)]
        
        #initial
        arr2.sort()
        dp[0][0] = -1
        
        for i in range(1,n+1):
            for j in range(0,i+1):
                if arr1[i-1] > dp[j][i-1]:
                    dp[j][i] = arr1[i-1]
                    
                if j > 0:
                    loc = bisect.bisect_right(arr2,dp[j-1][i-1])
                    if loc < len(arr2):
                        dp[j][i] = min(dp[j][i],arr2[loc])
                        
                if i == n and dp[j][i] != maxV:
                    return j
            
        return -1

