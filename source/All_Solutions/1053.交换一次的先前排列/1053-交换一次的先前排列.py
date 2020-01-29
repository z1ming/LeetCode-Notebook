class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 从后往前找第一个前>后的数字位置，记为tmp
        tmp = -1
        for i in range(len(A)-1, 0, -1):
            if A[i-1] > A[i]:
                tmp = i-1
                break
        
        # 如果tmp为1，即数组为升序排列
        if tmp == -1:
            return A
        
        # 在tmp右边寻找第一个出现的最接近tmp处数字的位置
        index = tmp
        mindiff = float("inf")
        for j in range(tmp+1, len(A)):
            if A[j] < A[tmp]:
                diff = A[tmp] - A[j]
                if mindiff > diff:
                    mindiff = diff
                    index = j
        
        A[tmp], A[index] = A[index], A[tmp]
        return A
        