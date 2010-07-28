#!/usr/bin/env python
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?
# Of course, we don't use standart Python library

def isLeap(year):
    if ((year%4==0) and (year%100!=0)) or year%400==0:
        return True
    return False

def DayInMonth(month, year):
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    res = days[month-1]
    if month==2 and isLeap(year): res+=1
    return res

cnt = 0
day = 6
month = 1
year = 1901
while year<2001:
    print "%s-%s-%s" % (day, month, year)
    if day==1: cnt+=1
    day+=7
    if day>DayInMonth(month, year):
        day = 7-DayInMonth(month, year)+(day-7)
        month+=1
        if month>12:
            month=1
            year+=1
print "Res=", cnt
