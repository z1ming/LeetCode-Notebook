# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # 根据给定数字和宽度生成字符串,输入词汇、词总长度、词汇总数
        def wordTostr(words, total_len, count, maxWidth):
            if count > 1:
                div = (maxWidth - total_len) / (count - 1)
                mod = (maxWidth - total_len) % (count - 1)
                res = ""
                for i in range(count):
                    res += words[i]
                    if i < count - 1:
                        if i < mod:
                            res += " " * int(div + 1)
                        else:
                            res += " " * int(div)
            else:
                res = words[0] + " " * (maxWidth - total_len)
            return res

        # 贪心法找出每一行的词，生成字符串
        n = len(words)
        res = []
        start_ind = 0
        total_len = 0
        count = 0
        for i in range(n):
            w_l = len(words[i])
            if maxWidth - total_len - count - w_l >= 0:
                if i == n - 1:
                    s = ""
                    for w in words[start_ind:n - 1]:
                        s += w
                        s += " "
                    s += words[n - 1]
                    s += " " * (maxWidth - total_len - count - w_l)
                    res.append(s)
                else:
                    if count == 0:
                        start_ind = i
                    total_len += w_l
                    count += 1
            else:
                if i == n - 1:
                    res.append(wordTostr(words[start_ind:i], total_len, count, maxWidth))
                    res.append(words[n - 1] + " " * (maxWidth - w_l))
                else:
                    res.append(wordTostr(words[start_ind:i], total_len, count, maxWidth))
                    start_ind = i
                    count = 1
                    total_len = w_l
        return res

