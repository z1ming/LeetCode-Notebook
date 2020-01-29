class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxa=-1
        for i in range(0,len(A)):
            if maxa<A[i] and A.count(A[i])==1:
                maxa=A[i]
        return maxa