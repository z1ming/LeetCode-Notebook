class Solution:
    def criticalConnections(self, n, connections):
        ans, low, d = [], [-1] * n, [[] for _ in range(n)]
        for i, j in connections:
            d[i].append(j)
            d[j].append(i)
        def tarjan(c, v, p):
            dfn = low[v] = c
            for i in d[v]:
                if i != p:
                    if low[i] == -1: 
                        c += 1
                        tarjan(c, i, v)
                        if low[i] > dfn:
                            ans.append([v, i])
                    low[v] = min(low[v], low[i])
        tarjan(0, 0, -1)
        return ans