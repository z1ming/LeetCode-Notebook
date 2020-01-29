"""
滑动窗口，窗口大小为minSize，因为要求出现的次数最大，如果maxSize的子串都出现了那么minSize必然也会出现,而且次数必然大于等于maxSize的次数
"""
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = []
        # 先把符合条件的全部搜集起来
        for i in range(0, len(s)-minSize+1):
            ts = s[i:i+minSize]
            if len(set(ts)) > maxLetters:
                continue
            else:
                res.append(ts)
        if not res:
            return 0
        # 返回出现次数最多的
        return sorted(Counter(res).items(), key=lambda x:x[1], reverse=True)[0][1]