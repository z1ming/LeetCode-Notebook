class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        return ''.join(sorted(list(T), key=lambda x:S.find(x)))
