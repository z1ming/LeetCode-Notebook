class Solution:
    def __init__(self):
        self.s = set()
        self.nums = []
        
    def dfs(self, st: int, cur: List[int]):
        # print(cur)
        if len(cur) >= 2:
            self.s.add(tuple(cur))
        for i in range(st, len(self.nums), 1):
            if len(cur) > 0 and cur[-1] > self.nums[i]:
                continue   
            cur.append(self.nums[i])    
            self.dfs(st=i + 1, cur=cur)
            cur.pop()
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs(st=0, cur=[])
        return [list(a) for a in self.s]

