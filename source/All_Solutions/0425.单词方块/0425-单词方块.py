class Node:
    def __init__(self):
        self.child = {}
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word, idx):
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node()
            cur = cur.child[ch]
        cur.idx = idx

class Solution:
    def dfs(self, cur, rows, index, candidate, res):
        if cur.idx != -1:
            candidate.append(self.words[cur.idx])
            if len(candidate) == self.d:
                res.append(candidate.copy())
            else:
                self.dfs(rows[len(candidate)], rows, len(candidate), candidate, res)
            candidate.pop()
        
        for ch in cur.child:
            parent = rows[index]
            if ch in rows[index].child:
                rows[index] = rows[index].child[ch]
                self.dfs(cur.child[ch], rows, index+1, candidate, res)
            rows[index] = parent
        
        return
        
        
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        T = Trie()
        self.words = words
        self.d = len(words[0])
        for i, word in enumerate(words):
            T.insert(word,i)
        
        rows = [T.root]*self.d
        candidate, res = [], []
        self.dfs(T.root, rows, 0, candidate, res)
        return res
        

