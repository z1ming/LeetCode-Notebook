class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [int]) -> str:
        p = {i:i for i in range(len(s))}  
        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)   
        
        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)

        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)
            for i, c in zip(sorted(q), t):
                ans[i] = c
        return ''.join(ans)