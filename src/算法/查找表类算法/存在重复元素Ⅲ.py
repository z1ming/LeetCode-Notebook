# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false

# 思路：使用查找表与滑动窗口

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        record = set()  # 定义窗口
        for i in range(n):
            if t == 0:  # 如果t=0，那么看看窗口内是否有重复元素，有就返回True
                if nums[i] in record:
                    return True
            else:
                for j in record:  # 遍历窗口元素，判断是否有绝对值小于t的情况，有就返回True
                    if abs(j - nums[i]) <= t:
                        return True
            record.add(nums[i])  # 向集合添加元素

            if len(record) > k:
                record.remove(nums[i - k])  # 维护长度为k的窗口
        return False
