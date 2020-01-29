class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        m = {}

        for a,b in dominoes:
            if a > b:
                a,b = b,a
            if (a,b) not in m:
                m[(a,b)] = 0
            m[(a,b)] += 1

        count = 0

        for i in m.values():
            if i > 1:
                count += i*(i-1)//2

        return count