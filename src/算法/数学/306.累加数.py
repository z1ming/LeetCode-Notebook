# 累加数是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
#
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 示例 1:
#
# 输入: "112358"
# 输出: true
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2:
#
# 输入: "199100199"
# 输出: true
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(sub1,sub2,num):
            if not num:
                return True
            sub1,sub2 = sub2,str(int(sub1) + int(sub2))
            return num.startswith(sub2) and isValid(sub1, sub2, num[len(sub2):])

        n = len(num)
        for i in range(1,n // 2 + 1):
            if num[0] == "0" and i > 1: return False
            sub1 = num[:i]
            for j in range(1,n):
                # 剩下的长度都没有前面两个数最大长度长
                if max(i,j) > n - i - j:break
                if num[i] == "0" and j > 1:break
                sub2 = num[i:i+j]
                # 找到两个数，看后面的数是否能引出来
                if isValid(sub1, sub2, num[i+j:]):return True
        return False