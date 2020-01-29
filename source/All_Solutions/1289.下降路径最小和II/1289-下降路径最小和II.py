class Solution:
    def minFallingPathSum(self, arr) -> int:

        dp = arr[0]
        if len(dp) == 1: return dp[0]
        tmp = sorted(dp)
        num1 = tmp[0]
        num2 = tmp[1]
        for i in range(1, len(arr)):
            tmp = dp.copy()
            nxt_num1 = float("inf")
            nxt_num2 = float("inf")
            for j in range(len(arr[0])):

                if tmp[j] == num1:
                    tmp[j] = num2 + arr[i][j]
                else:
                    tmp[j] = num1 + arr[i][j]
                # 找最小两个值
                if tmp[j] < nxt_num1:
                    nxt_num2 = nxt_num1
                    nxt_num1 = tmp[j]
                elif tmp[j] < nxt_num2:
                    nxt_num2 = tmp[j]
            num1 = nxt_num1
            num2 = nxt_num2
            dp = tmp
        return min(dp)