# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

class Solution:
    def countSegments(self, s: str) -> int:
        sigment_count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                sigment_count += 1
        return sigment_count
