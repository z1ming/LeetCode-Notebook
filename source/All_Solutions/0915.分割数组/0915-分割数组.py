class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lmaxv = A[0]
        maxv = A[0]
        l = 0
        for i in xrange(len(A)):
            if A[i] < lmaxv:
                lmaxv = maxv
                l = i
            elif A[i] > maxv:
                maxv = A[i]
        return l + 1