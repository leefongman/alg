#!/usr/bin/env python3

import os


def combine(ls):
    """
    列表ls中存储互不相同的多个字符,输出互不相同的排列组合
    """
    #  列表中只有一个元素时,返回列表[ls]
    if len(ls) == 1:
        return [ls]

    #  提取最后一个元素,用于递归组合
    last = ls[-1]
    #  除去最后一个元素的组合列表
    old = combine(ls[:-1])
    #  用于存储最终的组合列表
    new = []

    for comb in old:
        #  用最后一个元素插入到旧组合列表中元素的所有位置
        for idx in range(len(ls)):
            lT = comb.copy()
            lT.insert(idx, last)
            new.append(lT)


    return new


if __name__ == "__main__":
    ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    combList = combine(ls)
    for l in combList:
        print("".join(l))

