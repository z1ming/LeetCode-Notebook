# 给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，都有 A[2 * i + 1] = 2 * A[2 * i]” 时，返回 true；否则，返回 false。
#
#  
#
# 示例 1：
#
# 输入：[3,1,3,6]
# 输出：false
# 示例 2：
#
# 输入：[2,1,2,6]
# 输出：false
# 示例 3：
#
# 输入：[4,-2,2,-4]
# 输出：true
# 解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
# 示例 4：
#
# 输入：[1,2,4,16,8,4]
# 输出：false

class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True