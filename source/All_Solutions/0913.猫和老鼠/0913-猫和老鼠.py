class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        state = [[[0]*3 for i in range(N)]for j in range(N)]
        q = collections.deque()
        for i in range(1,N):
            for j in range(1,3):
                state[0][i][j] = 1
                q.append((0,i,j))
                state[i][i][j] = 2
                q.append((i,i,j))
        while q:
            curstate = q.popleft()
            m,c,turn = curstate
            for prestate in self.findAllprestate(graph,curstate):
                pm,pc,pturn = prestate
                if state[pm][pc][pturn]!=0:
                    continue
                if state[m][c][turn]==3-turn:
                    state[pm][pc][pturn] = pturn
                    q.append(prestate)
                elif self.AllneighboursWin(graph,prestate,state):
                    state[pm][pc][pturn] = turn
                    q.append(prestate)  
        return state[1][2][1]
    def findAllprestate(self,graph,curstate):
        ret = []
        m,c,turn = curstate
        if turn==1:
            for pc in graph[c]:
                if pc!=0:
                    ret.append((m,pc,3-turn))
        else:
            for pm in graph[m]:
                ret.append((pm,c,3-turn))
        return ret
    def AllneighboursWin(self,graph, curstate,state):
        m,c,turn = curstate
        if turn==1:
            for nextm in graph[m]:
                if state[nextm][c][2]!=2:
                    return False
        elif turn ==2:
            for nextc in graph[c]:
                if nextc==0:continue
                if state[m][nextc][1]!=1:
                    return False
        return True