class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(map(lambda i: bin(i)[2:] in S, range(1, N + 1)))