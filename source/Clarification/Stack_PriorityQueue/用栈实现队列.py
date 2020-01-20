# 使用栈实现队列的下列操作：
#
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 我们用一个数组来表示栈，栈的名称叫stack
        # 这种题目和一般题目的区别就是，如果在函数里定义了新的结构，
        # 记得在前面加上self，比如stack就成了self.stack
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 向栈压入一个数其实就相当于向数组中加入一个数，
        # 所以就写成了stack.append(x),但是这样不对，应该是
        # self.stack.append(x)
        return self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 同理，pop为出栈，但是按照后入先出的顺序，我们要变成队列的先入先出，
        # 则需要将栈底元素出栈，即stack数组的第一个数，故为self.stack.pop(0),
        # 0为第一个元素的索引
        return self.stack.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        # 队首元素即数组的第一个元素，索引为0，故写成self.stack[0]
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 如果队为空，即stack=[],需要返回True，否则返回False，所以用if语句即可。
        if self.stack == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()