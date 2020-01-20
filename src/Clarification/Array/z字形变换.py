# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['' for _ in range(len(s))]
        i,flag = 0,-1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(res)