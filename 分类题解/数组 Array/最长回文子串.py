# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
            # 通过比较，长度长的为当前最大子串
            max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(max_sub) > max_len:
                res = max_sub
                max_len = len(max_sub)
        return res

    # 定义中心拓展法的函数
    def __center_spread(self, s, size, left, right):
        # 函数的输入left = right时，回文中心是一条线
        # 函数的输入right = left + 1时，回文中心是任意一个字符，回文串的长度是偶数
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1
# 时间复杂度：O（N**2），遍历了一次数组，没个元素进行一次中心拓展法，因此时间复杂度为O（N的平方）
# 空间复杂度：O（1），只用到常数个临时变量，于字符串长度无关。