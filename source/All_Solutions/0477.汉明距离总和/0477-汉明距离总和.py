class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

