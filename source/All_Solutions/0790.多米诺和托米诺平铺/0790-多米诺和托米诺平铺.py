class Solution(object):
    def numTilings(self, N):
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]
        for _ in xrange(N):
            ndp = [0, 0, 0, 0]
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD
            dp = ndp

        return dp[0]

