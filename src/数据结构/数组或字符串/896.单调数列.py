# 如果数组是单调递增或单调递减的，那么它是单调的。
#
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
#
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
# 使用all()函数
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
        all(A[i] >= A[i+1] for i in range(len(A) - 1)))
# 时间复杂度：O（N）N是A的长度。遍历了两次。
# 空间复杂度：O（1）。