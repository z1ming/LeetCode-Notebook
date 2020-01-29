class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        import math
        n = len(prices)
        prices = [float(i) for i in prices]
        floor = [math.floor(i) for i in prices]
        ceil = [math.ceil(i) for i in prices]
        res1, res2 = sum(floor), sum(ceil)
        if res1 > target or target > res2:
            return "-1"
        dif = [prices[i] - floor[i] for i in range(n)]
        dif.sort()
        res = 0
        target = n + res1 - target
        for i in range(target):
            res += dif[i]
        for i in range(target, n):
            res += 1 - dif[i]
        return "{:.3f}".format(res)
