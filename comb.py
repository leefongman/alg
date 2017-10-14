#!/usr/bin/env python3

def combine(string):
    """
    字符串string中存储互不相同的多个字符,输出互不相同的排列组合
    """
    length = len(string)

    if length == 1:
        return [string]

    new = []

    for i in range(length):
        s = ["", string[0: i]][i > 0] + ["",
                string[i + 1: length]][i < length - 1]
        new += list(map(lambda a:string[i] + a, combine(s)))

    return new


if __name__ == "__main__":
    s = "123456789"
    combList = combine(s)
    for l in combList:
        print(l)
    print("共有", len(combList), "种排列组合")

