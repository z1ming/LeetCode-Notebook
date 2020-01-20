# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。

from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i]:以s[i]结尾的子字符串是否可以被空格拆分为一个或多个在字典中出现的单词
        """
        # 预处理，把wordDict 放进一个哈希表中
        word_dic = {word for word in wordDict}
        # 如果单词就在word_dic中，直接返回
        if s in word_dic:
            return [s]
        # 这种状态定义很常见
        dp = [False for _ in range(len(s))]
        dp[0] = s[0] in word_dic
        # 使用l，r分表表示左，右边界
        for r in range(1, len(s)):
            # 判断s[:r+1]是不是单词
            if s[:r + 1] in word_dic:
                dp[r] = True
                continue
            for l in range(r):
                # 判断是s[0:r+1]能不能分割成两个单词
                if dp[l] and s[l + 1:r + 1] in word_dic:
                    dp[r] = True
                    break
        res = []
        # 如果有解，才有必要回溯
        if dp[-1]:
            queue = deque()
            self.dfs(s, len(s) - 1, wordDict, res, queue, dp)
        return res

    def dfs(self, s, end, word_set, res, path, dp):
        # print('刚开始', s[:end + 1])
        # 如果不用拆分，整个单词就在 word_set 中就可以结算了
        if s[:end + 1] in word_set:
            path.appendleft(s[:end + 1])
            res.append(' '.join(path))
            path.popleft()

        for i in range(end):
            if dp[i]:
                suffix = s[i + 1:end + 1]
                if suffix in word_set:
                    path.appendleft(suffix)
                    self.dfs(s, i, word_set, res, path, dp)
                    path.popleft()

