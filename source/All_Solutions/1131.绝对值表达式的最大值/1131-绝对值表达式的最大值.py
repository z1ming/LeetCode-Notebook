class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n=len(arr1)
        d=[[],[],[],[]]
        b=[[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(n):
            for j in range(4):
                d[j]+=[arr1[i]+b[j][0]*arr2[i]+b[j][1]*i]
        return max([max(d[i])-min(d[i]) for i in range(4)])
