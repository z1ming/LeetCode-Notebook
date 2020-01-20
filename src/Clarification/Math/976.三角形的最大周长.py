# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
#
# 如果不能形成任何面积不为零的三角形，返回 0。
#
#  
#
# 示例 1：
#
# 输入：[2,1,2]
# 输出：5
# 示例 2：
#
# 输入：[1,2,1]
# 输出：0

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-3,-1,-1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0处。