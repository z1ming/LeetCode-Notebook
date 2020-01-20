# read 的定义：
#
# 参数类型:   char[] buf, int n
# 返回类型:   int
#
# 注意: buf[] 是目标缓存区不是源缓存区，你需要将结果写入 buf[] 中。
#  
#
# 示例 1：
#
# 输入： file = "abc", n = 4
# 输出： 3
# 解释： 当执行你的 rand 方法后，buf 需要包含 "abc"。 文件一共 3 个字符，因此返回 3。 注意 "abc" 是文件的内容，不是 buf 的内容，buf 是你需要写入结果的目标缓存区。

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
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        cur = 0
        while n>0:
            cache = [None]*4
            r = read4(cache)
            buf[cur:cur+r] = cache
            cur+=r
            if r<4:
                break
        return min(cur,n)
