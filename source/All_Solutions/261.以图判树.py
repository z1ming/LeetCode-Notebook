# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
#
# 示例 1：
#
# 输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true
# 示例 2:
#
# 输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false
# 注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for x, y in edges:
            tmp1 = find(x)
            tmp2 = find(y)
            if tmp1 == tmp2:
                return False
            union(x, y)
        return len(set(find(x) for x in range(n))) == 1

