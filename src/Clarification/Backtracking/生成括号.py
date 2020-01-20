# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s='',left=0,right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s+'(',left+1,right)
            if right < left:
                backtrack(s+')',left,right+1)
        backtrack()
        return ans