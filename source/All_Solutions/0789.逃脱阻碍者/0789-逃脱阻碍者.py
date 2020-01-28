class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return abs(target[0])+abs(target[1])<min([abs(target[0]-g[0])+abs(target[1]-g[1]) for g in ghosts])