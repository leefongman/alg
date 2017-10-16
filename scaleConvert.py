#!/usr/bin/env python3

def tenToCh(num):
    """
    数字转字符
    """
    if num < 10:
        return chr(num + 48)
    elif num >= 10:
        return chr(97 + num - 10)


def tenToX(num, x):
    """
    十进制转x进制
    """
    if num < x:
        return tenToCh(num)

    return tenToX(num // x, x) + tenToCh(num % x)


def ten(s):
    """
    字符转数字
    """
    if s > "9":
        return ord(s) - 97 + 10

    return int(s)


def xToTen(numStr, x):
    """
    x进制转十进制
    """
    if len(numStr) == 1:
        return ten(numStr)

    return xToTen(numStr[:-1]) * x + ten(numStr[-1])


def xToY(x, numStr, y):
    """
    x进制转y进制
    """
    return tenToX(xToTen(numStr, x), y)

