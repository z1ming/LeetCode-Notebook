class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        temp = []
        for i, j in enumerate(s):
            if not temp:
                temp.append([j, 1])
            else:
                if j == temp[-1][0]:
                    if temp[-1][1] == k - 1:
                        temp.pop()
                    else:
                        temp[-1][1] += 1
                else:
                    temp.append([j, 1])

        return ''.join(item[0] * item[1] for item in temp)