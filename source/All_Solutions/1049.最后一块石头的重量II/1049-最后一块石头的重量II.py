class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)/2.0
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                if x+y<= target:
                    addition.add(x+y)
            candidates = candidates.union(addition)
        return int(2*(target-max(candidates)))

