class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        dp = set(range(10))
        for i in range(1, N):
            prev_dp = dp
            dp = set()
            for num in prev_dp:
                if num == 0:
                    continue
                left = num % 10
                if left >= K:
                    dp.add(num*10+left-K)
                if left + K <= 9:
                    dp.add(num*10+left+K)
        return sorted(list(dp))