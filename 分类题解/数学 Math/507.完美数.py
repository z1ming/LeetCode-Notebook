# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
#
# 给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
#
#  
#
# 示例：
#
# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def helper(n):
            return (2 ** (n - 1)) * (2 ** n - 1)

        list_su = [2, 3, 5, 7, 13, 17, 19, 31]
        for i in list_su:
            if helper(i) == num:
                return True
        return False

