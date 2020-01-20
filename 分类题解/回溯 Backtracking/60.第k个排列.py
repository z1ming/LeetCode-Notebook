# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        z = 1
        l = []
        for i in range(1,n+1):
            z *= i # 计算排列数量
            l.append(i) # 生成排列所用列表
        s = ""
        k = k - 1
        while n > 0:
            z = z/n # 计算当前位置每种数字的情况个数
            h = int(k/z)
            s += str(l[h])
            del l[h]
            k %= z
            n -= 1
        return s