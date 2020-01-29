class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s,tmp):
            if not s:
                res.append(tmp)
            for i in range(1,len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        helper(s,[])
        return res