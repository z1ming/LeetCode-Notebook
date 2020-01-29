class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = list(itertools.accumulate([0] + arr, operator.xor))
        return [acc[a] ^ acc[b + 1] for a, b in queries]
