# 给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。
#
# 注意：
#
# 满足编辑距离等于 1 有三种可能的情形：
#
# 往 s 中插入一个字符得到 t
# 从 s 中删除一个字符得到 t
# 在 s 中替换一个字符得到 t
# 示例 1：
#
# 输入: s = "ab", t = "acb"
# 输出: true
# 解释: 可以将 'c' 插入字符串 s 来得到 t。

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 假设t总比s长，如果不是，则交换
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return ns + 1 == nt