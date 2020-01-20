# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
#
# 示例1:
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#  
#
# 示例2:
#
# 输入: 3
# 输出: False

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i <= c ** 0.5:
            b = math.sqrt(c-i**2)
            if b == int(b):
                return True
            i += 1
        return False