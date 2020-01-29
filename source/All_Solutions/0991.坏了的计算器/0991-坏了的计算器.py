class Solution(object):
    # 思路，主要有几种情况，第一，Y小于X,那么这种情况下，只能进行疯狂递减操作，需要进行X-Y次操作
    # 第二，Y>X，那么首先观察，Y是否为奇数，如果是奇数，那么只能Y先+1，如果是偶数，那么就可以直接Y除2，查看是够相近
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # 递归思路
        # if X == Y:
        #     return 0
        # if X > Y:
        #     return X - Y
        # if Y % 2 == 0:
        #     return 1 + self.brokenCalc(X,int(Y/2))
        # else:
        #     return 1 + self.brokenCalc(X,Y+1)
        # 循环思路
        allnum = 0
        while X != Y:
            if X > Y:
                allnum += (X - Y)
                break
            if Y % 2 == 0:
                Y /= 2
                allnum+=1
            else:
                Y += 1
                allnum+=1
        return int(allnum)