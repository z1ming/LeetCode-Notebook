###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def daysInMonth(year,month):
    if month == 1 or month == 3 or month == 5 \
        or month == 7 or month == 8 or month == 10 \
        or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        return 30

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < daysInMonth(year,month):
        return year,month,day+1
    else:
        if month == 12:
            return year + 1,1,1
        else:
            return year,month+1,1

def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    days = 0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        days += 1
        year1,month1,day1 = nextDay(year1,month1,day1)
    return days


def test():
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,2,30,2013,3,1) == 1
    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,4,30) == (2013,5,1)
    assert nextDay(2012,12,31) == (2013,1,1)
    assert daysBetweenDates(2013, 1, 1,2014, 1, 1) == 365
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    print("Test finished.")

test()