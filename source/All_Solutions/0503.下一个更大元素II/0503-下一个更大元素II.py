class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_length = len(nums)
        res_list = [-1 for _ in range(nums_length)]
        stack = list()
        
        double_nums = nums + nums
        for index, num in enumerate(double_nums):
            while stack and nums[stack[-1]] < num:
                res_list[stack[-1]] = num
                stack.pop()
            if index < nums_length:
                stack.append(index)
        return res_list