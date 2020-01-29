class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        p = [i for i in range(N + 1)]
        connections.sort(key = lambda x: x[2])
        count = 0
        ans = 0
        def f(x):
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]
        for x, y, c in connections:
            px, py = f(x), f(y)
            if px != py:
                count += 1
                ans += c
                if count == N - 1:
                    return ans
                p[px] = py
        return -1