class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        a = [0 for x in range(N+1)] #相信你的人
        b = [0 for x in range(N+1)] #你相信的人

        for num in trust:
            a[num[1]] += 1   #存储的为相信他的人
            b[num[0]] += 1

        for i,num in enumerate(a):
            if(i!=0 and num == N-1): #所有人都相信法官
                if(b[i] == 0): #法官不相信任何人
                    return i
        return -1