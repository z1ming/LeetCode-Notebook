# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。
#
# 示例 1:
#
# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
# 示例 2:
#
# 输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:return 0

        right_idx = {}
        left,right = 0,0
        max_len = 1
        while right < len(s):
            right_idx[s[right]] = right
            right += 1
            if len(right_idx) == 3:
                del_idx = min(right_idx.values())
                del right_idx[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len,right - left)
        return max_len