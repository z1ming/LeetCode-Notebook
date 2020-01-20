# 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
#
# 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
#
#  
#
# 示例 1：
#
# 输入：[0,1,1]
# 输出：[true,false,false]
# 解释：
# 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。

# 方法一
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        # 初始化结果[None,None,...,None]
        res = [None for _ in range(len(A))]
        s = ''
        for i,value in enumerate(A):
            s += str(value)
            if int(s,2) % 5 == 0: # 使用int(n,2)将二进制转化为10进制
                res[i] = True
            else:
                res[i] = False
        return res

# 方法二
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        d = 0
        ans = []
        for i in A:
            d = (d<<1)|i  # 二进制运算
            ans.append(not d%5)
            d%=5
        return ans