# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
#
# 输入: 100
# 输出: "202"
# 示例 2:
#
# 输入: -7
# 输出: "-10"
# 注意: 输入范围是 [-1e7, 1e7] 。

class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        if num < 0:
            s = '-'
        else:
            s = ''
        while abs(num) // 7 != 0:
            ans += str(abs(num) % 7)
            num = abs(num) // 7
        ans += str(abs(num) % 7)
        return ans[::-1] if s == '' else '-' + ans[::-1]
