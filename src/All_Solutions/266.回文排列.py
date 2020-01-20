# 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
#
# 示例 1：
#
# 输入: "code"
# 输出: false
# 示例 2：
#
# 输入: "aab"
# 输出: true
# 示例 3：
#
# 输入: "carerac"
# 输出: true

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = 0
        count_dict = Counter(s)
        for i in count_dict.values():
            if i % 2 != 0:
                if len(s) % 2 == 0: # 如果字符串长度为偶数
                    return False
                else:
                    odd += 1  # 如果字符串长度为奇数，出现次数为奇数的字符种类最多为一种
        return True if len(s) % 2 == 0 else odd == 1