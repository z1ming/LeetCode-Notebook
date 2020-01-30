class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 第一感觉是用滑动窗口
        # 维护一个滑动窗口
        # 考虑边界条件
        if not s: return 0

        hashmap = {s[0]:0}
        start = 0
        res = 1
        for i in range(1, len(s)):
            if s[i] not in s[start:i]:
                hashmap[s[i]] = i
                res = max(res,i - start + 1)
            else:
                start = hashmap[s[i]] + 1
                hashmap[s[i]] = i
        return res