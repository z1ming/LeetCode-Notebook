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
                elif  value - num != num:
                    return True

        return False     


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)