from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        mem = defaultdict(int)
        for n1 in A:
            for n2 in A:
                mem[n1 & n2] += 1
        ans = 0
        for num in A:
            for key, val in mem.items():
                if num & key == 0:
                    ans += val
        return ans
