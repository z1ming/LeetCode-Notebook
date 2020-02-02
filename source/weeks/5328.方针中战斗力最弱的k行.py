class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        for i in range(len(mat)):
            dic[i] = mat[i].count(1)
        sort_dic = sorted(dic.items(),key = lambda x:x[1])
        res = []
        i = 0
        for key,value in sort_dic:
            res.append(key)
            i += 1
            if i == k:
                break
        return res