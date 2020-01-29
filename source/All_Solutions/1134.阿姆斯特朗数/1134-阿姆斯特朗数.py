class Solution:
    def isArmstrong(self, N: int) -> bool:
        return sum(map(lambda c: int(c) ** len(str(N)), str(N))) == N
