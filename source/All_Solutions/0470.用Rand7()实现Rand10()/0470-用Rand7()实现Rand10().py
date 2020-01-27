class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n=rand7()
        while n>5:
            n=rand7()
        i=rand7()
        while i==4:
            i=rand7()
        if i<4:
            j=0
        else:
            j=5
        return n+j

