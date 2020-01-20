# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
#
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
#
# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

# 输入：n = 4, connections = [[0,1],[0,2],[1,2]]
# 输出：1
# 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        fa = [i for i in range(n)]
        sz = [1 for i in range(n)]
        def getfa(x):
            if (fa[x] == x): return x
            fa[x] = getfa(fa[x])
            return fa[x]
        def merge(x, y):
            fx = getfa(x)
            fy = getfa(y)
            if fx == fy: return sz[fx], fx
            if sz[fx] > sz[fy]:
                fa[fy] = fx
                sz[fx] += sz[fy]
                return sz[fx], fx
            else:
                fa[fx] = fy
                sz[fy] += sz[fx]
                return sz[fy], fy
        redundancy = 0
        cur_max_net_size = 1
        cur_max_net_fa = 0
        for x, y in connections:
            fx = getfa(x)
            fy = getfa(y)
            if fx != fy:
                cur_size, cur_fa = merge(x, y)
                if cur_size > cur_max_net_size:
                    cur_max_net_size = cur_size
                    cur_max_net_fa = cur_fa
                if cur_size == n:
                    return 0
            else:
                redundancy += 1
        result = 0
        for i in range(n):
            fi = getfa(i)
            if fi != cur_max_net_fa:
                redundancy -= 1
                if redundancy < 0:
                    return -1
                result += 1
                cur_size, cur_fa = merge(i, cur_max_net_fa)
                if cur_size == n:
                    return result
