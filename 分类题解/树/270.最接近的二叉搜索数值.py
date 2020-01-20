# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
#
# 注意：
#
# 给定的目标值 target 是一个浮点数
# 题目保证在该二叉搜索树中只会存在一个最接近目标值的数
# 示例：
#
# 输入: root = [4,2,5,1,3]，目标值 target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# 输出: 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：自己的写法
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # 先序遍历的固定模板，题目讲到二叉搜素树，该有有一个重要特征是先序遍历结果为升序
        # 我们使用数组保存排好序的结果，然后找到最接近的值
        res = []
        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        # 如果只有一个数，输出这个数就行了
        if len(res) == 1:
            return res[0]
        elif target >= res[-1]: # 如果目标只不在数组区间内，而在数组区间两侧，那么我们输出res[0]或者res[-1]
            return res[-1]
        elif target <= res[0]:
            return res[0]
        # 如果target在数组区间内，我们遍历一遍数组，比较最近的值
        for i in range(len(res) - 1):
            if res[i] <= target < res[i + 1]:
                if target - res[i] > res[i + 1] -target:
                    return res[i+1]
                elif target - res[i] < res[i+1] - target:
                    return res[i]
# 方法二：题解里比较好的写法
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # 运用递归，利用二叉搜索树左<根<右的特点，我们判断target和结点的大小
        # 如果target比结点小，我们搜索结点的左子树，反之搜索右子树
        # 如果target距离左孩子的距离比target到结点的距离近，结果为左孩子，反之结果为结点值
        res = root.val
        if target < root.val and root.left:
            left = self.closestValue(root.left, target)
            # 如果target距离左孩子更近
            if abs(res - target) >= abs(left - target):
                res = left
        elif target > root.val and root.right:
            right = self.closestValue(root.right, target)
            if abs(res - target) >= abs(right - target):
                res = right
        return res