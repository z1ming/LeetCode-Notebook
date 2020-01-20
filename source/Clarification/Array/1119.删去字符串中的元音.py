# 给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。
#
#  
#
# 示例 1：
#
# 输入："leetcodeisacommunityforcoders"
# 输出："ltcdscmmntyfrcdrs"


class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(filter(lambda c:c not in "aeiou",S))