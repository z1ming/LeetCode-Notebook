# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
#
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 运用滑动窗口
        ans,archor = 0,0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                archor = i
            ans = max(ans,i-archor+1)  # 长度 = i - archor + 1
        return ans

# 时间复杂度：O(N)，N是nums的长度，我们通过nums执行一个循环
# 空间复杂度：O(1)，anchor和ans使用了常数级空间