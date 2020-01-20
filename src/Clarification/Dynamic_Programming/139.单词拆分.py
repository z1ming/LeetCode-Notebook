# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i]:以s[i]结尾的子字符串是否可以被空格拆分为一个或多个在字典中出现的单词
        """
        # 预处理，把wordDict 放进一个哈希表中
        word_dic = {word for word in wordDict}
        # 如果单词就在word_dic中，直接返回
        if s in word_dic:
            return True
        # 这种状态定义很常见
        dp = [False for _ in range(len(s))]
        dp[0] = s[0] in word_dic
        # 使用l，r分表表示左，右边界
        for r in range(1,len(s)):
            # 判断s[:r+1]是不是单词
            if s[:r+1] in word_dic:
                dp[r] = True
                continue
            for l in range(r):
                # 判断是s[0:r+1]能不能分割成两个单词
                if dp[l] and s[l + 1:r + 1] in word_dic:
                    dp[r] = True
                    break
        # print(dp)
        return dp[-1]