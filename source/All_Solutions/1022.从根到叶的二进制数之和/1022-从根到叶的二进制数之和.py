class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        record = []
        sm = 0
        result = 0
        
        # 使用中序遍历来求和
        while record or root:
            while root:
                sm = 2*sm + root.val
                record.append([root, sm])
                root = root.left
            
            # 如果是已经遍历到最左，开始通过pop来向root方向返回遍历时
            # 就不会执行上面的while，而直接pop，重新给sm赋值
            # 所以record里存sm是有用的
            node, sm = record.pop()
            
            # 只有到叶子节点才将结果累加到result
            if not node.left and not node.right:
                result += sm
            
            root = node.right
        
        return result