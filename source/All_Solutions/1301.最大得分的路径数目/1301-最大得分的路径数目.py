class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        d = [[[c, 0, 0] for c in reversed(s)] + [['X', 0, 0]] for s in reversed(board)]
        d[0][0][0] = d[-1][-2][0] = '0'
        d[0][0][2] = 1
        m, n = len(d), len(d[0]) - 1
        for i in range(m):
            for j in range(n):
                if d[i][j][0].isdigit():
                    dij, t = d[i][j], (d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
                    for tij in t:
                        if tij[0].isdigit():
                            dij[1] = max(dij[1], tij[1])
                    for tij in t:
                        if tij[0].isdigit():
                            dij[2] += dij[1] == tij[1] and tij[2]
                    dij[1] += int(dij[0])
        return d[-1][-2][2] and d[-1][-2][1] % 1000000007, d[-1][-2][2] % 1000000007