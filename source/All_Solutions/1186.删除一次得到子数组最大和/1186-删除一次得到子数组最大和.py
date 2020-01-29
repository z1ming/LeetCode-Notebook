class Solution:
    def maximumSum(self, arr):
        sumre = [0]*(len(arr))
        resre = [0]*len(arr)
        sumre[0] = arr[0]
        resre[0] = arr[0]
        res = arr[0]
        for i in range(1,len(arr)):
            sumre[i] = max(sumre[i-1]+arr[i],arr[i])
            resre[i] = max(sumre[i-1],resre[i-1]+arr[i])
            res = max(res,max(sumre[i],resre[i]))
        return res