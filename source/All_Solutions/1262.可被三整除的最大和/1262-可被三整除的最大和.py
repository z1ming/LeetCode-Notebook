class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        k = s % 3
        if not k:  
            return s
        a, b, hq = s, [-s, -s], heapq.heappushpop
        c, d = (1, 2) if k == 1 else (2, 1)
        for i in nums:
            if i % 3 == c:
                a = min(a, i)
            elif i % 3 == d:
                hq(b, -i)
        return s - min(a, -sum(b))