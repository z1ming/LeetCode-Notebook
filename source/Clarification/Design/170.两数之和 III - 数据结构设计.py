# 设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。
#
# add 操作 -  对内部数据结构增加一个数。
# find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。
#
# 示例 1:
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 示例 2:
#
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data[number] = self.data.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.data.keys():
            if value - num in self.data:
                if value == 2 * num and self.data.get(num) >= 2:
                    return True
                elif value - num != num:
                    return True

        return False

    # Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)