# 根据逆波兰表示法，求表达式的值。
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 说明：
#
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：
#
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # eval函数用来执行一个字符串表达式，返回表达式的值
        # 用栈来处理
        stack = []
        for i in tokens:
            if i in {'+','-','*','/'}:
                a,b = stack.pop(),stack.pop()
                stack.append(str(int(eval(b + i + a))))
            else:
                stack.append(i)
        return stack[0]