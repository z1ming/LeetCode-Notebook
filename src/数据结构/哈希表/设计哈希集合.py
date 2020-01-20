# 不使用任何内建的哈希表库设计一个哈希集合
#
# 具体地说，你的设计应该包含以下的功能
#
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 用数组实现哈希集合

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number = 1000
        self.buckets = [[] for _ in range(self.number)]

    def add(self, key: int) -> None:
        y = key % self.number
        if key not in self.buckets[y]:
            self.buckets[y].append(key)

    def remove(self, key: int) -> None:
        y = key % self.number
        if key in self.buckets[y]:
            self.buckets[y].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        y = key % self.number
        if key in self.buckets[y]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)