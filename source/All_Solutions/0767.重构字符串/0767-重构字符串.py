class Solution:
    def reorganizeString(self, S: str) -> str:
        a = list(S)
        b = dict(collections.Counter(a))
        c = sorted(b,key = lambda k: 0-b[k])
        d = []
        for i in c:
            d += [i]*b[i]
        ans = [0]*len(a)
        ans[::2] = d[:len(ans[::2])]
        ans[1::2] = d[len(ans[::2])::]
        if ans[0] == ans[1]:
            return ""
        else:
            ans_str = ''
            for i in ans:
                ans_str +=i
            return ans_str