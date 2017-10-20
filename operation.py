#!/usr/bin/env python3

def add(a, b):
    """
    加法运算
    """
    adds = ""
    length = max(len(a), len(b))
    a, b = a.rjust(length, "0"), b.rjust(length, "0")
    carry = 0

    for i in range(1, length + 1):
        numAdd = carry
        numAdd += ord(a[-i]) + ord(b[-i]) - 96
        adds = chr(numAdd % 10 + 48) + adds
        carry = numAdd // 10

    return "1" + adds if carry == 1 else adds


def sub(a, b):
    """
    减法运算
    """
    subs = ""
    length = max(len(a), len(b))
    a, b = a.rjust(length, "0"), b.rjust(length, "0")
    a, b, sign = (b, a, "-") if a < b else (a, b, "")
    lose = 0
    start = length

    for i in range(1, length + 1):
        numSub = -lose
        lose = 1 if ord(a[-i]) - lose < ord(b[-i]) else 0
        numSub += ord(a[-i]) + lose * 10 - ord(b[-i])
        subs = chr(numSub + 48) + subs
        start = (length - i) if subs > "1" else start

    return 0 if start == length else sign + subs[start:]


if __name__ == "__main__":
    pass

