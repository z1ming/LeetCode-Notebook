# 将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
#
# 示例 1:
#
# 输入: 123
# 输出: "One Hundred Twenty Three"
# 示例 2:
#
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
# 示例 3:
#
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 示例 4:
#
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve\
         Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                return to19[num - 1:num]
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + helper(num % 100)
            for p,w in enumerate(['Thousand','Million','Billion'],1): # 指定索引从1开始
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return ' '.join(helper(num)) or 'Zero'