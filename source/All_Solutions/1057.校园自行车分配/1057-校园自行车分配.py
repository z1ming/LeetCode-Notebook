class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)
        def dis(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        mem = list()
        for i in range(n):
            for j in range(m):
                mem.append((dis(workers[i], bikes[j]), i, j))
        mem.sort()
        res = [0]*n
        seenx, seeny = set(), set()
        for it in mem:
            im, jm = it[1], it[2]
            if im in seenx or jm in seeny:
                continue
            res[im] = jm
            seenx.add(im)
            seeny.add(jm)
        return res

