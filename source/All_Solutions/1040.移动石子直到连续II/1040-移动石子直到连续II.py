class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        
        n = len(stones)
        # 最大值
        mind, maxd = 10001, max(stones[n - 1] - stones[1], stones[n-2] - stones[0]) - n + 2
        
        # 最小值
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] < n:
                j += 1
            
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            
            mind = min(mind, cost)
        
        return [mind, maxd]
        