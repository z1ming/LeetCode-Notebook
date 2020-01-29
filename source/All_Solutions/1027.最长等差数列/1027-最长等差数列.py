class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        def function(s):
            result={}
            maxv=2
            for i in range(1,len(s)):
                for j in range(i):
                    if (s[j]-s[i],j) not in result:
                        result[(s[j]-s[i],i)]=2
                    else:
                        result[(s[j]-s[i],i)]=result[(s[j]-s[i],j)]+1
                        if result[(s[j]-s[i],i)]>maxv:
                            maxv=result[(s[j]-s[i],i)]
            return maxv
        return function(A)