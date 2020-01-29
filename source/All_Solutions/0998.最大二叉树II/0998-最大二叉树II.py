class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        new = TreeNode(val)
        pre = None
        node = root
        while node!= None and node.val > val:
            pre = node
            node = node.right
        if pre == None:
            new.left = node
            return new
        elif node == None:
            pre.right = new
        else:
            new.left = node
            pre.right = new
        return root