class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_length = 1
        pre_length = 0
        result = 0
        for i in range((len(s) - 1)):
            if s[i] == s[i + 1]:
                cur_length = cur_length + 1
            else:
                pre_length = cur_length
                cur_length = 1
                
            if pre_length >= cur_length:
                result = result + 1
        return result