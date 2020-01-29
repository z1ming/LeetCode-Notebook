class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        l = toBeRemoved[0]
        r = toBeRemoved[1]
        
        for time in intervals:
            if time[0] > r or time[1] < l:
                res.append(time)
            if time[0] < l and l < time[1]:
                res.append([time[0],l])
            if time[0] < r and r < time[1]:
                res.append([r,time[1]])
        
        return res