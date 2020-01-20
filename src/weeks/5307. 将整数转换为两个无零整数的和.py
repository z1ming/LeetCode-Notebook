# 无零整数」是十进制表示中不含任何0的正整数。
#
# 给你一个整数n，请你返回一个由两个整数组成的列表[A, B]，满足：
#
# A和B都是无零整数
# A + B = n
# 题目数据保证至少有一个有效的解决方案。
#
# 如果存在多个有效解决方案，你可以返回其中任意一个。
#
#
#
# 示例1：
#
# 输入：n = 2
# 输出：[1, 1]
# 解释：A = 1, B = 1.A + B = n并且A和B的十进制表示形式都不包含任何0 。
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i,n-i]