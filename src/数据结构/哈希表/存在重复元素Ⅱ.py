# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 示例 3:
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = set()
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            hash.add(nums[i])
            if len(hash) > k:
                hash.remove(nums[i-k])
        return False