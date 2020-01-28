import copy
from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 1.只存在一棵树，只有一个入度为零的点
        # 2.不存在环
        def valid(graph,in_degree):
            node_num = len(in_degree)
            zeros = [v for v in in_degree if not in_degree[v]]
            stack = zeros
            visited = set()
            while stack:
                u = stack.pop(-1)
                visited.add(u)
                for v in graph[u]:
                    if in_degree[v] == 1:
                        stack.append(v)
                    in_degree[v] -= 1
                del graph[u]
            return len(visited) == len(in_degree)
        
        def delete_edge(graph,in_degree,u,v):
            graph[u].remove(v)
            in_degree[v] -= 1
        
        edge_index = dict(zip(map(tuple,edges),range(len(edges))))
        in_degree = defaultdict(int)
        graph = defaultdict(list) #u-->v
        graph_r = defaultdict(list) #u<--v
        zeros = set()
        ones = set()
        need_to_check = []
        for u,v in edges:
            graph[u].append(v)
            graph_r[v].append(u)
            in_degree[v] += 1
            if in_degree[v] == 1:
                ones.add(v)
                if v in zeros:zeros.remove(v)
            if in_degree[u] == 0:
                zeros.add(u)
            if in_degree[v] > 1:
                need_to_check = [[u,v] for u in graph_r[v]]
        if len(zeros) == 0: 
            need_to_check = [[graph_r[v][0],v] for v in ones]
        if len(zeros) == 2:
            pass
        #print(graph,in_degree,need_to_check)
        
        need_to_check.sort(key=lambda x:-edge_index[(x[0],x[1])])
        for u,v in need_to_check:
            in_degree1 = in_degree.copy()
            graph1 = copy.deepcopy(graph)
            delete_edge(graph1,in_degree1,u,v)
            #print(u,v,graph1,in_degree1)
            if valid(graph1,in_degree1):
                return [u,v]
        #print(graph,in_degree,need_to_check)

