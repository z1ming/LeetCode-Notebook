class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        nodes_status = [0] * len(graph)
        safe_nodes = []
        for i in range(len(graph)):
            if nodes_status[i] == 0:
                self.dfs(graph, i, nodes_status, safe_nodes)
        return sorted(safe_nodes)

    def dfs(self, graph, i, nodes_status, safe_nodes):
        nodes_status[i] = 1
        flag = False
        for sub_node in graph[i]:
            if nodes_status[sub_node] == 0:
                if self.dfs(graph, sub_node, nodes_status, safe_nodes):
                    flag = True
            elif nodes_status[sub_node] == 1:
                flag = True
        if not flag:
            safe_nodes.append(i)
            nodes_status[i] = 2
        return flag