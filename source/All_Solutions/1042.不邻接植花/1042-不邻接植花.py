class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # 思路: 对于当前的某一个花园，剔除掉与它邻接花园的花的种类，从剩下的种类中选一种即可。
        # 1. 构建邻接矩阵G; 2. 用res列表保存当前花园花的种类
        res = [0]*N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            # 对于当前花园, 排除掉邻接的花园的花种就ok了，然后pop出一种
            res[i] = ({1,2,3,4} - {res[j] for j in G[i]}).pop()
        return res