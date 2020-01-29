class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        ct=0
        n = len(A)
        flag = [0]*n
        sm = 0
        for i in range(n-K+1):
            if (sm+A[i])%2==0:
                ct+=1
                flag[i]=1
            sm+=flag[i]
            if i-K+1>=0:
                sm-=flag[i-K+1]
        for i in range(n-K+1,n):
            if (sm+A[i])%2==0:return -1
            if i-K+1>=0:
                sm-=flag[i-K+1]
        return ct