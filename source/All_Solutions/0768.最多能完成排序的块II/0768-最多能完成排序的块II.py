class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr = zip(arr, range(len(arr)))
        arr = sorted(arr)
        arrs = [0]*len(arr)
        for idx,i in enumerate(arr):
            arrs[i[1]] = idx
        m = -float('inf')
        res = 0
        for i in range(len(arrs)):
            m = max(m, arrs[i])
            if m == i:
                res += 1
        return res