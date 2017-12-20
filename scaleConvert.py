#!/usr/bin/env python3


def ten2Ch(num):
    """
    数字转字符
    """
    return chr(num + 48) if num < 10 else chr(num - 10 + 97)


def ten2X(num, x):
    """
    十进制转x进制
    """
    if num < x:
        return ten2Ch(num)

    return ten2X(num // x, x) + ten2Ch(num % x)


def ten(s):
    """
    字符转数字
    """
    return (ord(s) - 97 + 10) if s > "9" else (ord(s) - 48)


def x2Ten(numStr, x):
    """
    x进制转十进制
    """
    if len(numStr) == 1:
        return ten(numStr)

    return x2Ten(numStr[:-1], x) * x + ten(numStr[-1])


def x2y(x, numStr, y):
    """
    x进制转y进制
    """
    return ten2X(x2Ten(numStr, x), y)


if __name__ == "__main__":
    print(x2y(10, '234689723468716', 16))
