class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(A)
        while n :
            idx = A.index(n)
            res.append(idx+1)
            A = A[:idx+1][::-1]+A[idx+1:]
            res.append(n)
            A = A[:n][::-1]+A[n:]
            n -= 1
        # print(A)
        return res