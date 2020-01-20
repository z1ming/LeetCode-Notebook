# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。
#
# 示例:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.remove(self.queue[0])
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)