# 给你一种规律 pattern 和一个字符串 str，请你判断 str 是否遵循其相同的规律。
#
# 这里我们指的是 完全遵循，例如 pattern 里的每个字母和字符串 str 中每个 非空 单词之间，存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abab", str = "redblueredblue"
# 输出: true
# 示例2:
#
# 输入: pattern = "aaaa", str = "asdasdasdasd"
# 输出: true
# 示例2:
#
# 输入: pattern = "aabb", str = "xyzabcxzyabc"
# 输出: false

class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        m,n = len(pattern),len(str)
        pattern_str = dict()
        visited_str = set()

        def helper(i,j):
            if i == m and j == n:
                return True
            if i == m or j == n or n - j < m - i:return False
            for index in range(j,n):
                sub_str = str[j:index + 1]
                if pattern[i] in pattern_str and pattern_str[pattern[i]] == sub_str:
                    if helper(i+1,index+1):
                        return True
                if not pattern[i] in pattern_str and not sub_str in visited_str:
                    pattern_str[pattern[i]] = sub_str
                    visited_str.add(sub_str)
                    if helper(i + 1, index + 1): return True
                    del pattern_str[pattern[i]]
                    visited_str.remove(sub_str)
            return False
        return helper(0,0)