# 给定一个单词列表，只返回可以使用在键盘示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#  
#
# 注意：
#
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # 与每行求交集，如果与其中一行的交集等于本身，则该单词在同一行
        l1 = set('qwertyuiopQWERTYUIOP')
        l2 = set('asdfghjklASDFGHJKL')
        l3 = set('zxcvbnmZXCVBNM')
        ans = []
        for i in words:
            s = set(i)
            if s&l1 == s or s&l2 == s or s&l3 == s:
                ans.append(i)
        return ans