class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        from collections import defaultdict
        start = defaultdict(list)
        end = defaultdict(list)
        for i, phrase in enumerate(phrases):
            t = phrase.split(" ")
            start[t[0]].append((phrase, i))
            end[t[-1]].append((phrase, i))
        res = []
        for key, val in end.items():
            val.sort() #排序保证答案满足字典序排列
        for key, val in start.items():
            val.sort() #排序保证答案满足字典序排列
        for end_word, p1 in end.items():
            if end_word in start: #找到可以拼接的部分
                for s1, i1 in p1:
                    for s2, i2 in start[end_word]:
                        if i1 == i2: #满足题目给的 其他 这个条件
                            continue
                        if len(s2.split(" ")) == 1: #如果s2只有一个单词构成，那么直接返回s1
                            tmp = s1
                        else:
                            tmp = s1 + " " + " ".join(s2.split(" ")[1:])
                        if tmp not in res:
                            res.append(tmp)
        res.sort()
        return res

