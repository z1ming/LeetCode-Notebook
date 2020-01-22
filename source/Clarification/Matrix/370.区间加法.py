# 假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。
#
# 其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
#
# 请你返回 k 次操作后的数组。
#
# 示例:
#
# 输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# 输出: [-2,0,3,5,3]
# 解释:
#
# 初始状态:
# [0,0,0,0,0]
#
# 进行了操作 [1,3,2] 后的状态:
# [0,2,2,2,0]
#
# 进行了操作 [2,4,3] 后的状态:
# [0,2,5,5,3]
#
# 进行了操作 [0,2,-2] 后的状态:
# [-2,0,3,5,3]

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        只在操作区间的边界上存储变化的值（而不是整个区间都进行更新）。
        最终只需要对整个数组求一遍和。
        """
        ans = [0] * (length + 1)
        for update in updates:
            ans[update[0]] += update[2]
            ans[update[1] + 1] -= update[2]
            print(ans)
        for k in range(1,length):
            ans[k] += ans[k - 1]
        return ans[:length]