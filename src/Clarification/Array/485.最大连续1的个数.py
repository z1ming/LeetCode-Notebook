# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
### 算法思路：
遍历一遍数组，`left`指针指向子序列的第一个`1`的位置，当`nums[i]`为0时，`left`指针指向`i`的下一个位置，直到出现下一个连续子序列。
遍历的过程中，我们始终更新子序列的最大值。
### 参考代码
```
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i + 1
            res = max(res,i-left + 1)
        return res
```
### 复杂度分析
- 时间复杂度：*O(N)*，*N*是数组的长度，我们遍历了一遍数组
- 空间复杂度：*O(1)*，`res`，`left`占用了常数空间。
