# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
#
#  
#
# 示例 1：
#
# 输入：nums = [12,345,2,6,7896]
# 输出：2
# 解释：
# 12 是 2 位数字（位数为偶数） 
# 345 是 3 位数字（位数为奇数）  
# 2 是 1 位数字（位数为奇数） 
# 6 是 1 位数字 位数为奇数） 
# 7896 是 4 位数字（位数为偶数）  
# 因此只有 12 和 7896 是位数为偶数的数字
# 方法一
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
        return res
# 方法二
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            n = 0
            while i > 0:
                i //= 10
                n += 1
            if n % 2 == 0:
                res += 1
        return res