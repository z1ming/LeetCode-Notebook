class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1:
            x_max=0
        else:
            j=0
            i=x**j
            while(i<=bound):
                j+=1
                i=x**j           
            x_max=j-1
        if y==1:
            y_max=0  
        else:
            j=0
            i=y**j
            while(i<=bound):
                j+=1
                i=y**j           
            y_max=j-1
        res=[]        
        for i in range(max(x_max,y_max)+1):
            for j in range(min(x_max,y_max)+1):
                if x_max>=y_max:
                    cur=x**i + y**j
                else:
                    cur=y**i + x**j
                if cur<=bound:
                    res.append(cur)    
        return list(set(res))