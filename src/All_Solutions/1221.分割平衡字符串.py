# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
#
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#
# 返回可以通过分割得到的平衡字符串的最大数量。
#
#  
#
# 示例 1：
#
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
# 方法一
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 用堆栈实现
        stack = []
        res = 0
        for i in range(len(s)):
            stack.append(s[i])
            if str(stack).count('L') == str(stack).count('R'):
                stack = []
                res += 1
        return res
# 方法二
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        tmp = 0
        for i in s:
            if i == 'L':
                tmp -= 1
            else:
                tmp += 1
            if tmp == 0:
                res += 1

        return res