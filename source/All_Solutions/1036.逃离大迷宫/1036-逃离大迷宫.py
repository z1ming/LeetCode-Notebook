class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        from collections import deque
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        blocked_1=set()
        for x,y in blocked:
            blocked_1.add((x,y))
        def bfs(node,end):
            visited=set()
            queue=deque()
            queue.appendleft(tuple(node))
            visited.add(tuple(node))
            t=0
            while queue:                
                (x,y)=queue.pop()
                for (dx,dy) in directions:
                    if 0<=x+dx<=999999 and 0<=y+dy<=999999 and (x+dx,y+dy) not in visited and  (x+dx,y+dy) not in blocked_1:
                        if  [x+dx,y+dy]==end:
                            return 1
                        visited.add((x+dx,y+dy))
                        t+=1
                        queue.appendleft((x+dx,y+dy))
                if t>20000:
                    return 2
            return 0
        a= bfs(source,target)
        if a==0:
            return False
        elif a==1:
            return True
        elif a==2:
            b=bfs(target,source)
            if  b==2:
                return True
            return False