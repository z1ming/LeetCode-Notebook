# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 设置两个哈希表

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        l1 = str.split(' ')
        if len(l1) != len(pattern):
            return False
        dic1, dic2 = {}, {}
        for i in range(len(pattern)):
            if pattern[i] not in dic1:
                dic1[pattern[i]] = l1[i]
            else:
                if dic1[pattern[i]] != l1[i]:
                    return False
        for j in range(len(l1)):
            if l1[j] not in dic2:
                dic2[l1[j]] = pattern[j]
            else:
                if dic2[l1[j]] != pattern[j]:
                    return False

        return True