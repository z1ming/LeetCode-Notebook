# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
#
# 注意:
#  nums 数组的总和是一定在 32 位有符号整数范围之内的。
#
# 示例 1:
#
# 输入: nums = [1, -1, 5, -2, 3], k = 3
# 输出: 4
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
# 示例 2:
#
# 输入: nums = [-2, -1, 2, 1], k = 1
# 输出: 2
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。
# 进阶:
# 你能使时间复杂度在 O(n) 内完成此题吗?

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 前缀和＋哈希表，很神奇，用sum[i]表示（a[1]+a[2]+……+a[i])，
        # 其中sum[0]=0，则（a[i]+a[i+1]+……+a[j]）即等于sum[j]-sum[i-1]。
        # 使用哈希表存放{前缀和：当前索引}
        lookup = {0:-1} # 初始化边界条件
        cur = 0
        res = 0
        for idx,val in enumerate(nums):
            cur += val
            if cur - k in lookup:
                res = max(res,idx - lookup[cur - k])
                # 记录前面和的最小位置，如果和存在则不改变
            if cur not in lookup:
                lookup[cur] = idx
        return res