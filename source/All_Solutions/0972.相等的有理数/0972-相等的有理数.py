class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s=self.handle(S)
        t = self.handle(T)
        return abs(float(s)-float(t))<0.00000001
    def handle(self,s):
        p = s.find('(')
        if p!=-1:
            cycle = s[p+1:-1]
            s = s[:p]+cycle*15
        return s