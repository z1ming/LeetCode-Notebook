# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
# 说明：
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
# 方法一：排序
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)+1):
            if nums[i] == nums[i-1]:
                return nums[i]
# 时间复杂度：O(nlog n)排序调用在python中花费O(nlgn)时间，因此它支配后续的线性扫描
# 空间复杂度：O(1)，在这里，我们对nums进行排序，因此内存大小是恒定的。如果我们不能修改输入数组，那么我们必须为nums
# 的副本分配线性空间，并对其进行排序。

# 方法二：集合
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)