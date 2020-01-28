class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 3:
            return N
        result = 3
        length = 1
        dp = [0] * N
        dp[0],dp[1],dp[2] = 1,2,3
        temp1 = [(3,1)]
        temp2 = []
        for i in range(3,N):
            pre = dp[i-3]*2,dp[i-3]
            max_e = pre[0]
            for group in temp1:
                k = group[0] + group[1]
                max_e = max(max_e,k)
                if k > pre[0]:
                    temp2.append((k,group[1]))
            temp2.append(pre)
            temp1 = temp2
            temp2 = []
            dp[i] = max_e
        return dp[-1]

