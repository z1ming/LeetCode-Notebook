# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例:
#
# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。

import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
END_OF_WORD = "#"


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.result = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []

        # 构造字典树
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        # 开始dfs遍历
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)

        # 返回结果
        return self.result

    def dfs(self, board, i, j, cur_word, cur_dict):
        # 单词拼装
        cur_word += board[i][j]
        # 一层一层往下
        cur_dict = cur_dict[board[i][j]]

        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        # 将board[i][j]保存起来
        temp = board[i][j]
        # board[i][i]访问过，当前不能再用了，用@作为标记
        board[i][j] = "@"

        # 尝试四个方向
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != "@" and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        # backtrack
        board[i][j] = temp