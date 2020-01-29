class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        max_weight = 5000
        if sum(arr)<=5000:
            return len(arr)
        arr.sort()
        count = 0
        weight = 0
        while weight <= 5000:
            weight+=arr[count]
            count+=1
        return count-1


