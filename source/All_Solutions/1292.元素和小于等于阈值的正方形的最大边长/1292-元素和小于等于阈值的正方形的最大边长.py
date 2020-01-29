class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        tmp = [[0 for i in range(n+1)] for j in range(m+1)]
        def check(k):
            for i in range(k-1, m):
                for j in range(k-1, n):
                    if tmp[i][j] - tmp[i-k][j] - tmp[i][j-k] + tmp[i-k][j-k] <= threshold:
                        return True
            return False
        for i in range(m):
            for j in range(n):
                tmp[i][j] = tmp[i-1][j] + tmp[i][j-1] - tmp[i-1][j-1] + mat[i][j]
        l, r = 0, min(m, n)+1
        while l+1 < r:
            mid = (l+r) >> 1
            if check(mid):
                l = mid
            else:
                r = mid
        return l