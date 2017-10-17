#!/usr/bin/env python3

from functools import reduce


def transform(*arg):
    """
    位操作量化
    """
    return reduce(lambda n1, n2: (1 << (n1 - 1)) | (1 << (n2 - 1)), arg)


def setOne(num, *arg):
    """
    将整型数的二进制数指定位置置1
    """
    return num | transform(*arg)


def setZero(num, *arg):
    """
    将整型数的二进制数指定位置置0
    """
    return num & ~transform(*arg)


if __name__ == "__main__":
    pass

