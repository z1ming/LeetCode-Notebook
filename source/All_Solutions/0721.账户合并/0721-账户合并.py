class Solution:
    def accountsMerge(self, accounts):
        from collections import defaultdict

        f = {}

        def find(x):
            f.setdefault(x, x)
            while f[x] != x:
                #x = f[x]
                f[x] = f[f[x]]
                x = f[x]
            return x

        def union(x, y):
            f[find(x)] = find(y)

        lookup = {}
        n = len(accounts)
        for idx, account in enumerate(accounts):
            name = account[0]
            email = account[1:]
            for e in email:
                if e in lookup:
                    union(idx, lookup[e])
                else:
                    lookup[e] = idx
        # print(f)
        disjointSet = defaultdict(set)
        for i in range(n):
            tmp = find(i)
            for es in accounts[i][1:]:
                disjointSet[tmp].add(es)
        # print(disjointSet)
        res = []
        for key, val in disjointSet.items():
            res.append([accounts[key][0]] + list(sorted(val)))
        return res