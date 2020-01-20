# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 示例 1:
#
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 示例 2:
#
# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 示例 3:
#
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:return '0'
        res = []
        # 判断结果为正负
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator,denominator = abs(numerator),abs(denominator)
        # a,b为商的整数和余数
        a,b = divmod(numerator,denominator)
        res.append(str(a))
        if b != 0:
            res.append('.')
        dic = {b:len(res)}
        while b:
            b *= 10
            a,b = divmod(b,denominator)
            res.append(str(a))
            if b in dic:
                res.insert(dic[b],'(')
                res.append(")")
                break
            # 更新value
            dic[b] = len(res)
        return ''.join(res)