class Solution(object):
    def longestWord(self, words):
        words.sort()
        words.sort(key=len, reverse=True)
        
        words_set = set(words)
        
        for w in words:
            flag = False
            for i in range(1, len(w)+1):
                if w[:i] not in words_set:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return w
        return ''