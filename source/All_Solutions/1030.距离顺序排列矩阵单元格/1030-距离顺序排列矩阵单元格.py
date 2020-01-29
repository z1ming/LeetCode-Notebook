class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res=[]
        for i in range(R):
            for j in range(C):
                res.append([abs(r0-i)+abs(c0-j),[i,j]])
        res=sorted(res,key=lambda x:x[0])
        ans=[]
        for i in res:
            ans.append(i[1])
        return ans