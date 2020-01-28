class Solution:
    def maxSumOfThreeSubarrays(self, nums: [int], k: int) -> [int]:
        n = len(nums)
        l = n - k + 1     
        sums = [0] * l      #储存每个长度为k的子数组的和
        s = sum(nums[:k])
        sums[0] = s
        for i in range(1,l):
            s = s + nums[i+k-1] - nums[i-1]
            sums[i] = s

        #中间子数组为i时左子数组的开始位置
        mid = {i:0 for i in range(k,l)}   #初始化为0
        for i in range(k, l):
            j = mid.get(i-1,0)
            if sums[i-k] > sums[j]: #保证中间数组开始为i时左子数组为最优
                j = i-k
            mid[i] = j  #中间子数组开始为i时左子数组开始为j

        #右子数组开始为i时中间子数组开始位置
        right = {i:k for i in range(2*k,l)} #初始化为k
        res = [0, k, 2 * k]
        for r in range(2 * k, l):
            m = right.get(r-1,k)
            #但右子数组开始下标为r时，此时左子数组与中间子数组的最大和
            if sums[r-k]+sums[mid[r-k]] > sums[m]+sums[mid[m]]:
                m = r - k
            right[r] = m    #右子数组开始下标为r时中间数组开始下标为m
            if sums[r]+sums[m]+sums[mid[m]] > sums[res[0]]+sums[res[1]]+sums[res[2]]:
                res = [mid[m], m, r]
        return res