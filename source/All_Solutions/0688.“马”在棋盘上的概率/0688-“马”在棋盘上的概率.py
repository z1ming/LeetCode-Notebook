class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = {}
        moves = ((-1, -2), (-2, -1),(-2, 1), (-1, 2),(1, -2), (2, -1),(2, 1), (1, 2))
        def dfs(K, r, c):
            if r < 0 or c < 0 or r >= N or c >= N:
                return 0
            if K == 0:
                return 1
            if (K, r, c) in memo:
                return memo[(K, r, c)]
            p = 0
            for move in moves:
                p += dfs(K-1, r+move[0], c+move[1])
            p /= 8.0
            memo[(K, r, c)] = p
            return p
        return dfs(K, r, c)