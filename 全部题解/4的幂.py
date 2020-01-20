# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
# 示例 2:
#
# 输入: 5
# 输出: false
# 方法一
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 4 == 0:
            num //= 4
        return num == 1

# 方法二
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        # 首先判断是否为2的幂
        if num & (num-1) != 0:
            return False
        if num & 0x55555555 == num:
            return True
        return False