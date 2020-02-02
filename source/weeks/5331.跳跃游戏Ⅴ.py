class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        D = {}
        l = len(arr)
        def P(n):
            if n in D:
                return D[n]
            t = 1
            for i in range(1,d+1):
                if n + i >= l or arr[n] <= arr[n + i]:
                    break
                t = max(t, 1+ P(n + i))
            for i in range(1, d + 1):
                if n - i < 0 or arr[n] <= arr[n - i]:
                    break
                t = max(t, 1 + P(n - i))
            D[n] = t
            return t
        return max(P(i) for i in range(l))