#!/usr/bin/env python3
# coding="utf-8"

# 已知1900年1月1日是星期一，输出指定年份的所有黑色星期五
#   每月13日为星期五则为黑色星期五

def blackFridayInYear(year):
    dayNum = 0 # 用于从1900年1月1日起累计天数

    # 计算从1900年到(year-1)年的累计天数
    for yearValue in range(1900, year):
        if yearValue % 4 == 0 and yearValue % 100 != 0:
            dayNum += 366
        elif yearValue % 400 == 0:
            dayNum += 366
        else:
            dayNum += 365

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        listDayOfMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    else:
        listDayOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    # 通过讲累计天数对7求余判断当月13日是否为黑色星期
    num = 0 # 用于累计year年黑色星期五的数量
    for i in range(12):
        dayNum = dayNum + listDayOfMonth[i]
        if (dayNum + 13) % 7 == 5:
            num += 1
            print("%d年%d月13日是黑色星期五。" % (year, i + 1))
    print("%d年共有%d天是黑色星期五。" % (year, num))

if __name__ == "__main__":
    while True:
        year = int(input("请输入一个1900年后的年份，用于输出该年份所有的黑色星期五（数字0退出程序）："))
        if year == 0:
            break
        blackFridayInYear(year)

