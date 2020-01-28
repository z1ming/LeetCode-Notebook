class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        n = len(A)
        # if B == 1:
        #     return [i + 1 for i in range(n)] if -1 not in A else []
        dpInd = [(1,)] * n
        dpCost = [sys.maxsize] * n
        dpCost[0] = A[0]
        for i in range(1, n):
            if A[i] == -1:
                continue
            curMin = (9999,)
            for j in range(max(i - B, 0), i):
                if dpCost[j] + A[i] < dpCost[i]:
                    dpCost[i] = dpCost[j] + A[i]
                    curMin = dpInd[j]
                elif dpCost[j] + A[i] == dpCost[i]:
                    if A[j] == 0:
                        curMin = dpInd[j]
                    else:
                        curMin = min(curMin, dpInd[j])
            dpInd[i] = tuple(list(curMin) + [i + 1]) 
            
        if dpCost[-1] > sys.maxsize // 2:
            return []
        return dpInd[-1]
        

