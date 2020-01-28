class Solution:
    def rotatedDigits(self, N: int) -> int:
        return len([i for i in range(1, N + 1) if not any([d for d in str(i) if int(d) in (3, 4, 7)]) and any([d for d in str(i) if int(d) in (2, 5, 6, 9)])])