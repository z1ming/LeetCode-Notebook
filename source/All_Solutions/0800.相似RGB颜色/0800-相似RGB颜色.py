class Solution:
    
    def similarRGB(self, color: str) -> str:
        def similar(s):
            lookup = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            num = 0
            for c in s:
                num = num*16 + lookup.index(c)
            first = lookup.index(s[0])
            res = ''
            minNum = float('inf')
            for i in [-1,0,1]:
                if (first == 0 and i==-1) or (first == 15 and i == 1): continue
                cur = (first+i)*16 + (first+i)
                if abs(cur - num)<minNum:
                    res = lookup[first+i]
                    minNum = abs(cur - num)
            return res+res
        return "#" + similar(color[1:3])+ similar(color[3:5])+ similar(color[5:])