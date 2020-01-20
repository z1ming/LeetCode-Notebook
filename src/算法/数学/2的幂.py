# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:
#
# 输入: 218
# 输出: false
# 方法一
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        num = 2
        while num <= n:
            if num == n:
                return True
            else:
                num *= 2
        return False
# 方法二
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n &(n-1) == 0