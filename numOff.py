#!/usr/bin/env python3

def numOff(m, n):
    """
    m个人围成一圈循环报数退出
    """
    mList = list(range(1, M + 1))

    count = 0
    while mList:
        x = mList.pop(0)
        count += 1
        if count == n:
            print(x)
            count = 0
        else:
            mList.append(x)


if __name__ == "__main__":
    pass
