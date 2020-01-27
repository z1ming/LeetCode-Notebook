from bisect import bisect_left
from random import randint
class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.weight = []
        s = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) #×¢Òâ¼Ó1
            s += area
            self.weight.append(s)
    def pick(self):
        """
        :rtype: List[int]
        """
        index = bisect_left(self.weight, randint(1, self.weight[-1]))
        rect = self.rects[index]
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]