给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

class Solution(object):
    def countDigitOne(self, n):
        """
       用递归做的，可以改成记忆化搜索，加快时间
        """
        if n<=0: return 0
        if n<10: return 1
        last = int(str(n)[1:])
        power =  10**(len(str(n))-1)
        high = int(str(n)[0])
        if high == 1:
            return self.countDigitOne(last) + self.countDigitOne(power-1) + last+1
        else:
            return power+high*self.countDigitOne(power-1) + self.countDigitOne(last);
