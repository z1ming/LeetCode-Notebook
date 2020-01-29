class Solution:  
    def minimumMoves(self, grid: List[List[int]]) -> int:   
        n = len(grid)
        v = {(x, y) for x in range(n) for y in range(n) if grid[x][y] != 1}
        def move(x1,y1,x2,y2,i):
            if x1==x2:
                if i == 1:
                    if (x2,y2+1) in v:
                        return True,(x1,y1+1,x2,y2+1)
                elif i==2:
                    if (x1+1,y1) in v and (x2+1,y2) in v:
                        return True,(x1+1,y1,x2+1,y2)
                elif i==3:
                    if (x1+1,y1) in v and (x2+1,y2)  in v:
                        return True,(x1,y1,x1+1,y1)
            elif y1==y2:
                if i==1:
                    if (x1,y1+1) in v and (x2,y2+1) in v:
                        return True,(x1,y1+1,x2,y2+1)
                elif i==2:
                    if (x2+1, y2 ) in v:
                        return True,(x1+1,y1,x2+1, y2 )
                elif i==3:
                    if (x1,y1+1) in v and (x2,y2+1) in v:
                        return True,(x1,y1,x1,y1+1)
            return False,(0,0,0,0)
        def bfs(x1, y1, x2, y2):
            from collections import deque
            queue = deque()
            queue.appendleft((x1, y1, x2, y2))
            visit = set()
            visit.add((x1, y1, x2, y2))
            ans = -1
            while queue:
                ans+=1
                new_queue = deque()
                while queue:
                    x1, y1, x2, y2 = queue.pop()
                    if (x1, y1, x2, y2) == (n - 1, n - 2, n - 1, n - 1):
                        return ans
                    for i in range(1, 4):
                        flag, (nx1, ny1, nx2, ny2) = move(x1, y1, x2, y2, i)
                        if flag and (nx1, ny1, nx2, ny2) not in visit:
                            new_queue.appendleft((nx1, ny1, nx2, ny2))
                            visit.add((nx1, ny1, nx2, ny2))
                queue=new_queue
            return -1
        return bfs(0, 0, 0, 1)