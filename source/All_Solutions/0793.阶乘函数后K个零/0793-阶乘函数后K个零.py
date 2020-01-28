class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def f(n):
            res=0        
            while n>0:
                res+=n//5
                n//=5
            return res
        
        low,up=0,5*10**9    
        while up>low+1:
            mid=(low+up)//2
            tmp=f(mid)
            if K==tmp:return 5
            if K>tmp:low=mid
            if K<tmp:up=mid
        return 0