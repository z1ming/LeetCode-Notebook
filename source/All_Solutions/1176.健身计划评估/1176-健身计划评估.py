class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        if k >= len(calories):
            s = sum(calories)
            if s<lower: return -1
            elif s>upper: return 1
            else: return 0
        p = k
        currS = sum(calories[0:p])
        res = 0
        while p < len(calories):
            if currS<lower: res-=1
            elif currS>upper: res+=1
            currS = currS-calories[p-k]+calories[p]
            p+=1
        if currS<lower: res-=1
        elif currS>upper: res+=1
        return res