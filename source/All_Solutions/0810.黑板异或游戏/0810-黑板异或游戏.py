class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return not __import__('functools').reduce(operator.xor, nums) or not len(nums) & 1