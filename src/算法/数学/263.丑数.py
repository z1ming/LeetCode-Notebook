# 编写一个程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例 1:
#
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3

class Solution:
    def isUgly(self, num: int) -> bool:
        if num ==0:
            return False
        if num == 1:
            return True
        while num %2==0 or num%3==0 or num%5==0:
            if num%2==0:
                num/=2
            if num%3==0:
                num/=3
            if num%5==0:
                num/=5
        return num ==1