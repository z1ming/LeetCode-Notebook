class Solution(object):
    
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        
        def addOne(root, v, d):
            if not root:
                return

            if d == 1:
                newl = TreeNode(v)
                newr = TreeNode(v)
                newl.left = root.left
                newr.right = root.right
                root.left = newl
                root.right = newr
                return

            addOne(root.left, v, d-1)
            addOne(root.right, v, d-1)
        
        addOne(root, v, d-1)
        return root
    