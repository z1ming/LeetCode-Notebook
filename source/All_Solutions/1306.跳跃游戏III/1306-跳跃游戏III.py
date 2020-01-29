class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q, v, n = [start], {start}, len(arr)
        while q:
            p = []
            for i in q:
                if not arr[i]:
                    return True
                for j in i - arr[i], i + arr[i]:
                    if 0 <= j < n and j not in v:
                        p.append(j)
                        v.add(j)
            q = p
        return False