class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        # if len(s) == 0 : return 0
        ls = list(s.strip())
        if not ls: return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))