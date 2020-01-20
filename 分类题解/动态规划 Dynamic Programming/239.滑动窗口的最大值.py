给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。
#
#  
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 1.遍历数组
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:return
        # 用数组window_list表示一个滑动窗口
        window_list = []
        for i in range(k):
            window_list.append(nums[i])
        res = []
        res.append(max(window_list))
        for j in range(len(nums) - k):
            window_list.pop(0)
            window_list.append(nums[k+j])
            res.append(max(window_list))
        return res
# time:O(KN)
# space:O(N)
# 2.dynamic programming
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(nums[j], right[j + 1])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output
# time:O(N)
# space:O(N)