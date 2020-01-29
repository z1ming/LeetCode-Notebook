class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n, b = len(mat), len(mat[0]), int(''.join(map(str, itertools.chain(*mat))), 2)
        s, v, d, ans = {b}, {b}, set(), 0
        for t in range(m * n):
            k = 1 << t
            if t // n > 0:
                k += 1 << (t - n)
            if t // n < m - 1:
                k += 1 << (t + n)
            if t % n > 0:
                k += 1 << t - 1
            if t % n < n - 1:
                k += 1 << t + 1
            d.add(k)
        while s:
            t = set()
            for i in s:
                if not i:
                    return ans
                for j in d:
                    k = i ^ j
                    if k not in v:
                        t.add(k)
                        v.add(k)
            s = t
            ans += 1
        return -1