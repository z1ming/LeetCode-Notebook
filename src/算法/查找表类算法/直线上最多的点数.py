# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
#
# 示例 1:
#
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4
from decimal import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return len(points)

        res = 0
        for i in range(n):
            dic = {'inf': 0}  # 先列出斜率正无穷的情况
            same = 0
            for j in range(n):
                if i != j:
                    if points[i][0] == points[j][0] and points[i][1] != points[j][1]:
                        dic['inf'] += 1
                    elif points[i][0] != points[j][0]:
                        k1 = self.slope(points[i], points[j])
                        if k1 in dic:
                            dic[k1] += 1
                        else:
                            dic[k1] = 1
                    else:
                        same += 1
            res = max(res, max(dic.values()) + same)
        return res + 1

    def slope(self, x1, x2):
        return Decimal(x2[1] - x1[1]) / Decimal(x2[0] - x1[0])