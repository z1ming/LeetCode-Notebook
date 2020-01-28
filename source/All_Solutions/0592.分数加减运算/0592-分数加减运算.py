import re
class Solution:
    def fractionAddition(self, expr: str) -> str:
        pat = r"[+-]*\d+/\d+"
        its = re.findall(pat, expr)
        def h(it):
            up,down = it.split('/')
            up = int(up)
            down = int(down)
            return Fraction(up, down)
        its = map(h, its)
        ret = next(its)
        for it in its:
            ret  = ret + it
        return ret.to_str()
        
class Fraction:
    def __init__(self, up, down):
        self.up = up
        self.down = down
    def to_minimal(self):
        if self.up == 0:
            self.down = 1
            return
        def gcd(a, b):
            if a < b:
                return gcd(b,a)
            #print(a,b)
            if a%b == 0:
                return b
            else:
                return gcd(b,a%b)
        a, b = abs(self.up), abs(self.down)
        num = gcd(a,b)
        self.up //= num
        self.down //= num
    def __add__(self,other):
        if self.down == other.down:
            up = self.up + other.up
            down = self.down
            return Fraction(up, down)
        else:
            down = self.down*other.down
            up = self.up*other.down + self.down*other.up
            return Fraction(up, down)
    def __sub__(self,other):
        if self.down == other.down:
            up = self.up - other.up
            down = self.down
            return Fraction(up, down)
        else:
            down = self.down*other.down
            up = self.up*other.down - self.down*other.up
            return Fraction(up, down)
    def to_str(self):
        self.to_minimal()
        if self.up*self.down < 0:
            return f"-{abs(self.up)}/{abs(self.down)}"
        else:
            return f"{abs(self.up)}/{abs(self.down)}"