# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
#
# 注意：请不要在超过该数组长度的位置写入元素。
#
# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
#
#  
#
# 示例 1：
#
# 输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count_0 = arr.count(0)
        index_l = len(arr) - 1
        index_r = len(arr) - 1 + count_0
        arr.extend([None]*count_0) # 拓展数组长度
        while index_l < index_r:
            if arr[index_l] != 0:
                arr[index_r] = arr[index_l]
                index_l -= 1
                index_r -= 1
            else:
                arr[index_r] = arr[index_r-1] = 0
                index_l -= 1
                index_r -= 2
        for i in range(count_0):  # 还原数组长度
            arr.pop()

