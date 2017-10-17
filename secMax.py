#!/usr/bin/env python3

def secMax(numList):
    """
    不重复的第二大数
    """
    fir = sec = None

    for num in numList:
        #  当num在numList中不重复时执行以下代码块
        if numList.count(num) == 1:
            fir, sec = [(fir, sec), (num, num)][fir == None]
            fir = [fir, num][num > fir]
            sec = [sec, num][fir < num < sec or fir == sec and num < sec]

    return sec if fir != sec else None


if __name__ == "__main__":
    pass
