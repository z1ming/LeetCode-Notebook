# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        wordList = set(wordList)  # 转换为hash实现O(1)的in判断
        if endWord not in wordList:
            return []
        # 分别为答案、用于剪枝的已访问哈希，前向分支和后向分支，当前的前向分支以及后向分支中的路径和的长度
        # 前向路径分支与后向路径分支的字典结构为{结束词：到达该结束词的路径列表}
        res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):  # 始终从路径分支较少的一端做BFS
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i]+a+word[i+1:]  # 对结束词尝试每一位的置换
                        if new in backward:  # 如果在后向分支列表里发现置换后的词，则路径会和
                            if paths[0][0] == beginWord:  # 前向分支是从beginWord开始的，添加路径会和的笛卡尔积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:  # 后向分支是从endWord开始的，添加路径会和的笛卡尔积
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in wordList and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break
            forward = tmp  # 更新前向分支
        return res
