和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
# 方法一：暴力

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 方法一：枚举
        res = 0
        for i in nums:
            count = 0
            # 设置布尔变量判断是否是和谐子序列，避免都是相同的数的情况
            boolean = False
            for j in nums:
                if i == j:
                    count += 1
                elif j+1 == i:# 不能用（i-j）==1，这样意味着差别可以是2
                    count += 1
                    boolean = True
            if boolean:
                res = max(res,count)
        return res

#  方法二：哈希表
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        res = 0
        for key,value in dic.items():
            if dic.get(key+1,0) != 0:
                res = max(res,dic.get(key+1)+dic.get(key))
        return res
