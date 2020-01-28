from collections import defaultdict 
class AutocompleteSystem:
    class TrieNode():
        def __init__(self):
            self.next = defaultdict(AutocompleteSystem.TrieNode)
            self.isWord = False
            self.times = 0
            
    class Trie():
        def __init__(self):
            self.root = AutocompleteSystem.TrieNode()
        
        def insert(self,word, times=1):
            r = self.root
            for ch in word:
                r = r.next[ch]
            r.isWord = True
            r.times += times
        
        def search(self,word):
            r = self.root
            for ch in word:
                r = r.next[ch]
            ret,path = [],[word]
            self.traverse(r,path,ret)
            return ret
        
        def traverse(self,r,path,ret):
            if r.isWord:
                ret.append((-r.times, ''.join(path)))
            for ch in r.next:
                path.append(ch)
                self.traverse(r.next[ch],path,ret)
                path.pop()
            

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = AutocompleteSystem.Trie()
        self.cur = ''
        for word, cnt in zip(sentences,times):
            self.trie.insert(word,cnt)
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.cur)
            self.cur = ''
            return []
        else:
            self.cur += c
            ret = self.trie.search(self.cur)
            if not ret:
                return ret
            ret.sort()
            ret = [word for times, word in ret[:3]]
            return ret
