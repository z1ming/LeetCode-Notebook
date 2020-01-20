# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
#
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
# 示例:
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]
# 题目要求不适用额外空间，故可在原数组上修改，数组内的元素作为索引值，遍历一趟，取负后，没有被置为负值的索引即为所求。
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i)-1  # 保证索引值为正
            nums[index] = -abs(nums[index])
        return [i+1 for i,j in enumerate(nums) if j > 0]
