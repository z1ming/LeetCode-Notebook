# 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
#
# 每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。
#
#
#
# 示例 1:
#
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
#
# 返回 true。5个矩形一起可以精确地覆盖一个矩形区域。

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 保存所有矩形的四个点
        lookup = set()
        # 最大矩形的 左下角 右上角
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")
        area = 0
        for x, y, s, t in rectangles:

            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, s)
            y2 = max(y2, t)

            area += (t - y) * (s - x)
            # 每个矩形的四个点
            for item in [(x, y), (x, t), (s, y), (s, t)]:
                if item not in lookup:
                    lookup.add(item)
                else:
                    lookup.remove(item)
        # 只剩下四个点并且是最大矩形的左下角和右上角
        if len(lookup) != 4 or \
                (x1, y1) not in lookup or (x1, y2) not in lookup or (x2, y1) not in lookup or (x2, y2) not in lookup:
            return False
        # 面积是否满足
        return (x2 - x1) * (y2 - y1) == area
