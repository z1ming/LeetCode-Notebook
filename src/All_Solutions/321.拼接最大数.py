# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
#
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
#
# 示例 1:
#
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 示例 2:
#
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 取num1可以形成i位最大数字，num2k-i位最大数字
        def getMaxarr(nums, i):
            if not i:
                return []
            # pop 表示不要nums里的数字个数
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num:
                    pop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:i]

        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                tmp1 = getMaxarr(nums1, i)
                tmp2 = getMaxarr(nums2, k - i)
                # 合并
                tmp = merge(tmp1, tmp2)
                if res < tmp:
                    res = tmp
        return res