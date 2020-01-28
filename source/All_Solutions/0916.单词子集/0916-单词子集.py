class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter
        from functools import reduce
        cb=reduce(Counter.__or__,map(Counter,B))
        def fun(a):
            ca=Counter(a)
            for k,v in cb.items():
                if v>ca[k]:
                    return False
            return True
        return filter(fun,A)