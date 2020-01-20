# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。

class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
