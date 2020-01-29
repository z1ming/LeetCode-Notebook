class Solution:
# 思路：dp
# a,b分别记录前i项最大值
# 对于位置i, 最大值=前L项+b[i-L] 或者 前M项]+a[i-M] 或者前i-1位置的最大值
# res = max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        a, b = [0] * n, [0] * n  # a是L,b是M
        res = 0
        for i in range(1, n):
            A[i] += A[i - 1]
        for i in range(n):
            a[i] = A[i] if i < L else max(a[i - 1], A[i] - A[i - L])
            b[i] = A[i] if i < M else max(b[i - 1], A[i] - A[i - M])
            res = A[i] if i < L + M else max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])
        return res
