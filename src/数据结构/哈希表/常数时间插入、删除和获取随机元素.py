# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
# 示例 :
#
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
#
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
#
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
#
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
#
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
#
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
#
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
#
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();

# O(1)解法，使用哈希表和数组,哈希表存索引值，对数组操作
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.l1 = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        else:
            self.l1.append(val)
            self.dic[val] = len(self.l1)-1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        else:
            self.dic[self.l1[-1]] = self.dic[val]
            self.l1[self.dic.pop(val)] = self.l1[-1]
            self.l1.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.l1[random.randint(0,len(self.l1)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()