# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
#
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
#
# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 示例 3:
#
# 输入: ")("
# 输出: [""]

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(string):
            l_minus_r = 0
            for c in string:
                if c == '(':
                    l_minus_r += 1
                elif c == ')':
                    l_minus_r -= 1
                    if l_minus_r < 0:
                        return False
            return l_minus_r == 0

        level = {s}
        while True:
            valid = list(filter(isvalid,level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}