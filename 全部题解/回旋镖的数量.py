# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
#
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
#
# 示例:
#
# 输入:
# [[0,0],[1,0],[2,0]]
#
# 输出:
# 2
#
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
# 不知道为啥使用dic.get()会报错:(，所以用了if和else
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0
        res = 0
        for i in range(n):
            dic = dict()
            for j in range(n):
                if i != j:
                    key = self.f(points[i], points[j])
                    if key in dic:
                        dic[key] += 1
                    else:
                        dic[key] = 1
            for key, value in dic.items():
                res += value * (value - 1)
        return res

    def f(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2