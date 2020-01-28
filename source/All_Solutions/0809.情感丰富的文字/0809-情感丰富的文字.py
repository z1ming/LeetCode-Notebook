class Solution(object):
    def expressiveWords(self, S, words):
        def isStretchy(target, word):
            """
            Judge if word can be stretched to target
            """
            def charCnt(w):
                if len(w) == 1:
                    return [(w, 1)]
                res = []
                idx = 0
                while idx<len(w)-1:
                    currcnt = 1
                    while idx<len(w)-1 and w[idx+1]==w[idx]:
                        currcnt += 1
                        idx += 1
                    res.append((w[idx], currcnt))
                    idx += 1
                if w[-1] != w[-2]: res.append((w[-1],1))
                return res
            
            w_cnt = charCnt(word)
            t_cnt = charCnt(target)
            if len(w_cnt) != len(t_cnt):
                return False

            for idx in range(len(w_cnt)):
                if w_cnt[idx][0] != t_cnt[idx][0]:
                    return False
                if w_cnt[idx][1] != t_cnt[idx][1]:
                    if t_cnt[idx][1]<3 or w_cnt[idx][1] > t_cnt[idx][1]:
                        return False
            return True
        
        res = 0
        for word in words:
            if isStretchy(S, word):
                res += 1
        return res