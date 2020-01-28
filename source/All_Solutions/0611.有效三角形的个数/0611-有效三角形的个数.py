class Solution:
    def triangleNumber(self, nums: 'List[int]') -> 'int':
        nums.sort()
        res = 0
        # 从大到小遍历
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i -1
            while l < r:
                # 只要较小的两个值之和大于最大的值，则一定可组成三角形
                if nums[l] + nums[r] > nums[i]:
                    #i, r 和从l到r-1都可组成三角形，个数为 (r-1) - l + 1 = r - l
                    res += (r-1) - l + 1
                    r -= 1
                else: l += 1
        return res