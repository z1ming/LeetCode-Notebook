# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 方法一： 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归的模板记住就行了，是固定的。只需要改变下面三行代码的顺序
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return []
            # 以下三行按照左->根->右的顺序写即可，不同遍历方式按照不同的顺序写
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res
# time: O(N)。我们遍历了所有结点
# space: O(N)。输出使用了数组

# 方法二：迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # 使用栈进行迭代
        stack, output = [], []
        # 使用指针cur跟踪结点位置
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            output.append(cur.val)
            cur = cur.right
        return output
# time: O(N)。我们遍历了所有结点
# space: O(N)。输出使用了栈保存结点，使用数组保存结果

# 方法三：莫里斯遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        cur = root
        while cur:
            if not cur.left:
                output.append(cur.val) # 将current添加到输出
                cur = cur.right        # 进入右子树
            else:
                pre = cur.left         # 在current的左子树中，领cur成为最右侧结点的右子结点
                while pre.right:
                    pre = pre.right
                pre.right = cur
                tmp = cur
                cur = cur.left         # 进入左子树
                tmp.left = None
        return output
# time:O(N)。想证明时间复杂度是O(N)，最大的问题是找到每个结点的前驱结点的时间复杂度。乍一想，找到
# 每个节点的前驱节点的时间复杂度应该是O(NlogN)，因为找到一个节点的前驱节点和树的高度有关。
# 但事实上，找到所有节点的前驱节点只需要O(N)时间。一棵N个节点的二叉树只有n-1条边，每条边只可能使用2次，一次是定位点，
# 一次是找前驱节点。
# space:O(N)。使用了长度为N的数组。