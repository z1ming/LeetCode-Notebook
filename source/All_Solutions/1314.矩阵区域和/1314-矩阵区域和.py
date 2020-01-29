class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1)] + [[0, *itertools.accumulate(row)] for row in mat]
        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            s[i][j] += s[i - 1][j]
        def area(i, j):
            a = min(i + K, m - 1) + 1
            b = min(j + K, n - 1) + 1
            c = max(i - K, 0)
            d = max(j - K, 0)
            return s[a][b] + s[c][d] - s[a][d] - s[c][b]
        return [[area(i, j) for j in range(n)] for i in range(m)]