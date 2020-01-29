class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[1] - x[0]), reverse=True)
        total = 0
        left = 0
        right = 0
        for i in range(len(costs)):
            if left >= len(costs) // 2:
                total += costs[i][1]
            elif right >= len(costs) // 2:
                total += costs[i][0]
            elif costs[i][0] > costs[i][1]:
                total += costs[i][1]
                right += 1
            else:
                total += costs[i][0]
                left += 1
        return total