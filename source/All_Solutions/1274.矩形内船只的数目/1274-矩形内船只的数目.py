# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # print(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        else:
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1

        mx = (topRight.x - bottomLeft.x) // 2 + bottomLeft.x
        my = (topRight.y - bottomLeft.y) // 2 + bottomLeft.y
        r1a = bottomLeft
        r1b = Point(mx, my)
        count = self.countShips(sea, r1b, r1a)
        if topRight.x != bottomLeft.x:
            r4a = Point(mx + 1, bottomLeft.y)
            r4b = Point(topRight.x, my)
            count += self.countShips(sea, r4b, r4a)
        if topRight.y != bottomLeft.y:
            r2a = Point(bottomLeft.x, my + 1)
            r2b = Point(mx, topRight.y)
            count += self.countShips(sea, r2b, r2a) 
        if topRight.x != bottomLeft.x and topRight.y != bottomLeft.y:
            r3a = Point(mx + 1, my + 1)
            r3b = topRight
            count += self.countShips(sea, r3b, r3a)
        return count