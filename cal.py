#!/usr/bin/env python3
# coding="utf-8"

# 通过年份和月份调取日历信息
#   默认调取当前年份月份的日历信息
#   单独提交年份调取一整年的日历信息
#   提交年份月份调取该年份月份的日历信息

import datetime
import calendar

weekdayList = ['日', '一', '二', '三', '四', '五', '六'] 
monthList = [
        '一月', '二月', '三月', '四月', '五月', '六月',
        '七月', '八月', '九月', '十月', '十一月', '十二月'
        ]

def calNameOfWeek():
	for weekday in weekdayList:
		print(weekday.rjust(2), end='')

def calBlank(idx):
	for blankDay in range(idx):
		print(''.rjust(3), end='')

def calDayOfWeek(start, stop):
	for day in range(start, stop + 1):
		print(str(day).rjust(3), end='')

def cal(year=None, month=None):
	if year:
		year = int(year)
		if month:
			month = int(month)
			print((monthList[month - 1] + ' ' + str(year)).center(21))
			firstDayWeekday, monthRange = calendar.monthrange(year, month)
			idx = (firstDayWeekday + 1) % 7
			calNameOfWeek()
			print()
			calBlank(idx)
			calDayOfWeek(1, 7 - idx)
			print()
			for row in range(5):
				if (14 - idx) + row * 7 <= monthRange:
					calDayOfWeek((7 - idx + 1) + row * 7, (14 - idx) + row * 7)
					print()
				elif (7 - idx + 1) + row * 7 <= monthRange:
					calDayOfWeek((7 - idx + 1) + row * 7, monthRange)
					print()
				else:
					print()
		else:
			print(str(year).center(65))
			for row in range(4):
				print(monthList[row * 3 ].center(21), end=' ')
				print(monthList[row * 3 + 1].center(18), end=' ')
				print(monthList[row * 3 + 2].center(20), end=' ')
				print()
				for i in range(3):
					calNameOfWeek()
					print('', end=' ')
				print()
				firstDayWeekday1, monthRange1 = calendar.monthrange(year, row * 3 +1)
				firstDayWeekday2, monthRange2 = calendar.monthrange(year, row * 3 +2)
				firstDayWeekday3, monthRange3 = calendar.monthrange(year, row * 3 +3)
				idx1 = (firstDayWeekday1 + 1) % 7
				idx2 = (firstDayWeekday2 + 1) % 7
				idx3 = (firstDayWeekday3 + 1) % 7
				for idx in [idx1, idx2, idx3]:
					calBlank(idx)
					calDayOfWeek(1, 7 - idx)
					print('', end=' ')
				print()
				for line in range(5):
					for idx, monthRange in zip([idx1, idx2, idx3], [monthRange1, monthRange2, monthRange3]):
						if (14 - idx) + line * 7 <= monthRange:
							calDayOfWeek((7 - idx + 1) + line * 7, (14 - idx) + line * 7)
						elif (7 - idx + 1) + line * 7 <= monthRange:
							calDayOfWeek((7 - idx + 1) + line * 7, monthRange)
							calBlank(7 - (monthRange - ((7 - idx + 1) + line * 7) + 1))
						else:
							calBlank(7)
						print('', end=' ')
					print()
				print()

	else:
		year = datetime.date.today().year
		if month:
			month = int(month)
		else:
			month = datetime.date.today().month
		print((monthList[month - 1] + ' ' + str(year)).center(21))
		firstDayWeekday, monthRange = calendar.monthrange(year, month)
		idx = (firstDayWeekday + 1) % 7
		calNameOfWeek()
		print()
		calBlank(idx)
		calDayOfWeek(1, 7 - idx)
		print()
		for row in range(5):
			if (14 - idx) + row * 7 <= monthRange:
				calDayOfWeek((7 - idx + 1) + row * 7, (14 - idx) + row * 7)
				print()
			elif (7 - idx + 1) + row * 7 <= monthRange:
				calDayOfWeek((7 - idx + 1) + row * 7, monthRange)
				print()
			else:
				print()


if __name__ == "__main__":
    year = input('请输入年份：')
    month = input('请输入月份：')
    cal(year, month)
