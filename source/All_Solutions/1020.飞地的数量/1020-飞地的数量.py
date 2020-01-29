class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        n=len(A)
        m=len(A[0])
        from collections import deque
        queue=deque()
        canvisit={(x,y) for x in range(n) for y in range(m) if A[x][y]==1}
        for i in [0,n-1]:
            for j in range(m):
                if A[i][j]==1:
                    queue.appendleft((i,j))
                    canvisit.remove((i,j))
        for i in range(1,n-1):
            for j in [0,m-1]:
                   if A[i][j]==1:
                    queue.appendleft((i,j))
                    canvisit.remove((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            (x,y)=queue.pop()
            A[x][y]=0
            for dx,dy in directions:
                if (x+dx,y+dy) in canvisit:              
                    queue.appendleft((x+dx,y+dy))
                    canvisit.remove((x+dx,y+dy))
        return sum(sum(x) for x in A)
