# 给定一个二叉树，返回它的中序 遍历。
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：“颜色标记法？”
# 兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于
# 前序，中序，后序遍历，能够写出完全一致的代码。
# 其核心思想如下：
# 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
# 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
# 如果遇到的节点为灰色，则将节点的值输出。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE,GRAY = 0,1
        res = []
        stack = [(WHITE,root)]
        while stack:
            color,node = stack.pop()
            if node is None:continue
            if color == WHITE:
                stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                stack.append((WHITE,node.left))
            else:
                res.append(node.val)
        return res

# 方法二：递归
# 极其简单，为什么我还是不会
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # defint a new array res
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

# 方法三：迭代
# 用栈，再用指针模拟访问过程
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出栈顶元素
            p = stack.pop()
            res.append(p.val)
            # 看右子树
            p = p.right
        return res
# 类似相关先序、后序遍历查看https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-he-di-gui-by-powcai/