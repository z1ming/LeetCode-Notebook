# 给你一个回文字符串
# palindrome ，请你将其中
# 一个
# 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且
# 不是
# 回文串。
#
# 请你返回结果字符串。如果无法做到，则返回一个空串。
#
#
#
# 示例
# 1：
#
# 输入：palindrome = "abccba"
# 输出："aaccba"
# 示例
# 2：
#
# 输入：palindrome = "a"
# 输出：""
#
# 提示：
#
# 1 <= palindrome.length <= 1000
# palindrome
# 只包含小写英文字母。

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        if len(palindrome) % 2 == 0:
            for i in range(len(palindrome)):
                if palindrome[i] != 'a':
                    palindrome = palindrome[:i] + 'a' + palindrome[i + 1:]
                    return palindrome
                if i == len(palindrome) - 1 and palindrome[-1] == 'a':
                    palindrome = palindrome[:i] + 'b'
        else:
            for i in range(len(palindrome)):
                if palindrome[i] != 'a' and i != len(palindrome) // 2:
                    palindrome = palindrome[:i] + 'a' + palindrome[i + 1:]
                    return palindrome
                if i == len(palindrome):
                    continue
                if i == len(palindrome) - 1 and palindrome[-1] == 'a':
                    palindrome = palindrome[:i] + 'b'
        return palindrome