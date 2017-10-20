#!/usr/bin/env python3

def stairway(num):
    """
    每次跨1到3阶楼梯,求到达num阶楼梯顶端的所有组合
    """
    if num == 1:
        return [[1]]

    count = []

    for n in range(1, 4):
        if num - n > 0:
            count += list(map(lambda ls: ls + [n], stairway(num - n)))

    return count

if __name__ == "__main__":
    pass
