class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        思路:染色法,
        1.从某一个固定节点出发,将其相邻的点都染成相反的颜色,然后从相邻的点继续出发,重复1
        若出现两个相邻点的颜色相同或者,则不是二分图
        '''
        color = [0] * len(graph)
        def color_node(node):
            nonlocal color
            queue = [node]
            color[node] = 1
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 1 if color[node] == -1 else -1
                        queue.append(neighbor)
                    if color[neighbor] + color[node] != 0:
                        return False
            return True
        for node in range(len(graph)):
            if color[node] == 0:
                color_res = color_node(node)
                if not color_res:
                    return False
        return True