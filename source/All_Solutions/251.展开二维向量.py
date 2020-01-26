# 请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。、
#
# 示例：
#
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
#
# iterator.next(); // 返回 1
# iterator.next(); // 返回 2
# iterator.next(); // 返回 3
# iterator.hasNext(); // 返回 true
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 4
# iterator.hasNext(); // 返回 false

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.list = []
        for item in v:
            for num in item:
                self.list.append(num)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.list[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.list)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()