class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter
        count = 0
        words = Counter(words)
        for word,num in words.items():
            start = 0
            flag = False
            for alp in word:
                start = S.find(alp,start) + 1
                if start == 0:
                    flag = True
                    break
            if not flag:
                count += num
        return count