给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        left,right = 0,0
        max_len = 1
        idx_right = {}  # sliding window
        while right < len(s):
            idx_right[s[right]] = right
            right += 1
            if len(idx_right) == k + 1:
                del_idx = min(idx_right.values())
                del idx_right[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len,right - left)
        return max_len