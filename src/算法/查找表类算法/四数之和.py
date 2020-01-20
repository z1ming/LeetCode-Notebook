# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
class Solution:

    def twoSum(self, nums, target, l, r):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums[l : r+1])
        if n < 2:
            return list()

        start = nums[l - 1]
        dict1 = dict()
        ret = list()
        for i in range(l, r+1):
            other = target - nums[i]
            if other in dict1:
                ret.append([start, other, nums[i]])
            dict1[nums[i]] = i

        return ret

    # nums[l...r] 中返回 a+b+c=target
    def threeSum(self, nums, target, l, r):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums[l : r+1])
        if n < 3:
            return list()

        start = nums[l-1]
        ret = list()
        for i in range(l, r+1):
            if nums[i] > 0 and target <= 0:
                break
            if (i >= l+1 and nums[i] == nums[i-1]):
                continue
            ll = self.twoSum(nums, target-nums[i], i+1, r)
            if (ll == list()):
                continue
            for i in ll:
                i.insert(0, start)
                ret.append(i)
        return ret

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        ret = set()
        for i in range(n):
            ll = self.threeSum(nums, target-nums[i], i+1, n-1)
            if ll == list():
                continue
            for l in ll:
                ret.add(tuple(l))
        return list(ret)