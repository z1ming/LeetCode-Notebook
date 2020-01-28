class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 对 A 进行排序，若整个数组同加同减那么差值就是 A[-1]-A[0] 。
        #半加半减情况则可将 A 视为俩部分 A1<A2，为了使差值最小，只能 A1 同加， A2 同减。那么整个 A 的最大值只能是 A1 尾或 A2 尾，最小值只能是 A1 头或 A2 头，比较这4个值就可以求得差值。

        l = len(A)
        if l < 2:return 0
        A.sort()
        res = A[l-1]-A[0]
        for i in range(1,l):
            minu = min(A[0] + K, A[i] - K)
            maxu = max(A[i-1] + K, A[l-1] - K)
            res = min(res, maxu - minu)
        return res