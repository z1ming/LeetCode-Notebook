# 请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
#
# 1 号机（发送方）有如下函数：
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# 2 号机（接收方）有如下函数：
#
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# 1 号机（发送方）执行：
#
# string encoded_string = encode(strs);
# 2 号机（接收方）执行：
#
# vector<string> strs2 = decode(encoded_string);
# 此时，2 号机（接收方）的 strs2 需要和 1 号机（发送方）的 strs 相同。
#
# 请你来实现这个 encode 和 decode 方法。

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # ['chen','du','xiu'] -> '4,chen,2,du,3,xiu'
        self.encode_res = ''# 加入数组长度
        for i in strs:
            self.encode_res += str(len(i)) + ',' # 加入字符串i的长度
            self.encode_res += i + ',' # 加入字符串i
        return self.encode_res[:-1] # 去掉最后一个逗号

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        # '4,chen,2,du,3,xiu' -> ['chen','du','xiu']
        self.decode_res = []
        i = 0
        while i < len(s):
            len_word = ''
            # '4 , chen , 2 , du , 3 , xiu'
            #  ^          ^        ^
            # len_word记录单词长度
            while s[i] != ',':
                len_word += s[i]
                i += 1
            # '4 , chen , 2 , du , 3 , xiu'
            #      ^    ^
            #    start end
            start = i + 1
            end = start + int(len_word)
            self.decode_res.append(s[start:end]) # 将单词添加到结果
            i = end + 1
        return self.decode_res