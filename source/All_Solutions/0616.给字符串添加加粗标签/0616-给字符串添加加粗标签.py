class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        lookup = set()
        for d in dict:
            left = 0
            while True:
                loc = s.find(d, left)
                if loc == -1:
                    break
                for i in range(loc, loc + len(d)):
                    lookup.add(i)
                left = loc + 1
        res = ""
        i = 0
        while i < len(s):
            left = i
            while i < len(s) and i in lookup:
                i += 1
            # print(left, i)
            if left == i:
                res += s[i]
                i += 1
            else:
                res += "<b>"
                for j in range(left, i):
                    res += s[j]
                res += "</b>"
        return res