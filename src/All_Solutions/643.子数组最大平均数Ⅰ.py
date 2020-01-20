# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#  
#
# 注意:
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        res = sum(nums[0:k])
        temp = res
        for i in range(1,len(nums)-k+1):
            temp = temp - nums[i-1] + nums[i+k-1]
            if temp > res:
                res = temp
        return res / k