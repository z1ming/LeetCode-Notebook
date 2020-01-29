class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)