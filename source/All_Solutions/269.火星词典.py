# 现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
#
# 假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。
#
# 您需要根据这个输入的列表，还原出此语言中已知的字母顺序。
#
# 示例
# 1：
#
# 输入:
# [
#     "wrt",
#     "wrf",
#     "er",
#     "ett",
#     "rftt"
# ]
#
# 输出: "wertf"
# 示例
# 2：
#
# 输入:
# [
#     "z",
#     "x"
# ]
#
# 输出: "zx"
# 示例
# 3：
#
# 输入:
# [
#     "z",
#     "x",
#     "z"
# ]
#
# 输出: "" 
#
# 解释: 此顺序是非法的，因此返回
# ""。

from operator import itemgetter
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        pre, suc = defaultdict(set), defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break

        chars = set("".join(words))
        free = chars - set(pre)
        order = ""

        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)

        return order * (set(order) == chars)