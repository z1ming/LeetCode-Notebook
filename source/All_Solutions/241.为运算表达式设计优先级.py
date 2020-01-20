# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
#
# 示例 1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1. 分解，遇到运算符，计算左右两侧的结果集
                # 2. 解决，diffWaysToComputer递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                # 3. 合并，根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
