# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        避免一对多或者多对一的情况：
        1对多：a-b,a-c(哈希表中即一个key对应多个value)
        多对1：b-a,c-a(哈希表中即多个key具有一个value)
        """
        # 创建哈希表
        hash = {}
        for i, c in enumerate(s):
            if hash.get(c):
                if hash[c] != t[i]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                else:
                    hash[c] = t[i]

        return True