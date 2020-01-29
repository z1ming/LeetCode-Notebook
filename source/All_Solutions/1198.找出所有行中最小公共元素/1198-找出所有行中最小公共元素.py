class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        flatten = sum(mat,[])  # 把二维矩阵展开成一维
        dic = Counter(flatten) # 统计所有元素频率
        for num in mat[0]: # 在第一行元素里找有没有出现频率等于mat行数的元素
            if dic[num] == len(mat): # 第一次满足条件的元素就是答案
                return num
        return -1