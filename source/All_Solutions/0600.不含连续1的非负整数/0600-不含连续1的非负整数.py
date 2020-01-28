class Solution:

    def findIntegers(self, num: int) -> int:
        retMap = {
            1: 2,
            2: 1,
            3: 2
        }
        bstr = bin(num)[2:]
        k = len(bstr)
        for i in range(4, k + 2):
            retMap[i] = retMap[i - 1] + retMap[i - 2]

        def fun1(k: int) -> int:
            return retMap[k] + retMap[k + 1]

        def func2(n):
            if n <= 2:
                return n + 1
            b = bin(n)[2:]
            k2 = len(b)
            if b[1] == '1':
                return fun1(k2)
            else:
                a = fun1(k2 - 1)
                c = func2(int(b[2:], 2))
                return a + c

        return func2(num)