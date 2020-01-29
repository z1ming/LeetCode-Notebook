class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x]) 
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)
        for s in equations:
            if s[1]=="=":
                union(s[0],s[-1])
        for s in equations:
            if s[1]=="!":
                if find(s[0])==find(s[-1]):
                    return False
        return True