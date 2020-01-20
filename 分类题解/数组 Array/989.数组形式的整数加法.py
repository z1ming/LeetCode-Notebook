# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
#
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
#
#  
#
# 示例 1：
#
# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = ''
        for i in A:
            a += str(i)  # 提取a
        s = int(a) + K # 相加
        return [x for x in str(s)]