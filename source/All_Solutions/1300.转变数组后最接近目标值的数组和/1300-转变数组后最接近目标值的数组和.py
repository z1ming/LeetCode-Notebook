class Solution:
    def findBestValue(self, arr, target: int):
        
        temp = [0] * len(arr)
            
        arr.sort()
            
        c = 0
        for i in range(len(arr)):
            c += arr[i]
            temp[i] = c
        
        def lowerBound(arr, begin, end, target):
            while begin < end:
                mid = begin + (end - begin) // 2
                if arr[mid] < target:
                    begin = mid + 1
                else:
                    end = mid
            return begin
    
        def cal(m):
            index = lowerBound(arr, 0, len(arr), m)
            return (temp[index - 1] if index - 1 >= 0 else 0) + m * (len(arr) - index)

        s = 0
        e = arr[-1]
        while s < e:
            m = s + (e - s) // 2
            if cal(m) < target:
                s = m + 1
            else:
                e = m
        if abs(cal(s) - target) >= abs(cal(s - 1) - target):
            return s - 1
        return s