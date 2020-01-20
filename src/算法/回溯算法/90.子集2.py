# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        def track_back(idx,tmp):
            res.append(tmp)
            for i in range(idx,n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                track_back(i+1,tmp + [nums[i]])
        res = []
        track_back(0,[])
        return res