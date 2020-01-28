class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        path = [0]
        
        for i in range(N):
            if i % 2 == 0:
                path += board[N-1-i]
            else:
                path += board[N-1-i][::-1]
        
        from collections import deque
        q = deque()
        q.append((1,0))
        visited = [0]*(N*N+1)
        while len(q):
            cur,step = q.popleft()
            if cur+6 >= N*N:
                return step+1
            for nxt in range(cur+1,cur+7):
                if visited[nxt] == 0:
                    visited[nxt] = 1;
                    if path[nxt] == -1:
                        q.append((nxt,step+1))
                    else:
                        if path[nxt] == N*N:
                            return step+1
                        q.append((path[nxt],step+1))
        

        return -1