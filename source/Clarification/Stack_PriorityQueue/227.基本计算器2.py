# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
#
# 输入: "3+2*2"
# 输出: 7
# 示例 2:
#
# 输入: " 3/2 "
# 输出: 1
# 示例 3:
#
# 输入: " 3+5 / 2 "
# 输出: 5
# 说明：
#
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 0
                while i < len(s) and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                stack.append(tmp)
                # 如果栈中有乘除，先算出来
                while len(stack) > 1 and stack[-2] in {"*", "/"}:
                    stack.pop()
                    opt = stack.pop()
                    if opt == "*":
                        stack.append(stack.pop() * tmp)
                    else:
                        stack.append(stack.pop() // tmp)
            elif s[i] in { "*", "/", "+", "-"}:
                stack.append(s[i])
                i += 1
            else:
                 i += 1
        res = 0
        sign = 1
        for t in stack:
            if t == "+":
                sign = 1
            elif t == "-":
                sign = -1
            else:
                res += sign * t
        return res