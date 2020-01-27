class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        zcrossproduct = None
        for i in range(-2, n-2):
            x = [ points[i][0], points[i+1][0], points[i+2][0] ]
            y = [ points[i][1], points[i+1][1], points[i+2][1] ]
            dx1 = x[1] - x[0]
            dy1 = y[1] - y[0]
            dx2 = x[2] - x[1]
            dy2 = y[2] - y[1]
            if not zcrossproduct:
                zcrossproduct = dx1 * dy2 - dy1 * dx2
            elif ( dx1 * dy2 - dy1 * dx2 ) * zcrossproduct < 0:
                return False
        return True

