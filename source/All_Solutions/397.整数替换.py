# 给定一个正整数 n，你可以做如下操作：
#
# 1. 如果 n 是偶数，则用 n / 2替换 n。
# 2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
# n 变为 1 所需的最小替换次数是多少？
#
# 示例 1:
#
# 输入:
# 8
#
# 输出:
# 3
#
# 解释:
# 8 -> 4 -> 2 -> 1

class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or n & 2 == 0:
                n -= 1
            else:
                n += 1
            res += 1
        return res