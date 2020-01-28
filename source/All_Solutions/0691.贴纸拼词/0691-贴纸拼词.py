class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        from collections import Counter
        import functools
        stickers = [Counter(s) for s in stickers]
        #lookup = {}
        @functools.lru_cache(None)
        def helper(target):
            if not target: return 0
            #if target in lookup: return lookup[target]
            res, cnt = float("inf"), Counter(target)
            for c in stickers:
                if c[target[-1]] == 0:continue
                nxt = helper("".join([s * t for (s, t) in (cnt - c).items()]))
                if nxt != -1: res = min(res, nxt + 1)
            #lookup[target] = -1 if res == float("inf") else res
            return -1 if res == float("inf") else res
        return helper(target)