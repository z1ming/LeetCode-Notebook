import heapq # Ä¬ÈÏ×îÐ¡¶Ñ
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pq = [] 
        vis = set()
        dir = [0, -1, 0, 1, 0]
        #init
        heapq.heappush(pq, (grid[0][0], 0, 0))
        vis.add((0,0))
        while len(pq)>0:
            cost, x, y = heapq.heappop(pq)
            if x==n-1 and y==n-1:
                return cost
            for i in range(4): 
                dx, dy = dir[i] + x, dir[i+1] + y
                if 0<=dx<n and 0<=dy<n:
                    if (dx,dy) in vis:
                        continue;
                    vis.add((dx,dy))   
                    heapq.heappush(pq,(max(grid[dx][dy],cost), dx, dy))
                       
        return -1    