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


