# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树
# T
# 的两个结点
# p、q，最近公共祖先表示为一个结点
# x，满足
# x
# 是
# p、q
# 的祖先且
# x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
#
# 示例
# 1:
#
# 输入: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# 输出: 3
# 解释: 节点
# 5
# 和节点
# 1
# 的最近公共祖先是节点
# 3。
# 示例
# 2:
#
# 输入: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# 输出: 5
# 解释: 节点
# 5
# 和节点
# 4
# 的最近公共祖先是节点
# 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
# 说明:
#
# 所有节点的值都是唯一的。
# p、q
# 为不同节点且均存在于给定的二叉树中。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归
# 1.从跟节点开始遍历树
# 2.如果当前节点本身是p或q中的一个，我们会将变量mid标记为true，并继续搜索左右分支中的另一个节点
# 3.如果左分支或右分支中的任何一个返回true，则表示在下面找到了两个节点中的一个
# 4.如果在遍历的任何点上，左、右或中三个标志中的任意两个变为true，以为这我们找到了节点p和q的最近公共祖先。
class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left +right >=2:
                self.ans = current_node
            return mid or left or right
        recurse_tree(root)
        return self.ans
# 时间复杂度：O(N)，N是二叉树中的节点数，最坏情况下，我们需要访问二叉树的所有节点。
# 空间复杂度：O(N)，这是因为递归堆栈使用的最大空间位N，斜二叉树的高度可以是N。

# 方法二：使用父指针迭代
# 1.从根节点开始遍历树
# 2.在找到p和q之前，将父指针存储在字典中
# 3.一旦我们找到了p和q，我们就可以使用父亲字典获得p的所有祖先，并添加到一个称为祖先的集合中。
# 4.同样，我们遍历了节点q的祖先。如果祖先存在于为p设置的祖先中，这意味着这是p和q之间的第一个共同祖先（同时向上遍历），因此这是LCA节点。
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            # while traversing the tree,keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q while appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
# 时间复杂度：O（N）。其中N是二进制中的节点数，在最坏的情况下，我们可能会访问二叉树的所有节点。
# 空间复杂度：O（N）。在堆栈使用的最坏情况下，每个节点的父指针字典和祖先集的空间为N，斜二叉树的高度可能为N。

# 方法3：无父指针（太难了，还没理解）
# 算法：
#
# 从根节点开始。
# 将 (root, root_state) 放在堆栈上。root_state 定义要遍历该节点的一个子节点还是两个子节点。
# 当堆栈不为空时，查看堆栈的顶部元素，该元素表示为 (parent_node, parent_state)。
# 在遍历 parent_node 的任何子节点之前，我们检查 parent_node 本身是否是 p 或 q 中的一个。
# 当我们第一次找到 p 或 q 的时候，设置一个布尔标记，名为 one_node_found 为 true 。还可以通过在变量 LCA_index 中记录堆栈的顶部索引来跟踪最近的公共祖先。因为堆栈的所有当前元素都是我们刚刚发现的节点的祖先。
# 第二次 parent_node == p or parent_node == q 意味着我们找到了两个节点，我们可以返回 LCA node。
# 每当我们访问 parent_node 的子节点时，我们将 (parent_node, updated_parent_state) 推到堆栈上。我们更新父级的状态为子级/分支已被访问/处理，并且相应地更改状态。
# 当状态变为 BOTH_DONE 时，最终会从堆栈中弹出一个节点，这意味着左、右子树都被推到堆栈上并进行处理。如果 one_node_found 是 true 的，那么我们需要检查被弹出的顶部节点是否可能是找到的节点的祖先之一。在这种情况下，我们需要将LCA_index减少一个。因为其中一位祖先被弹出了。
# 当同时找到 p 和 q 时，LCA_index 将指向堆栈中包含 p 和 q 之间所有公共祖先的索引。并且 LCA_index 元素具有p和q之间的最近公共祖先。
class Solution:

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None
# 时间复杂度：O(N)O(N)，其中 NN 是二叉树中的节点数。在最坏的情况下，我们可能会访问二叉树的所有节点。这种方法的优点是可以减少回溯。只要找到两个节点，我们就返回。
# 空间复杂度：O(N)O(N)，在最坏的情况下，堆栈使用的空间是 NN 且斜二叉树的高度可能是 NN。

