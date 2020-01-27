class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words,key=lambda i:len(i))
        s = set(words)
        ans = []
        while words:
            word = words.pop(-1)
            s.remove(word)
            L = len(word)
            stack = [0]
            while stack:
                p = stack.pop(0)
                flag = False
                for i in range(p+1,L+1):
                    if word[p:i] in s:
                        stack.append(i)
                        if i == L:
                            ans.append(word)
                            flag = True
                            break
                if flag:break
        return ans

