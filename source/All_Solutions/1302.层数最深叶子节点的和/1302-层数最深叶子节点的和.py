class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root == None:
            return 0;
        queue = [];
        res = 0;
        resList = [];
        queue.append(root);
        while(queue):
            length = len(queue);
            for i in range(length):
                res += queue[0].val;
                if queue[0].left:
                    queue.append(queue[0].left);
                if queue[0].right:
                    queue.append(queue[0].right);
                del queue[0];
            resList.append(res);
            res = 0;
        return resList[-1];