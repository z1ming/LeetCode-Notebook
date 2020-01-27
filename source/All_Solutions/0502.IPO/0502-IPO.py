class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        dp = [i for i in zip(Capital, Profits)]
        dp.sort()
        heap = []
        n, i = len(dp), 0
        while k:
            while i < n and dp[i][0] <= W:
                heapq.heappush(heap, -dp[i][1])
                i += 1
            if not heap:
                return W
            W += -heapq.heappop(heap)
            k -= 1
        return W