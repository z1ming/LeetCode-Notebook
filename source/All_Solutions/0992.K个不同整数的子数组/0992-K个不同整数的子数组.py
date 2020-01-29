class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        B = [0] * (max(A) + 1)
        l = j = res = 0
        c = 1
        for i, n in enumerate(A):
            #print l,c,res,B
            if B[n] == 0:
                l += 1
                if l > K:
                    c = 1
                    B[A[j]] -= 1
                    j += 1
                    l -= 1
            B[n] += 1
            while B[A[j]] != 1:
                B[A[j]] -= 1
                c += 1
                j += 1
            if l == K:
                res += c
        return res