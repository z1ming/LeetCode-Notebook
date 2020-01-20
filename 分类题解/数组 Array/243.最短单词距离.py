# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
#
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]
#
# 输入: word1 = “coding”, word2 = “practice”
# 输出: 3

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # 将两个单词 索引分别保存在两个数组中
        l1,l2 = [],[]
        ans = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                l1.append(i)
            if words[i] == word2:
                l2.append(i)
        for i in l1:
            for j in l2:
                ans = min(ans,abs(i-j))
        return ans
# 时间复杂度:O(N)
# 空间复杂度：O(N)