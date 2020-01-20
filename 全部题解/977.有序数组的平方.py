# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#  
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            res.append(A[i]**2)
        res.sort()
        return res

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)