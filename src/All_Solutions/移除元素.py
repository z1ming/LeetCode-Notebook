# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
#
# 给定 nums = [3,2,2,3], val = 3,
#
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
#
# 你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        # 循环快指针，因为快指针将遍历整个nums
        for j in range(len(nums)):
            print(i)
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # 为什么不是返回i-1呢？
        # 因为i+=1是在完成赋值后，又加了1，因此i的值是result数组长度+1
        return i