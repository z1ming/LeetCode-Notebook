class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums) - 1):
            bt = nums[i + 1] - nums[i] - 1
            if k > bt:
                k -= bt
            else:
                return nums[i] + k
        return nums[-1] + k