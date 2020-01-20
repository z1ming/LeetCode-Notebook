# 给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。
#
# 返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。
#
#  
#
# 示例：
#
# 输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# 输出: [1,5]
# 解释: 只有 1 和 5 同时在这三个数组中出现.
#  
#
# 提示：
#
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        dic = {}
        for i in arr1:
            dic[i] = dic.get(i,0) + 1
        for j in arr2:
            dic[j] = dic.get(j,0) + 1
        for k in arr3:
            dic[k] = dic.get(k,0) + 1
        ans = []
        for key,value in dic.items():
            if value == 3:
                ans.append(key)
        return ans
# 时间复杂度：O（N），遍历了3个数组，1个字典。
# 空间复杂度：O（N），使用了dic和ans保存结果。