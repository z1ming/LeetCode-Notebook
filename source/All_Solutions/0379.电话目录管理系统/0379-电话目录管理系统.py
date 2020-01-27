class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.list = [0 for _ in range(maxNumbers)]

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        for i,x in enumerate(self.list):
            if x == 0:
                self.list[i] = 1
                return i
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.list[number] == 0

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.list[number] = 0


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)