# UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：
#
# 对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。
# 对于 n 字节的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。
# 这是 UTF-8 编码的工作方式：
#
#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# 给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。
#
# 注意:
# 输入是整数数组。只有每个整数的最低 8 个有效位用来存储数据。这意味着每个整数只表示 1 字节的数据。
#
# 示例 1:
#
# data = [197, 130, 1], 表示 8 位的序列: 11000101 10000010 00000001.
#
# 返回 true 。
# 这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
# 示例 2:
#
# data = [235, 140, 4], 表示 8 位的序列: 11101011 10001100 00000100.
#
# 返回 false 。
# 前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
# 下一个字节是开头为 10 的延续字节，这是正确的。
# 但第二个延续字节不以 10 开头，所以是不符合规则的。

class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # For each integer in the data array.
        for num in data:

            # Get the binary representation. We only need the least significant 8 bits
            # for any given number.
            bin_rep = format(num, '#010b')[-8:]

            # If this is the case then we are to start processing a new UTF-8 character.
            if n_bytes == 0:

                # Get the number of 1s in the beginning of the string.
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Else, we are processing integers which represent bytes which are a part of
                # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # We reduce the number of bytes to process by 1 after each integer.
            n_bytes -= 1

        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0

