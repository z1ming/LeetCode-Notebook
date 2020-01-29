class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = [{'count': 0, 'sum': 0} for _ in range(nodes + 1)]
        for i, (p, v) in [*enumerate(zip(parent, value))][:: -1]:
            tree[i]['sum'] += v
            if tree[i]['sum']:
                tree[p]['count'] += tree[i]['count'] + 1
                tree[p]['sum'] += tree[i]['sum']
        return tree[-1]['count']