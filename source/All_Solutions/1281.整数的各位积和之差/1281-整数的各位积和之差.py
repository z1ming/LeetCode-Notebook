class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        num = []
        for i in n:
            i = int(i)
            num.append(i)
        ji = 1
        he = 0
        for i in num:
            ji *= i
            he += i
        cha = ji-he
        return cha