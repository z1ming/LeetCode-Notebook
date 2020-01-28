class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pp, p = 1, int(s[0]!='0'and s[0]!='*') + 9*int(s[0]=='*')
        print(pp,p)
        for i in range(1, len(s)):
            if s[i]=='*':
                if s[i-1]=='*':
                    pp, p = p, pp*15+p*9
                elif s[i-1]=='1':
                    pp, p = p, pp*9+p*9
                elif s[i-1]=='2':
                    pp, p = p, pp*6+p*9
                else:
                    pp, p = p, p*9
            elif s[i]=='0':
                if s[i-1]=='*':
                    pp, p = p, pp*2
                elif s[i-1]=='1':
                    pp, p = p, pp
                elif s[i-1]=='2':
                    pp, p = p, pp
                else:
                    pp, p = p, 0
            elif int(s[i])>6:
                if s[i-1]=='*':
                    pp, p = p, pp+p
                elif s[i-1]=='1':
                    pp, p = p, pp+p
                else:
                    pp, p = p, p
            else:
                if s[i-1]=='*':
                    pp, p = p, pp*2+p
                elif 1<=int(s[i-1])<=2:
                    pp, p = p, pp+p
                else:
                    pp, p = p, p
        return (p%(10**9+7))