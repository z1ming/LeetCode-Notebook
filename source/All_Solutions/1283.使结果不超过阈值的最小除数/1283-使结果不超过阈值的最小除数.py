class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        简单二分
        时间复杂度: nums.length*log(max(nums)) = 17*5*10^4
        :param nums:
        :param threshold:
        :return:
        """
        L, R = 1, max(nums)
        while (L < R):
            mid = (L + R) >> 1
            # 小于等于阈值, 说明 答案不是在mid的左边就是mid
            if(sum(math.ceil(x/mid) for x in nums) <= threshold):
                R = mid
            # 大于阈值, 答案在mid右边
            else:
                L = mid + 1
        return R