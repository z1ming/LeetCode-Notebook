class Solution:
    def baseNeg2(self, N: int) -> str:
        def function(n):
            result=""
            while True:
                result=str(n%2)+result
                n=math.ceil(n/-2)
                if n==0:
                    break
            return result
        return function(N)