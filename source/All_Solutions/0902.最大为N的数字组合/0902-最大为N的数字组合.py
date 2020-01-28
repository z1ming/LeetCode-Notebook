class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        index = 0
        N = str(N)
        index = len(N)
        
        if D == [] or index == 0:
            return 0   
        result = 0
    
        while index-1:
            result = result + len(D)**(index-1)
            index = index - 1
        if len(D) < len(N) and int(D[-1]) < int(N[0]):
            result = result + len(D)**(len(N))
            return result

        pd = len(D)-1
        pn = 0
        while pn <= len(N)-1 and pd >= 0:
            if D[pd] < N[pn]:  
                result = result + (pd+1)*(len(D))**(len(N)-pn-1)
                break
            elif D[pd] == N[pn]:
                if pn == len(N)-1:
                    result = result + pd + 1
                    break
                result = result + (pd)*(len(D))**(len(N)-pn-1)       
                pd = len(D)-1
                pn = pn + 1
            else:
                pd = pd - 1
            
        return result    