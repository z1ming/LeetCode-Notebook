# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
# 示例 1:
#
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 示例 2:
#
# 输入: "abcd"
# 输出: "dcbabcd"
# KMP算法
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_table(p):
            table = [0] * len(p)
            i = 1
            j = 0
            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = get_table(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s