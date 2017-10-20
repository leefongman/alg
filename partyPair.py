#!/usr/bin/env python3

def pair(numMore, numLack, n):
    """
    舞会配对,前n轮配对情况
    """
    if n == 1:
        return [[(x, x) for x in range(1, numLack + 1)]]

    pairLast = pair(numMore, numLack, n - 1)
    left = pairLast[-1][-1][0] + 1

    return pairLast + [[([x % numMore, numMore][x == numMore], y)
        for x, y in zip(range(left, left + numLack), range(1, numLack + 1))]]


if __name__ == "__main__":
    pass
