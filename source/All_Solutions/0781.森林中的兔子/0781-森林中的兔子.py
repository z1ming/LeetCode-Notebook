class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = 0
        temp = {}
        for i in answers:
            if 0==i:
                s+=1
            elif temp.get(i):
                temp[i] += 1
            else:
                temp[i] = 1
        for i in temp.keys():
            if temp[i] > i+1:
                s += temp[i]//(i+1)*(i+1)+i+1 if 0!=temp[i]%(i+1) else temp[i]//(i+1)*(i+1)
            else:
                s += i+1
        return s