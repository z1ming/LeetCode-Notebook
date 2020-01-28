class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []                                 

        cur_layer = [root]                            
        res = []                                        # 结果列表，存放各层均值
        while cur_layer:                         
            # 将当前层结点平均值添加到结果中
            res.append(sum(node.val for node in cur_layer) / len(cur_layer))

            next_layer = []                             
            for node in cur_layer:                      # 遍历上一层结点列表中的各个结点

                if node.left:                           # 如果存在左子树
                    next_layer.append(node.left)        # 添加左孩子到下一层列表
                if node.right:                 
                    next_layer.append(node.right) 

            cur_layer = next_layer                      # 更新上一层结点列表

        return res   