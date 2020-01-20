# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
#
# 示例 1:
#
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]]
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 示例 2:
#
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]]
# 解释: 可拼接成的回文串为 ["battab","tabbat"]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 本身就是回文单词
        palidStr = []
        # 翻转单词记录位置
        rev_words = {}
        # 结果
        res = []
        for idx,word in enumerate(words):
            rev_words[word[::-1]] = idx
            # 为了防止数组里有空字符串
            if word == word[::-1]:
                palidStr.append(idx)

        for idx,word in enumerate(words):
            if word:
                # 这里没有len(word) + 1
                for i in range(len(word)):
                    left,right = word[:i],word[i:]
                    # 是否存在在单词的左边加，使得成为回文串
                    if left == left[::-1] and right in rev_words and idx != rev_words[right]:
                        res.append([rev_words[right],idx])
                    # 同理
                    if right == right[::-1] and left in rev_words and idx != rev_words[left]:
                        res.append([idx,rev_words[left]])
            else: # 对于空字符串
                for loc in palidStr:
                    if loc != idx:
                        res.append([idx,loc])
        return res