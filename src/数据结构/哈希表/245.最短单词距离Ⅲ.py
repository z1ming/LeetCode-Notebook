# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
#
# word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。
#
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"].
#
# 输入: word1 = “makes”, word2 = “coding”
# 输出: 1
# 输入: word1 = "makes", word2 = "makes"
# 输出: 3
# 注意:
# 你可以假设 word1 和 word2 都在列表里。

from collections import defaultdict
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        locations = defaultdict(list)
        for idx,word in enumerate(words):
            locations[word].append(idx)
        loc1 = locations[word1]
        loc2 = locations[word2]
        i,j = 0,0
        min_dist = float('inf')
        if word1 == word2:
            for i in range(len(loc1)-1):
                for j in range(i+1,len(loc1)):
                    min_dist = min(min_dist,abs(loc1[i] - loc2[j]))
            return min_dist
        while i < len(loc1) and j < len(loc2):
            min_dist = min(min_dist,abs(loc1[i]-loc2[j]))
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        return min_dist