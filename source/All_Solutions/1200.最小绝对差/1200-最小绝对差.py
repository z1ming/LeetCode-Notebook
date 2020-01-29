class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_dis = abs(arr[1] - arr[0])
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) <min_dis:
                min_dis = abs(arr[i]-arr[i-1])
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) ==min_dis:
                result.append([arr[i-1],arr[i]])
        return result