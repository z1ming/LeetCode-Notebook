class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.insert(0, x)

    def pop(self) -> int:
        return self.data.pop(0)

    def top(self) -> int:
        return self.data[0]

    def peekMax(self) -> int:
        return max(self.data)

    def popMax(self) -> int:
        num = max(self.data)
        self.data.remove(num)
        return num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()