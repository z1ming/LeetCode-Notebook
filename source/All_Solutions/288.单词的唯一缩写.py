# 一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。
#
# 以下是一些单词缩写的范例：
#
# a) it                      --> it    (没有缩写)
#
#      1
#      ↓
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# 假设你有一个字典和一个单词，请你判断该单词的缩写在这本字典中是否唯一。若单词的缩写在字典中没有任何 其他 单词与其缩写相同，则被称为单词的唯一缩写。
#
# 示例：
#
# 给定 dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        from collections import defaultdict
        self.lookup = defaultdict(set)
        for dic in dictionary:
            if len(dic) <= 2:
                continue
            self.lookup[dic[0] + str(len(dic) - 2) + dic[-1] ].add(dic)

    def isUnique(self, word: str) -> bool:
        n = len(word)
        if n <= 2: return True
        k = word[0] + str(n - 2) + word[-1]
        if k in self.lookup and word in self.lookup[k] and len(self.lookup[k]) > 1:
            return False
        if k in self.lookup and word not in self.lookup[k] and len(self.lookup[k]) >= 1:
            return False
        return True