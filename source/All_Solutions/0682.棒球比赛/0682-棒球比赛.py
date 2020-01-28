class Solution(object):
    def calPoints(self, ops):
        scores = []
        for i in ops:
            if i == '+':
                scores += [sum(scores[-2:])]
            elif i == 'D':
                scores += [scores[-1]*2]
            elif i == 'C':
                scores.pop()
            else:
                scores += [int(i)]
        return sum(scores)