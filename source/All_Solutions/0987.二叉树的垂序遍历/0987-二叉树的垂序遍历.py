class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # 字典d的key存放结点，value存放该结点的x、y坐标以及按先序遍历被访问到的index
        self.d = {} # node: (x, y, index)
        
        def dfs(root, x, y, idx):
            if not root:
                return 
            self.d[root] = [x, y, idx]
            dfs(root.left, x-1, y-1, idx+1)
            dfs(root.right, x+1, y-1, idx+2)
        dfs(root, 0, 0, 0)

        # 排序细节，容易出错！
        # 1.按 x 从小到大排，相当于从左向右垂直遍历树
        # 2.按 y 从大到小排，即当x坐标相同时先出现的点（y更大）先加入列表
        # 3.当x，y都相同时（即坐标完全一样），按结点的值从小到大排序
        dd = sorted(self.d.items(), key=lambda x: (x[1][0], -x[1][1], x[0].val)) # dd类型：list
        res, tmp = [],[]
        pre = dd[0][1][0] # pre 用来判断当前访问的结点和上一个结点是否处在同一根垂直线上
        for item in dd:
            node, pos = item
            if pos[0] == pre:
                tmp.append(node.val)
            else:
                res.append(tmp)
                pre = pos[0]
                tmp = [node.val]
        if tmp: # 最后的 tmp 中可能还有残留，补上！
            res.append(tmp)
        return res

