# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
#
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
#
# 返回所有不常用单词的列表。
#
# 您可以按任何顺序返回列表。
#
#  
#
# 示例 1：
#
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet","sour"]
# 示例 2：
#
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]


from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = []
        # 返回只出现一次的单词即可！
        L = A.split(' ')+B.split(' ')
        dic = Counter(L)
        for key,value in dic.items():
            if value == 1:
                res.append(key)
        return res