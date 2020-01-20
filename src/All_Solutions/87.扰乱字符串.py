# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
#
# 下图是字符串 s1 = "great" 的一种可能的表示形式。
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        # s1的前半可被扰乱成s2的前半 且 s1的后半可被扰乱成s2的后半。
        # s1的前半可被扰乱成s2的后半 且 s1的后半可被扰乱成s2的前半。
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False