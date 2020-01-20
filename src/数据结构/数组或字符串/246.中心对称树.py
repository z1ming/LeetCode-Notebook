# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
# 请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。
#
# 示例 1:
#
# 输入:  "69"
# 输出: true
# 示例 2:
#
# 输入:  "88"
# 输出: true
# 示例 3:
#
# 输入:  "962"
# 输出: false
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        ans = ''
        for i in num:
            if i == '2' or i == '3' or i == '4' or i == '5' or i == '7':
                return False
            elif i == '9':
                a = '6'
                ans += a
            elif i == '6':
                a = '9'
                ans += a
            else:
                a = i
                ans += a
            print(ans)
        if num != ans[::-1]:
            return False
        return True