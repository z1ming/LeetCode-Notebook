# 给一个嵌套整数序列，请你返回每个数字在序列中的加权和，它们的权重由它们的深度决定。
#
# 序列中的每一个元素要么是一个整数，要么是一个序列（这个序列中的每个元素也同样是整数或序列）。
#
# 与 前一个问题 不同的是，前一题的权重按照从根到叶逐一增加，而本题的权重从叶到根逐一增加。
#
# 也就是说，在本题中，叶子的权重为1，而根拥有最大的权重。
#
# 示例 1:
#
# 输入: [[1,1],2,[1,1]]
# 输出: 8
# 解释: 四个 1 在深度为 1 的位置， 一个 2 在深度为 2 的位置。
# 示例 2:
#
# 输入: [1,[4,[6]]]
# 输出: 17
# 解释: 一个 1 在深度为 3 的位置， 一个 4 在深度为 2 的位置，一个 6 在深度为 1 的位置。 1*3 + 4*2 + 6*1 = 17。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        from collections import defaultdict
        max_level = 0
        d = defaultdict(int)

        def dfs(nested, level):
            nonlocal max_level, d
            max_level = max(max_level, level)
            for i in nested:
                if i.isInteger():
                    d[level] += i.getInteger()
                else:
                    dfs(i.getList(), level + 1)

        dfs(nestedList, 1)
        max_level += 1
        ans = 0
        for k, v in d.items():
            ans += (max_level - k) * v
        return ans

