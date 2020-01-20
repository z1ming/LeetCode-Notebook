# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 方法一：如果是快乐数最终会收敛到1，如果不是快乐数最终会出现4 16 37 58 89 145 42 20
class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
            if n == 1:
                return True
# 方法二：传统解法
class Solution:
    def isHappy(self, n: int) -> bool:
        already = set()
        while n != 1:
            sum = 0
            while n > 0:
                sum += (n % 10)**2
                n = n // 10
            if sum in already:
                return False
            else:
                already.add(sum)
            n = sum
        return True