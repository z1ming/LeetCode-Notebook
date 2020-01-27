class Solution:
    def magicalString(self, n: int) -> int:
        ans,i = [1],0
        for i in range(n):
            if ans[i]==2:
                ans.append(ans[-1])
            ans.append(ans[-1]^3)
        return ans[:n].count(1)
