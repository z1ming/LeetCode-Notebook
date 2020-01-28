class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        temp = []
        for index, i in enumerate(A):
            if not temp:
                temp.append((i, index, i))
            else:
                while temp and temp[-1][0] > i:
                    temp.pop()
                if not temp:
                    temp.append((i, index, i * (index + 1)))
                else:
                    temp.append((i, index, temp[-1][-1] + i * (index - temp[-1][1])))
            result += temp[-1][-1]
        return result % (10 ** 9 + 7)