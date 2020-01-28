class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, max_val = 0, arr[0]
        for i, num in enumerate(arr):
            if num > max_val:
                max_val = num
            if max_val == i:
                res += 1
        return res