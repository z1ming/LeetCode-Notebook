# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
# 输入: "aba"
# 输出: True
# 示例 2:
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        while l < r:
            # 考虑端点可删除情况
            if s[l] != s[r]:
                # 舍弃左字符
                a = s[l + 1:r + 1]
                # 舍弃右字符
                b = s[l:r]
                return a[::-1] == a or b[::-1] == b
            l += 1
            r -= 1
        return True
