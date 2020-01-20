# 请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。
#
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]
#
# 输入: word1 = “coding”, word2 = “practice”
# 输出: 3
# 输入: word1 = "makes", word2 = "coding"
# 输出: 1

from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.locations = defaultdict(list)
        for idx,word in enumerate(words):
            self.locations[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        loc1,loc2 = self.locations[word1],self.locations[word2]
        l1,l2 = 0,0
        min_diff = float('inf')
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff,abs(loc1[l1]-loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff