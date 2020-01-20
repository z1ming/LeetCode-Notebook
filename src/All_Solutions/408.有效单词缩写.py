# 给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。
#
# 字符串 "word" 的所有有效缩写为：
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 注意单词 "word" 的所有有效缩写仅包含以上这些。任何其他的字符串都不是 "word" 的有效缩写。
#
# 注意:
# 假设字符串 s 仅包含小写字母且 abbr 只包含小写字母和数字。
#
# 示例 1:
#
# 给定 s = "internationalization", abbr = "i12iz4n":
#
# 函数返回 true.
#  
#
# 示例 2:
#
# 给定 s = "apple", abbr = "a2e":
#
# 函数返回 false.

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # 维护tmp（过程有些繁琐，能力有限）
        tmp = ''
        i = 0
        while i < len(abbr):
            if abbr[i] == '0':  # 处理测试案例里有0的情况
                tmp += abbr[i]
                i += 1
            elif abbr[i].isalpha():  # 是字母直接加到tmp中
                tmp += abbr[i]
                i += 1
            else:
                # 如果abbr = a13b，这里的数字表示13，而不是1和3，所以如果是数字还要考虑下一位是不是数字
                if i < len(abbr) - 1 and not abbr[i].isalpha() and not abbr[i + 1].isalpha():
                    tmp += '*' * int(abbr[i] + abbr[i + 1])
                    i += 2
                else:
                    tmp += '*' * int(abbr[i])
                    i += 1
        # 将tmp与word比较
        if len(tmp) != len(word):  # 长度不等直接返回False
            return False
        else:
            for j in range(len(tmp)):
                if tmp[j] != '*' and tmp[j] != word[j]:  # 只比较非*部分
                    return False

        return True