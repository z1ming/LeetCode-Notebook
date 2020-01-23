# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
#
# 列表中的每个元素只可能是整数或整数嵌套列表
#
# 提示：你可以假定这些字符串都是格式良好的：
#
# 字符串非空
# 字符串不包含空格
# 字符串只包含数字0-9, [, - ,, ]
#  
#
# 示例 1：
#
# 给定 s = "324",
#
# 你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        # num为数字，sign为符号为，is_num为前一个是否为数字
        num, sign, is_num = 0, 1, False

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == '-':
                sign = -1
            elif c == '[':
                stack.append(NestedInteger())
            elif c == ',' or c == ']':
                # 把刚才遇到的数字append进去
                if is_num:
                    cur_list = stack.pop()
                    cur_list.add(NestedInteger(sign * num))
                    stack.append(cur_list)
                num, sign, is_num = 0, 1, False

                # 此时为嵌套列表
                if c == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)

        return stack[0]


