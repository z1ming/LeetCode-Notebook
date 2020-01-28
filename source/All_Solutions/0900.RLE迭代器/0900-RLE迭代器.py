class RLEIterator(object):
    def __init__(self, A):
        self.arr = []
        self.count = 0
        for i,n in enumerate(A):
            if i%2==1:continue
            self.arr.append([A[i+1], n])
            self.count+=n

    def next(self, n):
        arr = self.arr
        res = -1
        while n >0:
            if self.count <=0:return -1
            num,le = arr[0][0],arr[0][1]
            if n<=le:
                res = num
                arr[0][1] -= n
                self.count-= n
                if n==le:
                    arr.pop(0)
                n=0
            else:
                n-=le
                self.count -= le
                arr.pop(0)
        return res