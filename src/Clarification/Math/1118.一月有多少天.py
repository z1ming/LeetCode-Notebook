# 指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。
#
#  
#
# 示例 1：
#
# 输入：Y = 1992, M = 7
# 输出：31
# 示例 2：
#
# 输入：Y = 2000, M = 2
# 输出：29
# 示例 3：
#
# 输入：Y = 1900, M = 2
# 输出：28

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        def is_leapyear(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True
            return False
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            return 31
        if M == 4 or M == 6 or M == 9 or M == 11:
            return 30
        if M == 2:
            if is_leapyear(Y) == True:
                return 29
            else:
                return 28