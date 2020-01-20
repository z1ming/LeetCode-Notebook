# 整数可以被看作是其因子的乘积。
#
# 例如：
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# 请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。
#
# 注意：
#
# 你可以假定 n 为永远为正数。
# 因子必须大于 1 并且小于 n。
# 示例 1：
#
# 输入: 1
# 输出: []
# 示例 2：
#
# 输入: 37
# 输出: []
# 示例 3：
#
# 输入: 12
# 输出:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(start,tmp,target):
            if target == 1:
                if len(tmp) > 1:
                    res.append(tmp)
            else:
                for j in range(start,target+1):
                    if target % j == 0:
                        helper(j, tmp + [j], target // j)
        helper(2, [], n)
        return res