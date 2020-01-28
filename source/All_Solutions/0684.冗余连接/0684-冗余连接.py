class Solution:
    """并查集"""
    '''
    记录1到N的每个数的根，因为如果有环，导致环相连的[u, v]一定有相同的root，
    我们可以理解为是一个节点的两个分支，通过[u,v]被连起来了，既然他们是一个节点的两个分支，那么他们一定有相同的root，所以直接移除[u,v]就好啦。
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges)+1)]

        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        for u, v in edges:
            u_parent = find(u)
            v_parent = find(v)
            if u_parent != v_parent:
                root[v_parent] = u_parent
            else:
                return [u, v]