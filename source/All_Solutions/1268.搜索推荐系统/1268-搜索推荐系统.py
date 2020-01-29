class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n=len(searchWord)
        products.sort()
        ans=[]
        for i in range(1,n+1):
            res=[]
            for j in products:
                if j[0:i]==searchWord[0:i]:
                    res.append(j)
            products=res
            ans.append(res[0:3])
        return ans