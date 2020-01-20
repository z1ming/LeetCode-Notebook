# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
#
# 如果有多个目标子集，返回其中任何一个均可。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2] (当然, [1,3] 也正确)
# 示例 2:
#
# 输入: [1,2,4,8]
# 输出: [1,2,4,8]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1:set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0),key = len) | {x}
        return list(max(S.values(),key = len))