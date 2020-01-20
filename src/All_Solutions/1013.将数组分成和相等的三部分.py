# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
#
#  
#
# 示例 1：
#
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 关键一步：求得每段的和 s
        # count为每段的和，pos作为某段结束的标志
        s = sum(A) / 3
        count, pos = 0, 0
        for i in A:
            count += i
            if count == s and pos == 1:
                return True  # 求得第二段的和，返回True
            if count == s and pos == 0:  # 求得第一段的和，count重置
                count = 0
                pos = 1
        return False

# 时间复杂度： O(N)。N为数组的长度，遍历了一遍数组
# 空间复杂度：O(1)。