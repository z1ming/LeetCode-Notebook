# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first = bool(s) and p[0] in {s[0],'.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or \
            first and self.isMatch(s[1:],p)
        else:
            return first and self.isMatch(s[1:],p[1:])