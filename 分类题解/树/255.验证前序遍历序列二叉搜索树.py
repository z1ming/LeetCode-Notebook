# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
#
# 你可以假定该序列中的数都是不相同的。
#
# 参考以下这颗二叉搜索树：
#
#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：
#
# 输入: [5,2,6,1,3]
# 输出: false
# 示例 2：
#
# 输入: [5,2,1,3,6]
# 输出: true

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        root = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] < root: return False
            while stack and preorder[i] > stack[-1]:
                root = stack.pop()
            stack.append(preorder[i])
        return True