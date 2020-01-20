# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。
#
#  
#
# 示例：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
# 方法一：哈希表
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s) - 9):
            if s[i:i+10] in d:
                d[s[i:i+10]] = True
            else:
                d[s[i:i+10]] = False
        return filter(lambda i:d[i],d)