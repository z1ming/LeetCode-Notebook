class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = [[0]]
        res = []
        target = len(graph)-1
        while paths:
            newpaths = []
            for i in paths:
                for j in graph[i[-1]]:
                    if j == target:
                        res.append(i+[target])
                    else:
                        newpaths.append(i+[j])
            paths = newpaths
        return res