# 给定一副牌，每张牌上都写着一个整数。
#
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
#
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。

from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        smaller = X = min(dic.values())
        # 寻找最大公约数
        for i in range(2,smaller+1):
            a = True
            for k,value in dic.items():
                if value % i != 0:
                    a = False
            if a:
                X = i
        for k,value in dic.items():
            if X < 2 or value % X != 0:
                return False
        return True

# 使用reduce迭代，gcd求解最大公约数
from functools import reduce
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2 # 对vals的前两个值使用gcd函数，再将结果与vals的第三个数使用gcd，这就是reduce的用法