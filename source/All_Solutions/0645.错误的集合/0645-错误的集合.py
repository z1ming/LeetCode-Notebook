class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]