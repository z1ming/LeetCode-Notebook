class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return None
        res = []
        # 使用flag标记当前节点的父节点是否需要删除
        def dfs(root, flag):
            if not root: return 
            if root.val in to_delete:
                dfs(root.left, 1)
                dfs(root.right, 1)
                root = None
            else:
                root.left = dfs(root.left, 0)
                root.right = dfs(root.right, 0)
                # 父节点在需要删除的时候才加入结果
                flag and res.append(root)
            return root

        # 根节点的父节点默认需要删除
        dfs(root, 1)
        return res