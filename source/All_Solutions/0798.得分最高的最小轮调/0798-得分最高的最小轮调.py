class Solution:
    def bestRotation(self, A: List[int]) -> int:
        score = 0
        list1 = [0 for i in range(20005)]
        l = len(A)
        k=0
        for i in range(l):
            if A[i]<=i:
                score += 1
                list1[i-A[i]]+=1
        ss=score
        for i in range(1,l):
            x=list1.pop(0)
            list1.append(0)
            list1[l-1-A[0]]+=1
            A.append(A.pop(0))
            ss=ss-x+1
            if score<ss:
                score = ss
                k=i
        return k