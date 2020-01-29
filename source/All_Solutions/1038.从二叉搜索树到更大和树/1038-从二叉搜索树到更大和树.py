class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def postOrder(nd, acc=0)->int:
            if not nd:return acc
            nd.val +=  postOrder(nd.right,acc)
            return postOrder(nd.left,nd.val)
            
        postOrder(root)
        return root