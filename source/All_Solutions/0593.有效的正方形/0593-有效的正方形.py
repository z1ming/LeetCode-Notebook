class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dis = []
        p = [p1, p2, p3, p4]

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                tmp = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                dis.append(tmp)
        # 如果正方形，那么六个距离只能有两种情况，要么是4条边 要么是2条对角线  经过排序之后，那么前四个距离是边长  后两个距离是对角线
        # 如果只校验边长，那么可能是菱形   所以需要判断一下对角线长度是否相等
        dis.sort()
        return True if dis[0] > 0 and dis[0] == dis[3] and dis[4] == dis[5] else False
