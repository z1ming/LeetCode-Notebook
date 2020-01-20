# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找到字符串个数最少的字符
        t = min(set(s),key = s.count)
        # 最少字符的个数都大于等于k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a, k) for a in s.split(t))