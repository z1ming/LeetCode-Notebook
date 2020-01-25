# 在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？
#
# 示例 1：
#
# 输入: [[1,1],[-1,1]]
# 输出: true
# 示例 2：
#
# 输入: [[1,1],[-1,-1]]
# 输出: false


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:

        # Hash Points
        hash_tb = {}
        for point in points:
            x, y = point
            if not hash_tb.get(y):       hash_tb[y] = []
            if x not in hash_tb.get(y):  hash_tb[y].append(x)

        # 对称轴检查
        common_y = set()
        for key in hash_tb:
            values = hash_tb[key]
            values.sort()

            # 确定第一个对称点
            if len(values) % 2 == 1:
                mid = values[int((len(values) - 1) / 2)]
                values.remove(mid)
            else:
                mid = (values[0] + values[-1]) / 2
                values.remove(values[0])
                values.remove(values[-1])

            # 如果不同y值的点，存在两个对称轴，则 False
            common_y.add(mid)
            if len(common_y) > 1:
                return False

            # 如果同 y 轴的 点，对称轴不相同，则 False
            if len(values) > 1:
                if mid == 0:
                    if sum(values) != 0: return False
                elif sum(values) / mid % 2 != 0:
                    return False

        return True

