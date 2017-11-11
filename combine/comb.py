#!/usr/bin/env python3

def combine(s):
    """
    字符串s中存储互不相同的多个字符,输出互不相同的排列组合
    """
    length = len(s)

    if length == 1:
        return [s]

    new = []

    for i in range(length):
        #  去除第i个元素作为组合的载体
        s = ["", s[0: i]][i > 0] + ["", s[i + 1: length]][i < length - 1]
        #  依次累加以第i个字符开头的所有组合
        new += list(map(lambda a: s[i] + a, combine(s)))

    return new


if __name__ == "__main__":
    s = "123456789"
    combList = combine(s)
    for l in combList:
        print(l)
    print("共有", len(combList), "种排列组合")

