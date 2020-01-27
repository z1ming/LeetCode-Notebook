# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in hash:
                count += hash[sum - k]
            if sum in hash:
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count


