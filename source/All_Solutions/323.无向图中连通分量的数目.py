# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。
#
# 示例 1:
#
# 输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# 输出: 2

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for x, y in edges:
            union(x, y)
        return len(set(find(x) for x in range(n)))