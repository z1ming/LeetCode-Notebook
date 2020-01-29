class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in set(arr):
            num = arr.count(i)
            if num/n > 0.25:
                return i