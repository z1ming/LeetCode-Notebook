# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
#
# 输入: "A"
# 输出: 1
# 方法一：最笨的办法：
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        # if len(s) == 1:
        #     return dic[s]
        for i in range(-1,-len(s)-1,-1):
            res += dic[s[i]] * 26**(-i-1)
        return res
# 方法二：
class Solution:
    def titleToNumber(self, s: str) -> int:
        # 使用ASCII码ord()函数
        res = 0
        bit = 1
        for a in s[::-1]:
            res += (ord(a)-64)*bit
            bit *= 26
        return res