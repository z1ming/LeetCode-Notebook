class Solution:
    def kClosest(self, points, K) :
        a = lambda x :x[0]**2 + x[1]**2
        points.sort(key = a)
        return points[:K]