#!/usr/bin/env python3

from functools import reduce


def setBitOne(num, *arg):
    """
    将整型数的二进制数指定位置置1
    """
    return num | reduce(lambda num1, num2: (1 << (num1 - 1)) |
            (1 << (num2 - 1)), arg)


def setBitZero(num, *arg):
    """
    将整型数的二进制数指定位置置0
    """
    return num & ~reduce(lambda num1, num2: (1 << (num1 - 1)) |
            (1 << (num2 - 1)), arg)


def main():
    pass


if __name__ == "__main__":
    print(setBitZero(7, 1, 2))
