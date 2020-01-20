# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
#  
#
# 示例 1：
#
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
# 示例 2：
#
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
# 示例 3：
#
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
# 方法一：库
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dic = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',
               5:'Friday',6:'Saturday',0:'Sunday'}
        week_num = int(datetime.datetime(year,month,day).strftime("%w"))
        return dic[week_num]

# 方法二：暴力法
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # 判断是否为闰年
        def isLeapYear(year):
            if year % 400 == 0:
                return True
            elif year % 100 == 0:
                return False
            elif year % 4 == 0:
                return True
            return False

        # 判断一个月有多少天
        def daysInMonth(year, month):
            if month == 1 or month == 3 or month == 5 or month == 7 \
                    or month == 8 or month == 10 or month == 12:
                return 31
            else:
                if month == 2:
                    if isLeapYear(year):
                        return 29
                    else:
                        return 28
                return 30

        # 判断下一天的日期
        def nextDay(year, month, day):
            if day < daysInMonth(year, month):  # 2015.3.4 -> 2015.3.5
                return year, month, day + 1
            else:
                if month == 12:  # 2015.12.31 -> 2016.1.1
                    return year + 1, 1, 1
                else:  # 2015.5.31 -> 2015.6.1
                    return year, month + 1, 1

        # 判断是否为曾经的日期
        def dateIsBefore(year1, month1, day1, year2, month2, day2):
            if year1 < year2:
                return True
            if year1 == year2:
                if month1 < month2:
                    return True
                if month1 == month2:
                    return day1 < day2
            return False

        # 判断日期之间的天数
        def daysBetweenDates(year1, month1, day1, year2, month2, day2):
            days = 0
            while dateIsBefore(year1, month1, day1, year2, month2, day2):
                days += 1
                year1, month1, day1 = nextDay(year1, month1, day1)
            return days

        # 判断为星期几
        dic = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
               4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        # 1971.1.1是星期五，通过给定日期与该日期的天数确定星期几
        days = daysBetweenDates(1971, 1, 1, year, month, day)
        return dic[(days + 5) % 7]