#!/usr/bin/env python3

import datetime
import calendar
import sys


def yearPrint(year):
    """
    整年日历的头部打印
    """
    print(("%d年" % year).center(65))


def monthPrint(month, year=None):
    if year:
        #  某月日历的日历头部打印
        print(("%d月 %d年" % (month, year)).center(20))
    else:
        #  整年日历下各个月份日历的头部打印
        print(("%d月" % month).center(21), end="")


def weekPrint():
    """
    日历星期信息打印
    """
    print(" 日 一 二 三 四 五 六", end=" ")


def dayPrint(year, month, start, stop, op=1):
    """
    日历号码打印
    """
    date = datetime.date.today()
    y, m, d = date.year, date.month, date.day
    s1 = "   " * (7 - (stop - start + 1))
    s2 = ""
    flag = False

    if year == y and month == m:
        flag = True

    for day in range(start, stop + 1):
        if flag and day == d:
            if len(str(day)) == 1:
                s2 += ("  \033[47m%d\033[0m" % day)
            elif len(str(day)) == 2:
                s2 += (" \033[47m%d\033[0m" % day)
        else:
            s2 += str(day).rjust(3)

    if op == 1:
        print(s1 + s2, end=" ")
    elif op == 2:
        print(s2 + s1, end=" ")


def calDataInit(year, month):
    firstDayWeek, maxNum = calendar.monthrange(year, month)
    start = 7 - (firstDayWeek + 1) % 7 + 1

    return start, maxNum


def calMonth(year, month):
    start, maxNum = calDataInit(year, month)

    monthPrint(month, year)

    weekPrint()
    print()

    dayPrint(year, month, 1, start - 1)
    print()

    for i in range(5):
        if start + 7 * (i + 1) - 1 <= maxNum:
            dayPrint(year, month, start + 7 * i, start + 7 * (i + 1) - 1)
            print()
        elif start + 7 * i <= maxNum:
            dayPrint(year, month, start + 7 * i, start + 7 * (i + 1) - 1, op=2)
            print()
            break


def cal3Month(year, first):
    start1, maxNum1 = calDataInit(year, first)
    start2, maxNum2 = calDataInit(year, first + 1)
    start3, maxNum3 = calDataInit(year, first + 2)
    start = [start1, start2, start3]
    maxNum = [maxNum1, maxNum2, maxNum3]

    for i in range(3):
        monthPrint(start[i])
    print()

    for j in range(3):
        weekPrint()
    print()

    for k in range(3):
        dayPrint(year, first + k, 1, start[k] - 1)
    print()

    for l in range(5):
        for m in range(3):
            if start[m] + 7 * (l + 1) - 1 <= maxNum[m]:
                dayPrint(year, first + m, start[m] + 7 * l,
                        start[m] + 7 * (l + 1) - 1)
            elif start[m] + 7 * l <= maxNum[m]:
                dayPrint(year, first + m, start[m] + 7 * l,
                        maxNum[m], op=2)
            else:
                print(" ".rjust(22), end="")

        print()

    print()


def cal(year=None, month=None):
    if year:
        year = int(year)

        if month:
            month = int(month)

            calMonth(year, month)
        else:
            yearPrint(year)

            for i in range(4):
                cal3Month(year, 1 + 3 * i)
    else:
        year = datetime.date.today().year

        if month:
            month = int(month)
        else:
            month = datetime.date.today().month

        calMonth(year, month)


if __name__ == "__main__":
    year = month = None

    if len(sys.argv) == 2:
        year = int(sys.argv[1])
    elif len(sys.argv) == 3:
        year = int(sys.argv[1])
        month = int(sys.argv[2])

    cal(year, month)
