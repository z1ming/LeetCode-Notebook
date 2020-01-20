# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#  
#
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
# 示例 2：
#
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：
#
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        letter = [c for c in S if c.isalpha()]
        for c in S:
            if c.isalpha():
                ans.append(letter.pop())
            else:
                ans.append(c)
        return ''.join(ans)
# 时间复杂度：O（N）
# 空间复杂度：O（N）