class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue=set()
        visit=set()
        red=set()
        blue=set()
        for x,y in red_edges:
            red.add((x,y))
        for x,y in  blue_edges:
            blue.add((x,y))
        queue.add((0,0))
        queue.add((0,1))
        visit.add((0,0))
        visit.add((0,1))
        ans=[0]+[1000]*(n-1)
        t=0
        while queue:
            t+=1
            new=set()
            for node,color in queue:
                for i in range(1,n+1):
                    if color==1:
                        if (node,i) in red and  (i,0) not in visit:
                            new.add((i,0))
                            visit.add((i,0))
                            ans[i]=min(ans[i],t)
                    elif color==0:
                        if (node,i) in blue and  (i,1) not in visit:
                            new.add((i,1))
                            visit.add((i,1))
                            ans[i]=min(ans[i],t)
            queue=new
        for i,j in enumerate(ans):
            if j==1000:
                ans[i]=-1
        return ans