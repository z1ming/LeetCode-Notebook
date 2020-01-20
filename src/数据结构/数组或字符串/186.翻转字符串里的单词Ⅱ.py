# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 示例：
#
# 输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 注意：
#
# 单词的定义是不包含空格的一系列字符
# 输入字符串中不会包含前置或尾随的空格
# 单词与单词之间永远是以单个空格隔开的
# 进阶：使用 O(1) 额外空间复杂度的原地解法。

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        for j in range(len(s)):  # aT bT c
            if s[j] != " ":
                continue
            self.reverse(s, i, j)
            i = j + 1
        self.reverse(s, i, len(s))  # aT bT cT
        self.reverse(s, 0, len(s))  # c b a

    # 定义翻转函数
    def reverse(self, s, i, j):
        left = i
        right = j - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1