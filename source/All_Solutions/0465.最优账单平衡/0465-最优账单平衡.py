class Solution(object):
    def __init__(self):
        self.mins = float("inf")
    def Baolifa(self,surplus_a,surplus_b,ao,bo,s,count):
        if ao == len(surplus_a) and bo == len(surplus_b):
            self.mins = min(self.mins, count)
            return self.mins
        if ao == len(surplus_a) or bo == len(surplus_b):
            return self.mins
        for i in range(s, len(surplus_a)):
            for j in range(len(surplus_b)):
                a = surplus_a[i]
                b = surplus_b[j]
                r = a + b
                if r > 0:
                    surplus_a[i] = r
                    surplus_b[j] = 0
                    self.Baolifa(surplus_a,surplus_b,ao,bo+1,i,count+1)
                elif r < 0:
                    surplus_a[i] = 0
                    surplus_b[j] = r 
                    self.Baolifa(surplus_a,surplus_b,ao+1,bo,i+1,count+1)
                else:
                    surplus_a[i] = 0
                    surplus_b[j] = 0
                    self.Baolifa(surplus_a,surplus_b,ao+1,bo+1,i+1,count+1)
                surplus_a[i] = a 
                surplus_b[j] = b   

    def minTransfers(self, transactions):
        surplus_a, surplus_b = [], []## surplus_a表示正余额，surplus_a表示负余额
        surplus = {}##surplus存储余额
        ao, bo = 0, 0 ## ao表示正余额列表0的个数，bo表示负余额0的个数
        s, count = 0,0  ## s为每次配对的值，count表示配对次数
        for i in range(len(transactions)):
            x = transactions[i][0]
            y = transactions[i][1]
            if surplus.get(x)==None:
                surplus[x] = 0
            if surplus.get(y)==None:
                surplus[y] = 0
            surplus[x] =surplus.get(x) - transactions[i][2]
            surplus[y] =surplus.get(y) + transactions[i][2]
        for i in surplus:
            if surplus[i]> 0:
                surplus_a.append(surplus[i])
            elif surplus[i]< 0 :
                surplus_b.append(surplus[i])
        for a in range(len(surplus_a)):
            for b in range(len(surplus_b)):
                if surplus_a[a] + surplus_b[b]==0:
                    surplus_a[a] = 0 
                    surplus_b[b] = 0
        i = 0
        while True:
            if i==len(surplus_a):
                break
            if surplus_a == []:
                break
            if surplus_a[i] == 0:
                del surplus_a[i]
                i = 0
                count+=1
            i+=1
        j = 0
        while True:
            if j==len(surplus_b):
                break
            if surplus_b == []:
                break
            if surplus_b[j] == 0:
                del surplus_b[j]
                j = 0
            j+=1
        self.Baolifa(surplus_a,surplus_b,ao,bo,s,count)
        return self.mins

