import heapq
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        n = len(blocks)
        if n == 1:
            return blocks[0]
        heapq.heapify(blocks)
        heap = blocks
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            heapq.heappush(heap, max(a+split, b+split))
        return heap[0]