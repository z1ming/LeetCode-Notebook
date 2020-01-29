class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node(False)
    
    def add(self, word):
        if not word:
            return
        
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c, Node(False))
        cur.val = True
    
    def check(self, word):
        # word is Iterable
        
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if cur.val:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])
        self.history = []
        

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        return self.trie.check(reversed(self.history))