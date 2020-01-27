class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        n_max = int(math.floor(math.log(num + 1) / math.log(2))) - 1
        for n in range(n_max, 1, -1):
            q = int(max(math.floor(math.pow(num, 1 / n)), 2))
            s = (pow(q, n + 1) - 1) / (q - 1)
            if abs(num - s) < 0.001:
                return str(q)
        return str(num - 1)