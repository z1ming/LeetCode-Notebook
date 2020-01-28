class Solution:
    def maxSubarraySumCircular(self, A):

        if not A:
            return 0
        # 记录前i最最小值
        dp = []
        cur_min_sum = 0
        all_sum = 0
        res = float("-inf")
        for a in A:
            all_sum += a
            res = max(res, all_sum - cur_min_sum)
            cur_min_sum = min(cur_min_sum, all_sum)
            dp.append(all_sum)
        # print(all_sum, cur_min_sum, dp)
        n = len(dp)
        suffix = [0] * n
        suffix[-1] = dp[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], dp[i])
        # print(suffix)
        for idx, a in enumerate(A):
            all_sum += a
            res = max(res, all_sum - suffix[idx])
            cur_min_sum = min(cur_min_sum, all_sum)
        return res