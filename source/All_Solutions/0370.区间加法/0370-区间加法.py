class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)
        for i, j, x in updates:
            res[i] += x
            res[j+1] -= x
        for i in range(1,length):
            res[i] += res[i-1]
        return res[:-1]