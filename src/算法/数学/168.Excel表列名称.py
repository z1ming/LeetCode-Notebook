# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# 示例 1:
#
# 输入: 1
# 输出: "A"
# 示例 2:
#
# 输入: 28
# 输出: "AB"
# 示例 3:
#
# 输入: 701
# 输出: "ZY"

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n,y = divmod(n, 26) # n,y分别位n%26的结果和余数
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res