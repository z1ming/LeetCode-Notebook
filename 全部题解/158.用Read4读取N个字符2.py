# read 方法：
#
# 通过使用 read4 方法，实现 read 方法。该方法可以从文件中读取 n 个字符并将其存储到缓存数组 buf 中。您 不能 直接操作文件。
#
# 返回值为实际读取的字符。
#
# read 的定义：
#
# 参数:   char[] buf, int n
# 返回值: int
#
# 注意: buf[] 是目标缓存区不是源缓存区，你需要将结果写入 buf[] 中。
#  
#
# 示例 1：
#
# File file("abc");
# Solution sol;
# // 假定 buf 已经被分配了内存，并且有足够的空间来存储文件中的所有字符。
# sol.read(buf, 1); // 当调用了您的 read 方法后，buf 需要包含 "a"。 一共读取 1 个字符，因此返回 1。
# sol.read(buf, 2); // 现在 buf 需要包含 "bc"。一共读取 2 个字符，因此返回 2。
# sol.read(buf, 1); // 由于已经到达了文件末尾，没有更多的字符可以读取，因此返回 0。

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.memory = [None] * 4
        self.idx = 0
        self.size = 0
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            if self.idx == self.size:
                self.size = read4(self.memory)
                self.idx = 0
            # 这里要返回i
            if self.size == 0: return i
            while i < n and self.idx < self.size:
                buf[i] = self.memory[self.idx]
                i += 1
                self.idx += 1

        return i