# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
#
# 示例
# 1：
#
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例
# 采用倒序遍历，双指针法
# 利用while循环
class Solution:
    def reverseWords(self, s: str) -> str:
        # 去除首位空格
        s = s.strip()
        res = ''
        i,j  = len(s) - 1,len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i+1:j] + ' '
                while s[i] == ' ':i-=1
                j = i + 1
            i -= 1
        return res + s[:j]
# 时间复杂度：O（N）遍历了一遍字符串
# 空间复杂度：O（N）使用额外的res