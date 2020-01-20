# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯
#
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 关系式：f(i) = cost(i) + min(f(i+1),f(i+2))
        f1,f2 = 0,0
        for i in reversed(cost): # reverse从后向前遍历，因为先求f(i+1)和f(i+2)再求f(i)
            f1,f2 = i + min(f1,f2),f1
        return min(f1,f2)