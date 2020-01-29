class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        sumdistance = sum(distance)
        res = 0
        if start > destination:
            start,destination = destination,start
        while start < destination:
            res += distance[start]
            start += 1
        return min(res,sumdistance-res)